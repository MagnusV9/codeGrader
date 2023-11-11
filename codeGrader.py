from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import sys

llm = Ollama(
    model="llama2", 
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

if len(sys.argv) < 1:
    print("whoops seems like you did not pass a file to grade...")
    exit()

file = sys.argv[1]

file_content = []

with open (file, "r") as f:
    content = f.read()

    for text in content:
        file_content.append(text)


file_content = ",".join(file_content)
file_type = file.split(".")
file_type = file_type[-1]
gen_prompt = f"""you are given code in a programming language that has the {file_type} extension, now grade the following code on a scale from f to a where a is best 
                 and give your reasoning. """

print(llm(gen_prompt + file_content))





    





