# quiz.01
# 함수를 활용한 기본 문제

# 1) 정수를 전달받아서 양수 혹은 음수를 판별하여 문자열로 변환하는 함수
def quiz1(num):
    sign = ''
    if num > 0:
        sign = '양수'
    else:
        sign = '음수'
    return sign


print(quiz1(3))     # 양수
print(quiz1(-5))    # 음수
print()

# 2) 츨생연도를 2자리로 전달받아서, 나이를 정수로 반환하는 함수
def quiz2(birthYear):
    currentYear = 22
    if currentYear < birthYear:
        birthYear += 1900
    else:
        birthYear += 2000
    age = 2000 + currentYear - birthYear + 1
    return age

print(quiz2(93))    # 30
print(quiz2(99))    # 24
print(quiz2(4))
print()

# 3) 1부터 전달받은 숫자까지의 합계를 반환하는 함수
def quiz3(num):
    total = 0
    for i in range(1, num+1):
        total += i
    return total
    
print(quiz3(10))    # 55
print(quiz3(100))   # 5050
print()