#데이터베이스에서 값 읽어 확인하기
import sqlite3

conn = sqlite3.connect(r'D:\Joo.min.hee\IOT강의\Source.1\pyupbit\upbit.db')
cur = conn.cursor()

cur.execute("SELECT * FROM BTC_KRW")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()