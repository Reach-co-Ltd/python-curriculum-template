# curriculum_12 / アプリ制作②（FastAPI + PostgreSQL + Docker）

## このカリキュラムについて

アプリ制作①で作ったCLIのToDoアプリを、Webアプリとして動く形に発展させます。
あなたが実装するのは `backend/` フォルダの5つのファイルだけです。
フロントエンドと環境設定は最初から用意されています。

## フォルダ構成

```
curriculum_12_start/
├── backend/
│   ├── main.py          ← あなたが実装する（TODOコメントあり）
│   ├── models.py        ← あなたが実装する（TODOコメントあり）
│   ├── schemas.py       ← あなたが実装する（TODOコメントあり）
│   ├── database.py      ← あなたが実装する（TODOコメントあり）
│   ├── task_manager.py  ← あなたが実装する（TODOコメントあり）
│   ├── requirements.txt ← 変更不要
│   ├── Dockerfile       ← 変更不要
│   └── tests/
│       ├── conftest.py  ← 変更不要
│       └── test_tasks.py ← あなたが実装する
├── frontend/            ← 変更不要（完成品）
├── docker-compose.yml   ← 変更不要
├── .env                 ← 変更不要
└── .gitignore
```

## 環境構築

### 前提条件の確認

```bash
docker --version
docker compose version
```

バージョンが表示されれば準備OKです。
表示されない場合は https://www.docker.com/products/docker-desktop/ から
Docker Desktop をインストールして、PCを再起動してください。

### 起動手順

```bash
# このフォルダに移動する
cd curriculum_12_start

# 起動する（初回は5〜10分かかります）
docker compose up --build
```

以下のメッセージが出れば起動完了です。

```
backend-1  | INFO: Uvicorn running on http://0.0.0.0:8000
frontend   | ▲ Next.js ready on http://localhost:3000
```

### 確認URL

| URL | 内容 |
|---|---|
| http://localhost:3000 | フロントエンド（ToDoアプリ画面） |
| http://localhost:8000/docs | Swagger UI（APIの動作確認画面） |

### 停止方法

```bash
# 停止する（データは残る）
docker compose down

# データごと削除してやり直す場合
docker compose down -v
```

## 実装の進め方

**この順番を守ってください。順番を守らないとエラーになります。**

1. `backend/database.py` の `get_db()` を実装する
2. `backend/models.py` の `Task` クラスを実装する
3. `docker compose up --build` でエラーなく起動することを確認する
4. `backend/schemas.py` の `TaskCreate`・`TaskResponse` を実装する
5. `backend/task_manager.py` の各関数を実装する
6. `backend/main.py` のエンドポイントを実装する
7. Swagger UI（http://localhost:8000/docs）で動作確認する
8. `backend/tests/test_tasks.py` のテストを実装する

**1つ実装するたびに Swagger UI で動作確認してください。**
まとめて実装してから確認すると、どこで間違えたかわからなくなります。

## よくあるエラーと対処法

**「Cannot connect to the Docker daemon」**
→ Docker Desktop が起動していません。アプリを起動してから再実行してください。

**「port is already in use」**
→ 同じポートを使っている別のコンテナが動いています。
`docker compose down` を実行してから再起動してください。

**「connection refused」（起動直後）**
→ DBの起動が完了する前にバックエンドが起動しています。
もう一度 `docker compose up` を実行すると解決します。

## 提出方法

```bash
git add .
git commit -m "curriculum_12: アプリ制作② 完成"
git push origin main
```
