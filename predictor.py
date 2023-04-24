import torch
from transformers import LlamaForCausalLM, LlamaTokenizer, GPTNeoForCausalLM, AutoTokenizer, pipeline

# model = LlamaForCausalLM.from_pretrained(
#     "vicuna-7B", torch_dtype=torch.float16, device_map='auto').to('cuda')
tokenizer = LlamaTokenizer.from_pretrained("vicuna-7B")


model = GPTNeoForCausalLM.from_pretrained(
    "gpt-neo-2.7B", torch_dtype=torch.float16, device_map='auto').to('cuda')
tokenizer = AutoTokenizer.from_pretrained("gpt-neo-2.7B")

# create pipeline
gen = pipeline("text-generation", model=model,
               tokenizer=tokenizer)
res = gen("Hello world,", max_length=50, do_sample=True, temperature=0.9)
# run prediction
print(res[0]["generated_text"])
