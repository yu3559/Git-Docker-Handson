# Pythonの公式イメージをベースにする
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコンテナにコピー
COPY requirements.txt .

# 依存ライブラリをインストール
RUN pip install -r requirements.txt

# コンテナ起動時にスクリプトを実行
CMD ["python", "main.py"] 