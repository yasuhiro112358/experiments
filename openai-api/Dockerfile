# Pythonの公式イメージを使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt ./
COPY app.py ./

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリ実行
CMD ["python", "app.py"]
