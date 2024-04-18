#가상화폐 시세를 데이터베이스에 10초마다 입력하기
import pyupbit
import sqlite3
import datetime
import time

conn = sqlite3.connect(r'D:\Joo.min.hee\IOT강의\Source.1\pyupbit\upbit.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS BTC_KRW (time TEXT, price INTEGER)")

while True:
    try:
        price = pyupbit.get_current_price("KRW-BTC")
        now = datetime.datetime.now()

        print(now,price)

        # 데이터베이스에 저장
        cur.execute("INSERT INTO BTC_KRW (time, price) VALUES (?, ?)", (now, price))
        conn.commit

        time.sleep(10)

    except Exception as e:
        print(e)
        time.sleep(1)

# 연결 종료
conn.close()