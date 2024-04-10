import os
import openai
import argparse
from dotenv import load_dotenv

PROMPT="""
You will receive a file's contents as text.
Generate a code review for the file. Indicate what changes should be made to improve 
its style, performance, readability, and maintainability. If there are any reputable 
libraries that could be introduced to improve the code, suggest them. Be kind and constructive.
For each suggested change, include line numbers to whichc you are referring
"""


def code_review(client, file_path, model):
    with open(file_path, "r") as file:
        content = file.read()

    generated_code_review = make_code_review_request(client, content, model)
    print(generated_code_review)


def make_code_review_request(client, fileContent, model):
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": f"Code review the following file: {fileContent}"}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    return response.choices[0].message.content


def main(client):
    parser = argparse.ArgumentParser(description="Simple code reviewer for a file")
    parser.add_argument("file")
    parser.add_argument("--model", default="gpt-4")
    args = parser.parse_args()

    code_review(client, args.file, args.model)


if __name__ == "__main__":
    load_dotenv()

    client = openai.OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    main(client)
