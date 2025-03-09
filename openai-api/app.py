import os
from openai import OpenAI
from openai import AsyncOpenAI
from openai_client import OpenAIClient


def chat_with_gpt(client: OpenAI, prompt: str) -> str:
    messages: list[dict[str, str]] = [
        {
            "role": "user",
            "content": prompt
        },
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
        # temperatureは0.0から1.0の間で設定できる
        # temperatureは0.0にすると、最も確信度の高い回答を返す
        # temperature=0.0,
        temperature=1.0,
    )

    return chat_completion.choices[0].message.content

def main() -> None:
    # Create an OpenAI client
    openai_client = OpenAIClient()
    client = openai_client.get_client()

    # Testing on console
    user_input = input("入力: ")

    response = chat_with_gpt(client, user_input)
    # response = chat_with_gpt(async_client, user_input)

    print("\nAIの応答:\n", response)

if __name__ == "__main__":
    main()
