from __future__ import annotations

import argparse
import os
from typing import Any

import httpx
from dotenv import load_dotenv


API_URL = "https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401"
ELEMENTS = "itemName,itemPrice,itemUrl,shopName"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="楽天市場商品検索APIで keyword 検索を行う。"
    )
    parser.add_argument("keyword", help="検索キーワード")
    parser.add_argument("--min-price", type=int, default=None, help="最低価格")
    parser.add_argument("--max-price", type=int, default=None, help="最高価格")
    parser.add_argument("--hits", type=int, default=10, help="取得件数 1-30")
    parser.add_argument("--page", type=int, default=1, help="ページ番号 1-100")
    parser.add_argument(
        "--availability",
        type=int,
        choices=(0, 1),
        default=1,
        help="0: 全商品, 1: 在庫ありのみ",
    )
    return parser


def build_params(args: argparse.Namespace, app_id: str, access_key: str) -> dict[str, Any]:
    params: dict[str, Any] = {
        "applicationId": app_id,
        "accessKey": access_key,
        "format": "json",
        "formatVersion": 2,
        "keyword": args.keyword,
        "availability": args.availability,
        "hits": args.hits,
        "page": args.page,
        "elements": ELEMENTS,
    }
    if args.min_price is not None:
        params["minPrice"] = args.min_price
    if args.max_price is not None:
        params["maxPrice"] = args.max_price
    return params


def main() -> int:
    load_dotenv()
    app_id = os.getenv("RAKUTEN_APP_ID")
    access_key = os.getenv("RAKUTEN_ACCESS_KEY")
    if not app_id or not access_key:
        raise SystemExit("RAKUTEN_APP_ID と RAKUTEN_ACCESS_KEY を設定してください。")

    parser = build_parser()
    args = parser.parse_args()
    params = build_params(args, app_id, access_key)

    response = httpx.get(API_URL, params=params, timeout=20)
    response.raise_for_status()

    items = response.json().get("items", [])
    if not items:
        print("0件")
        return 0

    for index, item in enumerate(items, start=1):
        print(f"[{index}] {item['itemName']}")
        print(f"  価格: {item['itemPrice']}円")
        print(f"  店舗: {item['shopName']}")
        print(f"  URL: {item['itemUrl']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
