import sqlite3
import matplotlib.pyplot as plt
# 데이터베이스 파일에 연결
conn = sqlite3.connect(r'D:\Joo.min.hee\IOT강의\Source.1\pyupbit\upbit.db')
# 쿼리문 작성
query = 'SELECT * FROM BTC_KRW'
# 데이터 가져오기
cur = conn.cursor()
cur.execute(query)
rows = cur.fetchall()
# 날짜와 금액을 분리하여 리스트에 저장
dates = [row[0] for row in rows]
amounts = [row[1] for row in rows]
# 그래프 그리기
fig, ax = plt.subplots()
ax.bar(dates, amounts)
ax.set_xlabel('Date')
ax.set_ylabel('Amount')
ax.set_title('Upbit Data')
plt.show()
# 연결 종료
conn.close()


import sqlite3
import matplotlib.pyplot as plt
# 데이터베이스 파일에 연결
conn = sqlite3.connect(r'D:\Joo.min.hee\IOT강의\Source.1\pyupbit\upbit.db')
# 쿼리문 작성
query = 'SELECT * FROM BTC_KRW'
# 데이터 가져오기
cur = conn.cursor()
cur.execute(query)
rows = cur.fetchall()
# 날짜와 금액을 분리하여 리스트에 저장
dates = [row[0] for row in rows]
amounts = [row[1] for row in rows]
# 그래프 그리기
fig, ax = plt.subplots()
ax.scatter(dates, amounts, s=10)
ax.set_xlabel('Date')
ax.set_ylabel('Amount')
ax.set_title('Upbit Data')
plt.show()
# 연결 종료
conn.close()