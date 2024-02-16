import time
import asyncio

from openai import OpenAI

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI()

def send_request(user_input):
    # Streaming:
    print("----- streaming request -----")
    stream = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_input,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://plus.unsplash.com/premium_photo-1664048713363-7e18285e3053?q=80&w=3540&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        },
                    }
                ]
            },
        ],
        stream=False,
    )
    return stream

def main():
    while True:
        user_input = input()
        if user_input == "break":
            break
        stream = send_request(user_input)
        print(stream)
        for chunk in stream: 
            if 'choices' in chunk:
                print(chunk[1][0].message.content)

if __name__ == "__main__":
    main()
