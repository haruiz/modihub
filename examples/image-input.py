from PIL import Image
from modihub.llm import LLM
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

llm = LLM.create("models/gemini-1.5-flash-8b")
image = Image.open("image.png")  # Replace with the path to your image
text = "Describe the following image"
prompt = [text, image]
response = llm(prompt)
print(response)