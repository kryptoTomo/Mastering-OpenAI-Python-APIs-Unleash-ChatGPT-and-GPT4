import openai
from dotenv import dotenv_values

config = dotenv_values("/home/freshman/Mastering-OpenAI-Python-APIs-Unleash-ChatGPT-and-GPT4/.env")

client = openai.OpenAI(
  api_key=config["OPENAI_API_KEY"],
)



prompt = """
you are a chat bot that speaks like a toddler
User: Hi, how are you?
Chatbot: I'm good
User: Tell me about your family
Chatbot: I have a moomy and a daddy and a baby sister and two kitties
User: What do you do for fun?
Chatbot: I wike to play with my toys and watch cartoons and pway outside with my fwiends.
User:"""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", 
     "content": prompt}
  ],
  max_tokens=100,
  stop="5."
)

print(completion)