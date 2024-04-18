"""import datetime

print("날짜 계산기 프로그램입니다.")
print("연도, 월, 일을 차례로 입력하세요.")
year = int(input("연도: "))
month = int(input("월: "))
day = int(input("일: "))

given_date = datetime.date(year, month, day)

print("입력한 날짜는",given_date.strftime("%Y년 %m월 %d일"), "입니다.")
print("이 날짜에서 몇 일을 더하거나 빼시겠습니까?")
days_diff = int(input("일 수:"))

result_date = given_date + datetime.timedelta(days=days_diff)

print(days_diff, "일을 더하거나 빼면",result_date.strftime("%Y년 %m월 %d일"), "입니다.")"""



"""import datetime

print("기준 날짜부터 오늘까지 몇일이 지났는지 계산하는 프로그램입니다.")
print("연도, 월, 일을 차례로 입력하세요.")
year = int(input("연도: "))
month = int(input("월: "))
day = int(input("일: "))

start_date = datetime.date(year, month, day)
end_date = datetime.date.today()

days_diff = (end_date - start_date).days

print(start_date.strftime("%Y년 %m월 %d일"), "부터 오늘까지",days_diff, "일이 지났습니다.")"""


"""import tkinter as tk
import datetime

def calculate_days():
    start_date = datetime.date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    end_date = datetime.date.today()
    days_diff = (end_date - start_date).days
    result_iabel.config(text=f"{start_date.strftime('%Y년 %m일 %d일')}부터 오늘까지 {days_diff}일이 지났습니다.")

rook = tk.Tk()
rook.title("날짜 계산기")

year_label = tk.Label(rook, text="연도")
year_label.grid(row=0, column=0)
year_entry = tk.Entry(rook)
year_entry.grid(row=0, column=1)

month_label = tk.Label(rook, text="월")
month_label.grid(row=1, column=0)
month_entry = tk.Entry(rook)
month_entry.grid(row=1, column=1)

days_label = tk.Label(rook, text="일")
days_label.grid(row=2, column=0)
days_entry = tk.Entry(rook)
days_entry.grid(row=2, column=1)

calculate_button = tk.Button(rook, text="계산", command=calculate_days)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(rook, text="")
result_label.grid(row=4, column=0, columnspan=2)

rook.mainloop()"""


"""import pyupbit
# 원화 시장에서 BTC/KRW의 현재가를 조회합니다.
price = pyupbit.get_current_price("KRW-BTC")

# 조회한 현재가를 출력합니다.
print("현재 BTC/KRW의 가격은", price, "원입니다.")"""


"""#모든 가상화폐 시세조회하기
import pyupbit

tickers = pyupbit.get_tickers()

for ticker in tickers:
    try:
        price = pyupbit.get_current_price(ticker)
        print(ticker, price)
    except:
        pass"""

"""# 비트코인 1년 그래프 그리기
import pyupbit
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

to_date = datetime.now()
from_date = to_date - timedelta(days=365)

df=pyupbit.get_ohlcv("KRW-BTC", interval="day",to=to_date, count=365)

#그래프의 x축 값을 지정
x_values = pd.date_range(start=from_date, end=to_date - timedelta(days=1), freq='D')

#그래프를 그립니다.
plt.plot(x_values, df['close'])

#그래프 제목과 레이블을 추가
plt.title('Bitcoin Price in KRW (1 year)')
plt.xlabel('Date')
plt.ylabel('Price (KRW)')

#x축에 레이블을 45도로 회전
plt.xticks(rotation=45)

plt.show()"""

"""#가상화폐 시세를 데이터베이스에 입력하기
import pyupbit
import sqlite3
import datetime

conn = sqlite3.connect(r'D:\Joo.min.hee\IOT강의\Source.1\pyupbit\upbit.db')
cur = conn.cursor()

# 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS BTC_KRW (time TEXT, price INTEGER)")

# 시세 조회
price = pyupbit.get_current_price("KRW-BTC")
now = datetime.datetime.now()

# 조회 결과 출력
print(now,price)

# 데이터베이스에 저장
cur.execute("INSERT INTO BTC_KRW (time, price) VALUES (?, ?)", (now, price))
conn.commit()

# 연결 종료
conn.close()"""


"""#가상화폐 시세를 데이터베이스에 10초마다 입력하기
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
conn.close()"""

"""#데이터베이스에서 값 읽어 확인하기
import sqlite3

conn = sqlite3.connect(r'D:\Joo.min.hee\IOT강의\Source.1\pyupbit\upbit.db')
cur = conn.cursor()

cur.execute("SELECT * FROM BTC_KRW")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()"""



