# OpenAI API コンソールアプリ

## 環境構築
1. `.env.example` をコピーして `.env` を作成
```bash
cp .env.example .env
```

2. OpneAIのAPIキーを設定

3. Dockerコンテナを起動
```bash
docker compose run --rm openai_app
```
* --rm オプションはコンテナを終了したら削除するオプション

## 使い方
- 起動後、プロンプトを入力すると OpenAI API からの応答が表示されます

