from src.openai_client import OpenAIClient

class Persona:
    def __init__(self, name, personality, memory=None):
        self.name = name
        self.personality = personality
        self.memory = memory if memory else []  # 過去の会話履歴
        self.client = OpenAIClient().get_client()

    def chat(self, user_input) -> str:
        """ChatGPTを使って会話を行う"""
        messages = [{"role": "system", "content": self.personality}]
        messages += self.memory  # 過去の会話履歴を追加
        messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            # temperatureは0.0から1.0の間で設定できる
            # temperatureは0.0にすると、最も確信度の高い回答を返す
            # temperature=0.0,
            temperature=1.0,
        )
        reply = response.choices[0].message.content

        # 会話履歴に追加
        # この部分は切り分けても良いかもしれない
        self.memory.append({"role": "user", "content": user_input})
        self.memory.append({"role": "assistant", "content": reply})

        return reply