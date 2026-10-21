import json
import os

# 本来はここで公式サイトやまとめサイトをスクレイピング（自動取得）します。
# ※まずは動作テスト用に最新のツアー日程データを自動生成するコードにしています。
def fetch_live_events():
    events = [
        {"date": "2026-11-15", "title": "ドームツアー 2026（東京ドーム）", "status": "当落発表済"},
        {"date": "2026-12-05", "title": "ドームツアー 2026（バンテリンドーム）", "status": "一般発売中"},
        {"date": "2026-12-24", "title": "ドームツアー 2026（京セラドーム）", "status": "申込受付中"},
    ]
    
    # events.json として保存
    with open("events.json", "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)
    print("最新イベント情報を更新しました！")

if __name__ == "__main__":
    fetch_live_events()
