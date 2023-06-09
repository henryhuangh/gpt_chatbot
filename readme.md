# Getting Started

deploy on ec2 g4 instance Deep Learning AMI GPU PyTorch 2.0.0.

in the terminal run

`source activate pytorch`

`git clone https://github.com/henryhuangh/gpt_chatbot.git`

`cd gpt_chatbot`

`sh installer.sh`

`flask --app=server.py run --host=0.0.0.0 --port=80`

# Setup EC2 Instance

It will need ports 80, 22 and 443 open. Configure this in EC2 security groups.

# Auto GPT

[AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ)
`pip install git+https://github.com/PanQiWei/AutoGPTQ`

# Langchain CustomLLM Usage

```python
from custom_LLM import CustomLLM
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


llm = CustomLLM(streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

conversation.predict(input="Hello there")
```
