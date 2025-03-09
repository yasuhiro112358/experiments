import os
from dotenv import load_dotenv
from openai import OpenAI
from openai import AsyncOpenAI

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
    # Load environment variables from a .env file
    load_dotenv()

    # Access environment variables
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    if not OPENAI_API_KEY:
        print("ERROR: OpenAI APIキーが設定されていません")
        exit(1)

    # Create an OpenAI client
    client = OpenAI(api_key=OPENAI_API_KEY)

    # Create an AsyncOpenAI client
    async_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    # Testing on console
    user_input = input("入力: ")

    response = chat_with_gpt(client, user_input)
    # response = chat_with_gpt(async_client, user_input)

    
    print("\nAIの応答:\n", response)

if __name__ == "__main__":
    main()
