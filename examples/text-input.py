from modihub.llm import LLM
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv()) # Loads API keys from .env file

# Replace with your desired model
llm = LLM.create("gpt-4o-mini")
# Generate text
response = llm("Tell me a joke about AI.")
print(response)