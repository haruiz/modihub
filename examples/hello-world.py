from PIL import Image
from dotenv import find_dotenv, load_dotenv

from modihub.llm import LLM

load_dotenv(find_dotenv())

if __name__ == "__main__":
    available_models = LLM.available_models()
    for client, models in available_models.group_by("client"):
        for model in models:
            print(f"{client}: {model.name}")

    for model in available_models.filter_by("client", "openai"):
        print(model)

    llm = LLM.create("models/gemini-1.5-flash-8b")
    image = Image.open("image.png")
    text = "Describe the following image"
    prompt = [text, image]
    response = llm(prompt)
    print(response)