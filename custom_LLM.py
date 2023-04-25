from pyexpat import model
from langchain.llms.base import LLM
from transformers import pipeline
from llama_index import SimpleDirectoryReader, LangchainEmbedding, GPTListIndex, PromptHelper
from typing import Optional, List, Mapping, Any
from transformers import LlamaForCausalLM, LlamaTokenizer, AutoTokenizer, GPTNeoForCausalLM, GPT2LMHeadModel, GPT2TokenizerFast
import torch
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:24"
torch.cuda.empty_cache()
# define prompt helper
# set maximum input size
max_input_size = 2048
# set number of output tokens
num_output = 256
# set maximum chunk overlap
max_chunk_overlap = 20

prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)


model = GPTNeoForCausalLM.from_pretrained(
    "gpt-neo-2.7B")
tokenizer = AutoTokenizer.from_pretrained("gpt-neo-2.7B")


class CustomLLM(LLM):
    # model_name = 'vicuna-7B'
    # model = LlamaForCausalLM.from_pretrained(
    # "vicuna-7B", torch_dtype=torch.float16, device_map='auto', load_in_8bit=True)
    # tokenizer = LlamaTokenizer.from_pretrained("vicuna-7B")
    model_name = 'gpt-neo-2.7B'
    # model = GPT2LMHeadModel.from_pretrained(
    # "gpt2-large")
    # tokenizer = GPT2TokenizerFast.from_pretrained("gpt2-large")
    pipeline = pipeline("text-generation", model=model,
                        tokenizer=tokenizer)

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        prompt_length = len(prompt)
        response = self.pipeline(prompt, max_new_tokens=num_output)[
            0]["generated_text"]

        # only return newly generated tokens
        return response[prompt_length:]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"name_of_model": self.model_name}

    @property
    def _llm_type(self) -> str:
        return "custom"
