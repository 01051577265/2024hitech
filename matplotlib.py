import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

conn = sqlite3.connect(r'D:\Joo.min.hee\IOT강의\Source.1\query\upbit.db')

query = 'SELECT * FROM BTC_KRW'

cur = conn.cursor()
cur.execute(query)
rows = cur.fetchall()

# 날짜와 금액을 분리하여 리스트에 저장
dates = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in rows]
amounts = [row[1] for row in rows]

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot_date(dates, amounts, '-')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))  # x 축에 날짜 형식 지정
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Upbit Data')
plt.xticks(rotation=45)  # x 축 눈금 레이블 회전
plt.tight_layout()  # 그래프 여백 조정
plt.show()

# 연결 종료
conn.close()



