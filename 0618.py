import requests
import tkinter as tk
from tkinter import messagebox

def get_exchange_rate():
    base_currency = 'USD'  # 기준 통화 (미국 달러)
    target_currency = 'KRW'  # 대상 통화 (대한민국 원)
    api_key = '2571fc33672388bd6004a5d9'  # 여기에 자신의 API 키를 입력하세요.
    api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

    # API 요청
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # 응답 상태 코드가 200(OK)가 아닐 경우 예외 발생

        data = response.json()  # JSON 파싱
        rate = data['conversion_rates'][target_currency]
        date = data['time_last_update_utc']

        exchange_info = f"오늘의 환율 (기준: {base_currency} → 대상: {target_currency})\n1 {base_currency} = {rate} {target_currency}\n(기준일: {date})"
        messagebox.showinfo("환율 정보", exchange_info)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("에러", f"요청 중 오류 발생: {e}")
    except ValueError:
        messagebox.showerror("에러", "응답을 JSON으로 변환하는 데 실패했습니다.")
    except KeyError:
        messagebox.showerror("에러", "예상치 못한 응답 형식입니다. 환율 데이터를 찾을 수 없습니다.")

# GUI 설정
root = tk.Tk()
root.title("환율 정보 앱")

info_label = tk.Label(root, text="미국 달러(USD) → 대한민국 원(KRW) 환율 정보")
info_label.pack()

get_info_button = tk.Button(root, text="환율 정보 가져오기", command=get_exchange_rate)
get_info_button.pack()

root.mainloop()
