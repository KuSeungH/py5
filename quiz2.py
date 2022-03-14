# quiz02.py
# 함수 활용 문제 (2)

# 1) cm값을 전달 받아서, inch로 변환하여 문자열 형태로 반환하는 함수
# (1 inch = 2.54cm)

def cmtoInch(cm):
    inch = cm / 2.54
    return '{:.2f}inch'.format(inch)

print('3cm는 {}입니다'.format(cmtoInch(3)))
print('7.62cm는 {}입니다'.format(cmtoInch(7.62)))
print()


# 2) 전달받은 정수의 절대값을 반환하는 함수
# (abs 함수를 사용하지 않고 직접 만들기)

def adsoValue(num):
    #return (num > 0) and num or -num
    #return (num > 0) and num or num * -1
    # 전달받은 수가 0보다 크면 그대로, 아니면 부호반전해서 반환

    if num > 0:
        return num
    else:
        num = -num

    return -num

    # 함수에서 제어문을 활용하여 반환처리한다면
    # 모든경우 반환되도록 신경쓰기

print('-3의 절대값은 {}입니다'.format(adsoValue(-3)))
print('5의 절대값은 {}입니다'.format(adsoValue(5)))
print()

# 3) BMI 계산 함수 만들기 (키와 체중을 전달받아서 상태를 문자열형태로 반환)
# 체질량지수는 자신의 몸무게(Kg)을 키의 제곱(m)로 나눈 값입니다
# 18.5 미만 : 저체중
# 18.5 ~ 23미만 : 정상
# 23 ~ 25미만 : 과체중
# 25 이상 : 비만
# 체질량지수는 근육량을 반영하지 못하므로, 참고차료로만 활용하시면 됩니다

def getBMI(height, weight):
    result = '키 : {}cm, 체중 : {}kg, 상태 : {}, 수치 : {:.2f}'
    h = (height / 100) ** 2
    bmi = weight / h
    if      bmi < 18.5:                  state = '저체중'
    elif    18.5 <= bmi and bmi < 23:    state = '정상'
    elif    23 <= bmi and bmi < 25:      state = '과체중'
    elif    25 <= bmi and bmi:           state = '비만'

    result = result.format(height, weight, state, bmi)
    return result
result1 = getBMI(180, 75)
# 키 : 180cm, 체중 : 75kg, 상태 : 과체중, 수치 : 23.14

result2 = getBMI(170, 60)
# 키 : 170cm, 체중 : 60kg, 상태 : 정상, 수치 : 20.76

result3 = getBMI(165, 45)
# 키 : 165cm, 체중 : 45kg, 상태 : 저체중, 수치 : 16.52

print(result1)
print(result2)
print(result3)
print(getBMI(int(input('키 : ')), int(input('체중 : '))))