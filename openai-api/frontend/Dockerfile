FROM node:14

WORKDIR /

COPY ./frontend/package.json ./frontend/
COPY ./frontend/package-lock.json ./frontend/
COPY ./frontend/tsconfig.json ./frontend/
COPY ./frontend/public/ ./frontend/public/
COPY ./frontend/src/ ./frontend/src/
COPY ./config/.env.dev ./config/

WORKDIR /frontend

RUN npm install
RUN npm run build

EXPOSE 3000
CMD ["npx", "serve", "-s", "build"]

