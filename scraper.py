import json
import os

def fetch_live_events():
    events = [
        # Snow Man
        {
            "group": "Snow Man", 
            "category": "ライブ",
            "date": "2026-11-15", 
            "title": "Snow Man Dome Tour 2026", 
            "venue": "東京ドーム", 
            "open_time": "16:00",
            "start_time": "18:00",
            "status": "当落発表済",
            "notice": ""
        },
        {
            "group": "Snow Man", 
            "category": "メディア",
            "date": "2026-11-18", 
            "title": "〇〇テレビ「音楽特番」生出演", 
            "venue": "テレビ放送", 
            "open_time": "19:00",
            "start_time": "19:00",
            "status": "放送予定",
            "notice": "⚠️ 放送時間が変更になる可能性があります"
        },
        
        # SixTONES
        {
            "group": "SixTONES", 
            "category": "ライブ",
            "date": "2026-11-20", 
            "title": "SixTONES LIVE TOUR 2026", 
            "venue": "横浜アリーナ", 
            "open_time": "17:30",
            "start_time": "18:30",
            "status": "受付中",
            "notice": ""
        },
        {
            "group": "SixTONES", 
            "category": "メディア",
            "date": "2026-11-22", 
            "title": "ラジオ「SixTONESのオールナイトニッポン」", 
            "venue": "ラジオ・配信", 
            "open_time": "23:30",
            "start_time": "23:30",
            "status": "レギュラー",
            "notice": ""
        },
        
        # King & Prince
        {
            "group": "King & Prince", 
            "category": "ライブ",
            "date": "2026-11-28", 
            "title": "King & Prince LIVE TOUR 2026", 
            "venue": "マリンメッセ福岡", 
            "open_time": "16:30",
            "start_time": "17:30",
            "status": "一般発売中",
            "notice": ""
        }
    ]
    
    with open("events.json", "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)
    print("最新のスケジュール情報を更新しました！")

if __name__ == "__main__":
    fetch_live_events()
