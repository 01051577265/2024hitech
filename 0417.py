"""while True:
    try:
        value = float(input("변환하고자 하는 값을 입력하세요: "))
        unit = input("변환하고자 하는 단위를 입력하세요:")

        if unit == 'C':
            fahrenheit =value * 9/5 +32
            print("{0:.2f}℉".format(fahrenheit))    
        elif unit == "F":
             celsius = (value - 32) * 5/9
             print("{0:.2f}℃".format(celsius))
        elif unit == "m":
             feet = value * 3.281
             print("{0:.2f}ft".format(feet))
        elif unit == "ft":
             meter = value / 3.281
             print("{0:.2f}m".format(meter))
        else:
             print("잘못된 입력입니다. 다시 시도해주세요.")
 
         # 다시 변환할 것인지 사용자에게 물어봄
        answer = input("다시 변환하시겠습니까? (Y/N)").upper()
        if answer == "N":
            break
    except ValueError:
     print("잘못된 입력입니다. 다시 시도해주세요.")"""



"""import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLineEdit, QLabel, QPushButton

class UnitConverter(QWidget):
     def __init__(self):
         super().__init__()
         self.initUI()

def initUI(self):
    # 단위변환 프로그램 제목
    self.setWindowTitle("Unit conveter")

    # 입력 필드
    self.value_input = QLineEdit(self)
    self.value_input.setGeometry(20,20,150,30)

    # 입력 단위 선택
    self.unit_from = QComboBox(self)
    self.unit_from.addItems(["celsius","Fahrenheit","Meter","Feet"])
    self.unit_from.setGeometry(180,20,100,30)

    # 출력 단위 선택
    self.unit_to = QComboBox(self)
    self.unit_to.addItems(["Fahrenheit","celsius","Feet","Meter"])
    self.unit_to.setGeometry(290,20,100,30)

    # 변환 버튼
    self.convert_button = QPushButton("Convert",self)
    self.convert_button.setGeometry(400,20,100,30)
    self.convert_button.clicked.connect(self.convert)

    # 결과 출력
    self.result_label = QLabel("",self)
    self.result_label.setGeometry(20,80,480,30)

    # 윈도우 크기 및 위치 설정
    self.setGeometry(300,300,520,150)
    self.show()

def convert(self):
        # 사용자로부터 입력값과 단위를 가져옴
        value = float(self.value_input.text())
        unit_from = self.unit_from.currentText()
        unit_to = self.unit_to.currentText()

        # 입력받은 단위에 따라 변환 수행
        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            result = value * 9/5 +32
        elif unit_from == "Fahrenheit" and unit_to == "Celsius":
            result = (value - 32) * 5/9
        elif unit_from == "Feet" and unit_to == "Meter":
            result = value * 3.281
        elif unit_from == "Meter" and unit_to == "Feet":
            result = value / 3.281
        else:
            result = "Invalid input"

        # 결과를 레이블에 출력
        self.result_label.setText("{:2f} {} = {:.2f} {}".format(value, unit_from, result, unit_to))

        if __name__ == '__main__':
            app = QApplication(sys.argv)
            Converter =UnitConverter()
            sys.exit(app.exec_())"""


"""import requests
from bs4 import BeautifulSoup

code = '005930'
url = f'https://finance.naver.com/item/main.nhn?code={code}'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
market_cap = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
print(market_cap.text)"""


"""import requests
from bs4 import BeautifulSoup

code = input("종목 번호를 입력하세요: ")
url = f'https://finance.naver.com/item/main.nhn?code={code}'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
price = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
print(f"현재 {code} 주가는 {price.text}입니다.")"""

"""import requests
from bs4 import BeautifulSoup
import tkinter as tk

def get_stock_price():
    code = code_entry.get()
    url = f'https://finance.naver.com/item/main.nhn?code={code}'
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    price = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    result_label.config(text=f"현재 {code} 주가는 {price.text}입니다.")

root = tk.Tk()
root.title("주식 가격 조회 프로그램")

label = tk.Label(root, text="종목 번호를 입력하세요:")
label.pack()

code_entry = tk.Entry(root)
code_entry.pack()

button = tk.Button(root, text="조회", command=get_stock_price)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()"""

"""from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("제목", "내용")

from datetime import datetime, timedelta
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

while True:
    now = datetime.now()
    if now.weekday() in [0, 2, 4] and now.hour == 9 and now.minute == 50:
     # 다음 회의 시작 시간 계산
     next_meeting_time = now + timedelta(minutes=10)
     next_meeting_time_str = next_meeting_time.strftime("%Y-%m-%d %H:%M:%S")
     
     # 알림 표시
     toaster.show_toast("알림", f"{next_meeting_time_str}에 회의가 시작됩니다.", duration=10)
     # 1초마다 반복
    time.sleep(1)"""

"""import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))
    return password

password = generate_password()

print("생성된 패스워드: ", password)"""

"""import random
import string
import sys
from typing import Self
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QVBoxLayout

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()  
         
         # 기본값 설정
        self.password_length = 12
        self.include_uppercase = True
        self.include_lowercase = True
        self.include_numbers = True
        self.include_special_characters = True  
        
        # UI 구성
        self.title_label = QLabel("패스워드 생성기")
        self.password_label = QLabel("생성된 패스워드: ")
        self.password_textbox = QLineEdit()
        self.length_label = QLabel("패스워드 길이: ")
        self.length_textbox = QLineEdit(str(self.password_length))
        self.uppercase_checkbox = QCheckBox("대문자 포함")
        self.uppercase_checkbox.setChecked(self.include_uppercase)
        self.lowercase_checkbox = QCheckBox("소문자 포함")
        self.lowercase_checkbox.setChecked(self.include_lowercase)
        self.numbers_checkbox = QCheckBox("숫자 포함")
        self.numbers_checkbox.setChecked(self.include_numbers)
        self.special_checkbox = QCheckBox("특수문자 포함")
        self.special_checkbox.setChecked(self.include_special_characters)
        self.generate_button = QPushButton("패스워드 생성")
        
        # UI 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_textbox)
        vbox.addWidget(self.length_label)
        vbox.addWidget(self.length_textbox)
        vbox.addWidget(self.uppercase_checkbox)
        vbox.addWidget(self.lowercase_checkbox)
        vbox.addWidget(self.numbers_checkbox)
        vbox.addWidget(self.special_checkbox)
        vbox.addWidget(self.generate_button)
        self.setLayout(vbox)
        
        # 이벤트 처리 함수 등록
        self.generate_button.clicked.connect(self.generate_password)
        self.length_textbox.textChanged.connect(self.update_length)
        self.uppercase_checkbox.stateChanged.connect(self.update_uppercase)
        self.lowercase_checkbox.stateChanged.connect(self.update_lowercase)
        self.numbers_checkbox.stateChanged.connect(self.update_numbers)
        self.special_checkbox.stateChanged.connect(self.update_special)
        
        # 초기 패스워드 생성
        self.generate_password()

        # 윈도우 설정
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("패스워드 생성기")
        self.show()

    def generate_password(self):
         # 사용자 설정에 따른 패스워드 생성
        characters = ''
        if self.include_uppercase:
            characters += string.ascii_uppercase
        if self.include_lowercase:
            characters += string.ascii_lowercase
        if self.include_numbers:
             characters += string.digits
        if self.include_special_characters:
             characters += string.punctuation
        password = ''.join(random.choice(characters) for i in range(self.password_length))
        self.password_textbox.setText(password)
    
    def update_length(self, text):
        # 패스워드 길이 변경
        try:
            self.password_length = int(text)
            self.generate_password()
        except ValueError:
         pass
    def update_uppercase(self, state):
        # 대문자 포함 여부 변경
        self.include_uppercase = bool(state)
        self.generate_password()
    
    def update_lowercase(self, state):
        # 소문자 포함 여부 변경
        self.include_lowercase = bool(state)
        self.generate_password()
   
    def update_numbers(self, state):
        # 숫자 포함 여부 변경
        self.include_numbers = bool(state)
        self.generate_password()
    
    def update_special(self, state):
        # 특수문자 포함 여부 변경
        self.include_special_characters = bool(state)
        self.generate_password()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    sys.exit(app.exec_())"""

"""import random
import time

sayings = [
    "노력하는 것만이 성공으로 이끄는 길이다. - 니키 라우드",
    "삶이 있는 한 희망은 있다. - 키케로",
    "오늘을 낭비하지 마라. 어제의 후회와 내일의 불안에 가로막혀 오늘을 놓치고 있다. - 에머슨",
    "문제점을 찾지 말고 해결책을 찾으라. - 헨리포드",
    "사람은 자신이 믿는 대로 된다. - 괴테",
    "지식은 인생을 바꾼다. - 윌리엄 제임스",
    "지금까지 당신이 살아온 모든 날들의 합이 오늘이라면, 오늘하루를 잘 살아야 합니다. - 괴테",
    "한번의 실패와 영원한 실패를 혼동하지 마라. - F.스콧 핏제랄드",
    "당신이 할 수 있다고 믿든 할 수 없다고 믿든 믿는 대로 될 것이다. - 헨리 포드",
    "성공한 사람을 보면 마치 그들이 실패한 적이 없는 것처럼 보이지만, 많은 실패들을 겪고 다시 일어난 것이다. - 왈트 디즈니",
]
# 무작위로 명언 선택하여 출력
saying = random.choice(sayings)
print(saying)

# 10초 뒤에 자동으로 프로그램 종료
time.sleep(10)"""


"""import random
import time
from win10toast import ToastNotifier

# 윈도우 토스트 알림 객체 생성
toaster = ToastNotifier()

# 명언 리스트 생성
sayings = [
    "노력하는 것만이 성공으로 이끄는 길이다. - 니키 라우드",
    "삶이 있는 한 희망은 있다. - 키케로",
    "오늘을 낭비하지 마라. 어제의 후회와 내일의 불안에 가로막혀 오늘을 놓치고 있다. - 에머슨",
    "문제점을 찾지 말고 해결책을 찾으라. - 헨리포드",
    "사람은 자신이 믿는 대로 된다. - 괴테",
    "지식은 인생을 바꾼다. - 윌리엄 제임스",
    "지금까지 당신이 살아온 모든 날들의 합이 오늘이라면, 오늘하루를 잘 살아야 합니다. - 괴테",
    "한번의 실패와 영원한 실패를 혼동하지 마라. - F.스콧 핏제랄드",
    "당신이 할 수 있다고 믿든 할 수 없다고 믿든 믿는 대로 될 것이다. - 헨리 포드",
    "성공한 사람을 보면 마치 그들이 실패한 적이 없는 것처럼 보이지만, 많은 실패들을 겪고 다시 일어난 것이다. - 왈트 디즈니",
]

while True:
    # 무작위로 명언 선택
    saying = random.choice(sayings)
    
    # 윈도우 토스트 알림으로 명언 보여주기
    toaster.show_toast(
        "명언 알림",
        saying,
        duration=10,
        threaded=True
     )  
    
    # 1시간 대기
    time.sleep(60 * 60)"""


"""import vlc

player = vlc.Instance('--no-xlib')

url = 'http://www.moneywars.co.kr/?mid=mt_board43&document_srl=10618'

media_player = player.media_player_new()

media = player.media_new(url)

media_player.set_media(media)

media_player.play()

while True:
    pass"""

# import tkinter as tk
# import vlc

# radios = {
#     "강릉MBC mms://118.46.233.19/ams (32k)"
#     "원주MBC mms://live.wjmbc.co.kr/fm2 (48k)"
#     "충주MBC mms://VODSTR.cjmbc.co.kr/STFM (32k)"
#     "삼척MBC mms://121.189.151.7/sfm (128k)"
#     "포항MBC mms://cast.phmbc.co.kr/AMLive (48k)"
#     "마산MBC mms://210.114.220.120/masanmbcam (20k)"
# }
# class RadioPlayer:
#     def __init__(self, master):
#         self.master = master
#         master.title('라디오')   
#         master.geometry('200x100')
#         # 라디오 선택 메뉴 생성
#         self.radio_var = tk.StringVar(master)
#         self.radio_var.set(list(radios.keys())[0])  
#         self.radio_menu = tk.OptionMenu(master, self.radio_var, *radios.keys())
#         self.radio_menu.pack()

#          # 재생/일시정지/중지 버튼 생성
#         self.play_button = tk.Button(master, text='재생', command=self.play_radio)
#         self.pause_button = tk.Button(master, text='일시정지', command=self.pause_radio)
#         self.stop_button = tk.Button(master, text='중지', command=self.stop_radio)
#         self.play_button.pack(side=tk.LEFT, padx=10)
#         self.pause_button.pack(side=tk.LEFT, padx=10)
#         self.stop_button.pack(side=tk.LEFT, padx=10)
#         # 미디어 재생을 위한 인스턴스 생성
#         self.instance = vlc.Instance('--no-xlib')

#          # 미디어 플레이어 생성
#         self.media_player = self.instance.media_player_new()

#         # 초기 상태
#         self.is_playing = False
 
#     def play_radio(self):
#          """선택한 라디오 방송을 재생합니다."""
#          radio_url = radios[self.radio_var.get()]
#          media = self.instance.media_new(radio_url)
#          self.media_player.set_media(media)
#          self.media_player.play()
#          self.is_playing = True

#     def pause_radio(self):
#          """현재 재생 중인 라디오 방송을 일시정지합니다."""
#          if self.is_playing:
#             self.media_player.pause()
#             self.is_playing = False
 
#     def stop_radio(self):
#          """현재 재생 중인 라디오 방송을 중지합니다."""
#          if self.is_playing:
#             self.media_player.stop()
#             self.is_playing = False
# root = tk.Tk()
# radio_player = RadioPlayer(root)
# root.mainloop()

"""print("MBTI 성격유형검사")
print("각 문항에 대해 가장 적절한 답변을 선택해주세요.")
print("1: 전혀 그렇지 않다 / 2: 그렇지 않은 편이다 / 3: 보통이다 / 4: 그렇다 / 5: 매우 그렇다")
questions = [
    "1. 대체로 사람들과 어울리는 것을 좋아한다.",
    "2. 논쟁보다는 타협하는 것이 좋다고 생각한다.",
    "3. 대개 계획을 세우는 것을 좋아한다.",
    "4. 새로운 일에 도전하는 것을 좋아한다.",
    "5. 감정을 드러내는 것보다는 이성적으로 생각하는 것이 좋다고 생각한다.",
    "6. 대체로 조용한 분위기를 좋아한다.",
    "7. 사람들과의 대화에서 자주 말하는 편이다.",
    "8. 어떤 일을 할 때 체계적으로 처리하는 편이다.",
    "9. 강한 경쟁심이 있다.",
    "10. 주로 자신의 감정에 따라 일을 처리한다."
]
results = {
    "ISTJ": [1, 2, 3, 8, 10],
    "ISFJ": [1, 2, 3, 6, 10],
    "INFJ": [2, 3, 5, 6, 10],
    "INTJ": [3, 4, 5, 8, 10],
    "ISTP": [4, 6, 7, 9, 10],
     "ISFP": [4, 6, 7, 10],
    "INFP": [2, 5, 6, 10],
    "INTP": [3, 5, 6, 8, 10],
    "ESTP": [4, 6, 7, 9],
    "ESFP": [4, 6, 7],
    "ENFP": [2, 5, 6],
    "ENTP": [3, 5, 6, 9],
    "ESTJ": [1, 2, 3, 8, 9],
    "ESFJ": [1, 2, 3, 6, 9],
    "ENFJ": [2, 3, 5, 6, 9],
    "ENTJ": [3, 4, 5, 8, 9]
}

results_count = {result: 0 for result in results}

for i, question in enumerate(questions):
    print(question)
    while True:
        try:
            answer = int(input("답변을 입력해주세요: "))
            if answer < 1 or answer > 5:    
                print("1에서 5 사이의 값을 입력해주세요.")
                continue
            break
        except ValueError:  
            print("숫자를 입력해주세요.")
for result, result_answers in results.items():
    if i+1 in result_answers:
        results_count[result] += answer

max_result = max(results_count, key=results_count.get)
print(f"당신의 MBTI 성격유형은 {max_result}입니다.")"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    questions = [
        "1. 대체로 사람들과 어울리는 것을 좋아한다.",
        "2. 논쟁보다는 타협하는 것이 좋다고 생각한다.",
        "3. 대개 계획을 세우는 것을 좋아한다.",
        "4. 새로운 일에 도전하는 것을 좋아한다.",
        "5. 감정을 드러내는 것보다는 이성적으로 생각하는 것이 좋다고 생각한다.",
        "6. 대체로 조용한 분위기를 좋아한다.",
        "7. 사람들과의 대화에서 자주 말하는 편이다.",
        "8. 어떤 일을 할 때 체계적으로 처리하는 편이다.",
        "9. 강한 경쟁심이 있다.",
        "10. 주로 자신의 감정에 따라 일을 처리한다."
    ]
    return render_template('index.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    questions = [
        "1. 대체로 사람들과 어울리는 것을 좋아한다.",
        "2. 논쟁보다는 타협하는 것이 좋다고 생각한다.",
        "3. 대개 계획을 세우는 것을 좋아한다.",
        "4. 새로운 일에 도전하는 것을 좋아한다.",
        "5. 감정을 드러내는 것보다는 이성적으로 생각하는 것이 좋다고 생각한다.",
        "6. 대체로 조용한 분위기를 좋아한다.",
        "7. 사람들과의 대화에서 자주 말하는 편이다.",
        "8. 어떤 일을 할 때 체계적으로 처리하는 편이다.",
        "9. 강한 경쟁심이 있다.",
        "10. 주로 자신의 감정에 따라 일을 처리한다."
    ]
    results = {
        "ISTJ": [1, 2, 3, 8, 10],
        "ISFJ": [1, 2, 3, 6, 10],
        "INFJ": [2, 3, 5, 6, 10],
        "INTJ": [3, 4, 5, 8, 10],
        "ISTP": [4, 6, 7, 9, 10],
        "ISFP": [4, 6, 7, 10],
        "INFP": [2, 5, 6, 10],
        "INTP": [3, 5, 6, 8, 10],
        "ESTP": [4, 6, 7, 9],
        "ESFP": [1, 4, 6, 7, 10],
        "ENFP": [1, 2, 5, 6, 10],
        "ENTP": [3, 5, 7, 8, 10],
        "ESTJ": [1, 3, 8, 9, 10],
        "ESFJ": [1, 2, 6, 7, 10],
        "ENFJ": [2, 3, 5, 6, 7],
        "ENTJ": [3, 4, 5, 8, 9]
    }
    
    scores = { "E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0 }

    for i in range(1, 11):
        answer = int(request.form['q' + str(i)])
        for k, v in results.items():
            if i in v:
                if answer <= 3:
                    scores[k[0]] += 1
                else:
                    scores[k[1]] += 1
    
    result = ""
    if scores['E'] > scores['I']:
        result += "E"
    else:
        result += "I"
    if scores['S'] > scores['N']:
        result += "S"
    else:
        result += "N"
    if scores['T'] > scores['F']:
        result += "T"
    else:
        result += "F"
    if scores['J'] > scores['P']:
        result += "J"
    else:
        result += "P"
  
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()



















