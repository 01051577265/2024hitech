"""print(len("hello"))
print(len("12345"))
print("hello"[10])
print("123"+"456")
"""

"""num_char = len(input("당신의 이름은 무엇입니까?"))
print(type(num_char))
"""

"""new_num_char = str(num_char)
Print("당신의 이름은" + new_num_char + "characters.")
"""
"""a = input("숫자:")
new_a = int(a[0])
new_a1 = int(a[1])
print(new_a + new_a1)
"""

"""height = input("당신의 키는 몇 m : ")
weight = input("당신의 몸무게는 몇 kg :")

bmi = int(weight) / float(height)**2

bmi_as_int = int(bmi)
print(bmi_as_int)
"""

"""print(round(0.145676747234, 2))
"""

"""#여러분이 90살까지 산다면 실제로 몇일, 몇주, 몇달이 남았을까요?
#1년은 365일, 52주, 12개월

age = input("당신의 나이는 몇살일까요?")


# 형변환 필요함
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
week_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(months_remaining)

#f-string :(f"{  }") 서로 다른 데이터 유형을 문자열로 처리할 수 있는것

message = f"당신의남은{days_remaining} 날, {week_remaining} 주, {months_remaining} 월"

print(message)
"""

"""# -- 팁계산기 --
# 총 얼마를 주문했을까?
# 팁은 몇%
# 팁을 포함해서 총 얼마를 내야할까?
# 몇명이 지불 해야될까?
# 1인당 지불 금액은?

print("팁 계산기!")

order = float(input("총 얼마를 주문했을까?"))
tip =int(input("팁을 얼마나 주면 좋을까? 10,12, or, 15 ?"))
people = int(input("몇명이서 나눠서 낼까?"))

tip_as_percent = tip / 100
total_tip = order * tip_as_percent
total_bill = total_tip +order
bill_per_person = total_bill / people
#소수점 둘째까지만
final_bill = round(bill_per_person, 2)
print(f"팁 포함해서 각자 내야되는 금액은 :{final_bill} $ ")"""

"""#롤러코스터 매표기
#롤러코스터는 120cm 이상 되어야 탈 수 있다.

print("롤러코스터를 타러 오셧군요!")
height = int(input("키가 몇 cm 입니까?"))

if height >= 120:
    print("롤러코스터를 탈 수 있습니다!")
else:
    print("죄송하지만 롤러코스터를 탈 수 없어요.")"""

"""print("롤러코스터를 타러 오셨군요!")
height = int(input("키카 몇 cm 입니까?"))

if height >= 120:
    print("롤러코스터를 탈 수 있습니다!")
    age = int(input("당신은 몇살입니까?"))
    if age <=18:
        Print("7천원입니다")
    else:
        print("만2천원입니다")

else:
    print("죄송하지만 롤러코스터를 탈 수 없어요.")
"""

"""print("롤러코스터를 타러 오셨군요!")
height = int(input("키카 몇 cm 입니까?"))

if height >= 120:
    print("롤러코스터를 탈 수 있습니다!")
    age = int(input("당신은 몇살입니까?"))
    if age < 12:
        print("무료입니다!")
    if age <=18:
        print("7천원입니다")
    else:
        print("만2천원입니다")
else:    
    print("죄송하지만 롤러코스터를 탈 수 없어요.")"""

