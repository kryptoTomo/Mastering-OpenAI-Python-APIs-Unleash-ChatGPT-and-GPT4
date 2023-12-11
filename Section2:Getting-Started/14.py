import openai
from dotenv import dotenv_values

config = dotenv_values("/home/freshman/Mastering-OpenAI-Python-APIs-Unleash-ChatGPT-and-GPT4/.env")

client = openai.OpenAI(
  api_key=config["OPENAI_API_KEY"],
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "The top 10 most populated cities are: "}
  ],
  max_tokens=100
)

print(completion.choices[0].message)