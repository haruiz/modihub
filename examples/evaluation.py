from dotenv import find_dotenv, load_dotenv
from modi.metrics import Perplexity, LexicalDiversity
from modi.eval import Evaluator

load_dotenv(find_dotenv())

prompts = [
    "What are LLMs?",
    "Explain AI", "What is the meaning of life?"]
models = [
    "gpt-4o-mini",
    "llama3.1:latest",
    "models/gemini-1.5-flash-latest"
]
metrics = [Perplexity(), LexicalDiversity()]

evaluator = Evaluator(models, metrics)
results = {prompt: evaluator.evaluate(prompt) for prompt in prompts}
for prompt, result in results.items():
    print(f"Prompt: {prompt}")
    for model, metrics in zip(models, result):
        print(f"{model}: {metrics}")
    print()