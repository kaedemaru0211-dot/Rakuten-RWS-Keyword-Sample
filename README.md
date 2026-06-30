# Rakuten RWS Keyword Sample

楽天市場の Rakuten Web Service Ichiba Item Search API を使って、keyword 検索で商品情報を取得する最小サンプル。

申請用の推奨アプリ名: `Rakuten RWS Keyword Sample`

この repo の用途は 2 つ。

- 楽天API申請時の Application URL / Allowed websites 用の公開説明
- keyword 検索サンプルコードの公開

スクレイピングは含めない。公式APIのみ使う。

## 1. この repo がやること

- keyword で楽天市場の商品を検索
- `itemName`, `itemPrice`, `itemUrl`, `shopName` を取得
- `minPrice`, `maxPrice`, `availability`, `hits` を指定可能
- GitHub Pages 用の説明ページを同梱

## 2. ファイル構成

```text
.
├── .env.example
├── .gitignore
├── README.md
├── docs/
│   └── 電脳せどり_楽天API申請メモ_20260630.md
├── index.html
├── requirements.txt
└── scripts/
    └── search_keyword.py
```

## 3. 使い方

### 3.1 依存インストール

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3.2 環境変数

`.env.example` を `.env` にコピーして埋める。

```text
RAKUTEN_APP_ID=your_application_id
RAKUTEN_ACCESS_KEY=your_access_key
```

### 3.3 実行例

```bash
python scripts/search_keyword.py "Braun 替刃 52B" --min-price 3000 --max-price 12000 --hits 10
```

## 4. GitHub Pages に出す内容

`index.html` をそのまま公開ページに使う。

`index.html` に設定済みの値:

| 項目 | 値 |
|---|---|
| GitHubユーザー名 | `kaedemaru0211-dot` |
| 運営者名 | Daisuke Oura |
| 連絡先 | daisu.k.oura@gmail.com |
| 公開URL | `https://kaedemaru0211-dot.github.io/Rakuten-RWS-Keyword-Sample/` |

## 5. 楽天申請フォームの記入例

### 5.1 Application name

```text
Rakuten RWS Keyword Sample
```

### 5.2 Application URL

```text
https://kaedemaru0211-dot.github.io/Rakuten-RWS-Keyword-Sample/
```

### 5.3 Allowed websites

```text
https://kaedemaru0211-dot.github.io
```

### 5.4 Purpose of data usage

```text
楽天市場商品検索APIを用いて商品情報を取得し、価格比較と仕入れ候補抽出の検証を行うため
```

### 5.5 Expected QPS

```text
1
```

## 6. 申請前チェック

- [ ] Application name を申請フォームに入力した
- [x] `index.html` の運営者名と連絡先を設定した
- [x] GitHub に push した
- [ ] GitHub Pages を有効化した
- [ ] 公開URLでページが開く
- [x] スクレイピング前提の表現を消した
- [x] `RAKUTEN_ACCESS_KEY` を使う実装にした

## 7. 注意

- 2026-06 時点の楽天市場商品検索APIは `applicationId` に加えて `accessKey` も必要
- `localhost` やダミーURLは Application URL に使わない
- 公式APIがある取得元は公式APIを優先する

