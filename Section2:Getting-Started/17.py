import openai
from dotenv import dotenv_values

config = dotenv_values("/home/freshman/Trainings/Mastering-OpenAI-Python-APIs-Unleash-ChatGPT-and-GPT4/.env")

client = openai.OpenAI(
  api_key=config["OPENAI_API_KEY"],
)



prompt = """Q: What is the tallest building in the world?"""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", 
     "content": prompt}
  ],
  max_tokens=100,
  n=3,
#   echo=True ?
)

print(completion)