FROM mongo:latest

WORKDIR /

# 公式イメージはこのディレクトリにあるファイルを初回起動時に実行する
COPY ./database/init-mongo.js /docker-entrypoint-initdb.d/