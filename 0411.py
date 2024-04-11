# # 살충제 오염이 심한 먹거리
# #dirty_dozen = ["딸기","시금치","콜라드","케일",복숭아","배","천도복숭아","사과","포도","피망","체리","블루베리","강낭콩"]
# #리스트 안에 리스트 > 중첩리스트
# fruits = ["딸기","복숭아","배","천도복숭아","사과","포도","체리","블루베리"]
# vegetables = ["시금치","콜라드","피망","강낭콩","케일"]
# # 과일+야채 리스트를 포함한 리스트 생성
# dirty_dozen = [fruits, vegetables]
# #리스트를 출력
# print(dirty_dozen)


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

# import random

# rock = '''
#      _______
# ---'    ____)
#        (_____)
#        (_____)
#        (____)
# ---.__ (___)
# '''
# paper = '''
#     _______
# ---'   ____)____
#            ______)
#            _______)
#           _______)
# ---.__________)
# '''
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#      (____)
# ---.__(___)
# '''
# #가위바위보 게임
# img_hands =[rock, paper, scissors]

# my_gyem = int(input("무엇을 내겠습니까? 바위(0),보(1),가위(2)"))
# if my_gyem >=3 or my_gyem < 0:
#     print("잘못된 숫자를 입력했습니다")
# else:
#     print(f"나의 선택은: ")
#     print(img_hands[my_gyem])

#     computer_gyem = random.randint(0, 2)
#     print(f"컴퓨터의 선택은: ")
#     print(img_hands[computer_gyem])

#     if computer_gyem == 0 and my_gyem == 2:
#         print("컴퓨터가 이겼다")
#     elif my_gyem == 0 and computer_gyem == 2:
#         print("내가 이겼다!")
#     elif computer_gyem > my_gyem: 
#         print("컴퓨터가 이겼다")
#     elif my_gyem == computer_gyem:
#          print("비겼다!")
#     elif my_gyem > computer_gyem:
#      print("내가 이겼다!")

# import random

# # 1부터 100까지 무작위 숫자 생성
# number = random.randint(1, 100)
# # 몇 회 시도했는지를 저장하는 변수
# num_of_guesses = 0
# # 무한 반복문
# while True:
#     # 사용자로부터 숫자 입력 받기
#     guess = int(input("1부터 100까지의 숫자를 입력하세요: "))
 
#     # 시도 횟수 증가
#     num_of_guesses += 1
 
#     # 추측한 숫자가 정답보다 큰 경우
#     if guess > number:
#         print("입력한 숫자가 너무 큽니다.")
 
#     # 추측한 숫자가 정답보다 작은 경우
#     elif guess < number:
#         print("입력한 숫자가 너무 작습니다.")
 
#      # 추측한 숫자가 정답인 경우
#     else:
#          print(f"축하합니다! {num_of_guesses}회 만에 숫자를 맞췄습니다.")
#          break

# import socket

# #호스트 이름 가져오기
# hostname = socket.gethostname()

# # IP 주소 가져오기
# ip_address = socket.gethostbyname(hostname)

# print("내부 IP: " + ip_address)

# import pyttsx3

# #한글 TTS 엔진을 설정합니다.
# engine = pyttsx3.init()
# engine.setProperty('rate',150)

# #텍스트를 읽어주는 함수를 정의합니다.
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# #텍스트를 입력받아 TTS로 변환합니다.
# text = "안녕하세요 챗GPT로 만드는 파이썬 작품들 입니다."
# speak(text)

# from gtts import gTTS
# from playsound import playsound

# # 텍스트를 입력받습니다.
# text = input('텍스트를 입력하세요: ')

# # 한국어로 음성을 출력하도록 설정합니다.
# tts = gTTS(text, lang='ko')

# # 음성을 mp3 파일로 저장합니다.
# tts.save('output.mp3')

# # 저장한 mp3 파일을 재생합니다.
# playsound('output.mp3')

# import qrcode

# # QR 코드에 넣을 데이터
# data = "Hello, World!"

# # QR 코드 생성
# img = qrcode.make(data)

# # 이미지 파일로 저장
# img.save("qrcode.png")

# import qrcode
# import os
# # QR 코드에 넣을 데이터
# data = "Hello, World!"

# # QR 코드 생성
# img = qrcode.make(data)

# # 이미지 파일로 저장
# file_path = os.path.join("qrcode.png")
# img.save(file_path)

# import qrcode
# import os

# # 데이터가 저장된 파일 경로
# file_path = os.path.join("폴더명","qrdata.txt")

# # QR 코드 생성 함수
# def create_qrcode(data):
#     # QR 코드 생성
#     img = qrcode.make(data)
    
#     # 이미지 파일로 저장
#     img_file_path = os.path.join("폴더명",f"qrcode_{data}.png")
#     img.save(img_file_path)

# # qrdata.txt 파일에서 데이터 읽어오기
# with open(file_path, 'r') as f:
#     for line in f:
#         # 개행 문자 제거
#         data = line.strip()
#         create_qrcode(data)


# import psutil # psutil 모듈을 사용하기 위해 import 합니다.
# import time  # time 모듈을 사용하기 위해 import 합니다.
# # 무한루프를 돌며 CPU, RAM, 네트워크 사용량을 출력합니다.
# while True:
#     # CPU 사용량을 구하고 출력합니다.
#      cpu_percent = psutil.cpu_percent(interval=None)
#      print(f"CPU 사용량: {cpu_percent}%")
     
#      # 메모리 사용량을 구하고 출력합니다.
#      mem = psutil.virtual_memory()
#      mem_percent = mem.percent
#      print(f"메모리 사용량: {mem_percent}%")
#      # 네트워크 사용량을 구하고 출력합니다.
#      net_io_counters = psutil.net_io_counters()
#      bytes_sent = net_io_counters.bytes_sent
#      bytes_recv = net_io_counters.bytes_recv
#      print(f"네트워크 사용량: 송신={bytes_sent}bytes, 수신={bytes_recv}bytes")
 
#      # 1초 대기합니다.
#      time.sleep(1)

# import psutil
# import tkinter as tk

# # 윈도우를 생성합니다.
# window = tk.Tk()
# window.title("시스템 모니터")

# # CPU 사용량을 표시할 라벨을 생성합니다.
# cpu_label = tk.Label(window, text="CPU 사용량: ")
# cpu_label.pack()

# # RAM 사용량을 표시할 라벨을 생성합니다.
# ram_label = tk.Label(window, text="RAM 사용량: ")
# ram_label.pack()

# # 무한루프를 돌며 CPU, RAM 사용량을 업데이트합니다.
# def update_usage():
#     # CPU 사용량을 구하고 라벨에 업데이트합니다.
#     cpu_percent = psutil.cpu_percent(interval=None)
#     cpu_label.config(text=f"CPU 사용량: {cpu_percent}%")    
     
#     # RAM 사용량을 구하고 라벨에 업데이트합니다.
#     mem = psutil.virtual_memory()
#     mem_percent = mem.percent
#     ram_label.config(text=f"RAM 사용량: {mem_percent}%")
    
#     # 1초 대기합니다.
#     window.after(1000, update_usage)

# # 무한루프를 돌며 GUI를 업데이트합니다.
# update_usage()

# # 윈도우를 실행합니다.
# window.mainloop()

# import itertools
# import zipfile

# def crack_zip_password(zipfilename, digits=True, letters=True, max_length=9):
    
#     chars = ""
#     if digits:
#         chars += "0123456789"
#     if letters:
#         chars += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     passwords = itertools.chain.from_iterable(
#          itertools.product(chars, repeat=i) for i in range(1, max_length + 1))
    
#     # 비밀번호를 하나씩 시도합니다.
#     with zipfile.ZipFile(zipfilename) as zf:
#         for password in passwords:
#             password = "".join(password)
#             print(password)
#         try:
#             zf.extractall(pwd=password.encode())
#             return password
#         except:
#              pass
#     # 비밀번호를 찾지 못한 경우 None을 반환합니다.
#     return None
# password = crack_zip_password(r"암호.zip", digits=True, letters=True, max_length=9)
# print("비밀번호는:",password)

# import requests

# def currency_converter(amount, from_currency, to_currency):
#     # API 호출 URL
#     url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
 
#     # API 호출 및 응답 받기
#     response = requests.get(url)
#     data = response.json()

#     # 환율 계산
#     exchange_rate = data['rates'][to_currency]
#     result = round(amount * exchange_rate, 2)

#     # 결과 반환
#     return result
# print("환율 변환기")
# print("============")

# while True:
#     try:
#         # 변환하려는 금액 입력
#         amount = float(input("변환하려는 금액을 입력하세요: "))
 
#         # 변환하려는 화폐 입력
#         from_currency = input("어떤 화폐에서 변환하시겠습니까? (예: USD, KRW): ").upper()
#         to_currency = input("어떤 화폐로 변환하시겠습니까? (예: USD, KRW): ").upper()
 
#         # 환율 계산
#         result = currency_converter(amount, from_currency, to_currency)
 
#         # 결과 출력
#         print(f"{amount} {from_currency}은(는) {result} {to_currency}입니다.")
 
#         # 계속 변환할지 묻기
#         choice = input("계속 변환하시겠습니까? (Y/N): ").upper()
#         if choice != "Y":
#             break
     
#     except:
#         print("올바른 값을 입력해주세요.")


# import zipfile
# def compress_file(file_path):
#     with zipfile.ZipFile(file_path + '.zip', 'w') as zip_file:
#      zip_file.write(file_path)
# if __name__ == '__main__':
#     compress_file('압축.txt')

# import pyzipper

# def compress_file_with_password(file_path, password):
#     # read the file contents
#     with open(file_path, 'rb') as f:
#          data = f.read()
#     # create a new zip file with the given name
#     with pyzipper.AESZipFile(file_path + '.zip', 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_file:
#         # set password for the zip file
#         zip_file.setpassword(password.encode('utf-8'))
#         # write the file to the zip file
#         zip_file.writestr(file_path, data)
# if __name__ == '__main__':
#     # specify the file path and password
#     compress_file_with_password('압축.txt.zip', '1234')

# from googletrans import Translator

# # 번역할 파일 경로
# input_file_path = "영어문서.txt"
# # 번역된 파일 저장 경로
# output_file_path = "한글번역.txt"

# # 번역기 생성
# translator = Translator()

# # 파일 읽기
# with open(input_file_path, "r", encoding="utf-8") as input_file:
#      text = input_file.read()

# # 번역
# result = translator.translate(text, dest="ko")

# # 번역된 결과를 파일에 쓰기
# with open(output_file_path, "w", encoding="utf-8") as output_file:
#      output_file.write(result.text) 





