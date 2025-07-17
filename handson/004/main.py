import os
from dotenv import load_dotenv
from chat_client import ChatClient

# .envファイルから環境変数をロード
# プロジェクトルートの .env ファイルを探索して読み込む
load_dotenv()

# 環境変数からAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")

def main():
    if not api_key:
        raise ValueError("❌ APIキーが設定されていません。.envファイルを確認してください。")

    # ChatClientのインスタンスを作成
    chat_client = ChatClient(api_key)

    # AIに送信するメッセージ
    message = "こんにちは！自己紹介をしないでください。"

    # メッセージを送信して返信を取得
    response = chat_client.send_message(message)

    if response:
        print("-----------------------------------")
        print(f"🤖 AIからの返信:\n{response}")
        print("-----------------------------------")

if __name__ == "__main__":
    main() 