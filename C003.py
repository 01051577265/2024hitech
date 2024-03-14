#3-1) 파이썬 띄어쓰기
"""
print("hello world")
print("hello  world")
print("hello"+"world")
print("Hello" + " " + "world")
"""

#3-2) 디버깅 연습하기
"""
print("오늘은 파이썬 챌린지 3일차 입니다)
print('디버깅 "+" 연습중입니다')
 print('내일은("금요일" + "입니다)')
print(("그래서 챌린지가 없습니다"))
"""

# 3-2) 다시
"""
print("오늘은 파이썬 챌린지 3일차 입니다")
print('디버깅 연습중입니다')
print("내일은 금요일입니다")
print("그래서 챌린지가 없습니다")
"""

#3-3 입력함수1
#input("당신의 이름은 무엇입니까?")

# 입력 + 출력 해봅시다.
"""
print("나는" + input("당신의 이름은 무엇입니까?") + "입니다")
"""

#3-4) 입력함수2
#문자열의 길이를 계산하려면? len(s)를 사용한다. 
#print(len(input("당신의 이름은 무엇입니까?")))

#3-5) 파이썬 변수1
#name 이라는 변수에 입력값을 할당해보자
"""
name = input("당신의 이름은 무엇입니까?")
print(name)
"""

#이름을 입력받아서 이름의 길이를 출력해보자
"""
name = input("당신의 이름은 무엇입니까?")
length = len(name)
print(length)
"""

#3-6) 파이썬 변수2

a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)