from openai import OpenAI


class ChatClient:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("❌ APIキーが設定されていません。.envファイルを確認してください。")
        self.client = OpenAI(api_key=api_key)
        print("✅ APIキーを環境変数から取得しました。")

    def send_message(self, message):
        try:
            print("🤖 OpenAIのChat APIにメッセージを送信します...")
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant.",
                    },
                    {
                        "role": "user",
                        "content": message,
                    },
                ],
                model="gpt-4o",
            )
            print("✅ メッセージの受信に成功しました！")
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"😱 API呼び出し中にエラーが発生しました: {e}")
            return None 