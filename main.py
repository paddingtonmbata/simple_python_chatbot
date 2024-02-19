from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
print(os.environ["OPENAI_API_KEY"])
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)

def chatbot():
    # to remember previous user inputs as context throughout the session
    messages = [
        {"role": "system", "content":"You're a very helpful assistant."},
    ]
    while True:
        message = input("User: ")

        if message.lower() == "quit":
            print("Chat ended!")
            break
        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chat_message = response.choices[0].message.content
        print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content":chat_message})

if __name__ == "__main__":
    print("This is an ai chatbot start chatting (type in 'quit' to stop chatting)")
    chatbot()