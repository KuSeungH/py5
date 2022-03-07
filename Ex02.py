# ex02.py
# 수학의 함수(function)와 비교

# y = f(x)
# f라는 어떤 식이 있고, x에 값을 넣으면 서로 다른 y값이 구해진다

# y = 2x + 3
# x = 1, y = 5
# x = 2, y = 7
# x = 3, y = 9 
# ...

# x  : 매개변수, 함수를 호출하면서 전달하느 데이터 (입력값)
# y  : 반환값, 함수를 호출했을때 돌아오는 데이터 (출력값)
# f : 함수이름을 지정하여 일정한 코드를 묶어서 관리

def sampleFunction(x):
    y = 2 * x + 3
    return y 
    # return : 함수를 종료하면서, 값을 함수 호출자리로 되돌려준다

result = sampleFunction(1)  # 함수 반환값을 변수에 저장
print(result)               # 지정된 반환값을 출력

print(sampleFunction(2))    # 함수 호출 - 반환 - 출력

def pythagoras(base, height):
    # a^2 + b^2 = c^2
    diagonal = (base ** 2 + height ** 2) ** 0.5
    result = '밑변이 {}cm이고, 높이가 {}cm인 직각삼각형'
    result += '빗변의 길이는 {:.2f}cm입니다'
    result = result.format(base, height, diagonal)
    return result

# 3^2 + 4^2 = 5^
result1 = pythagoras(3, 4)
print(result1)

result2 = pythagoras(5, 12)
print(result2)