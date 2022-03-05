# ex01.py
# 함수

print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('Hello')
print()

for i in range(5): 
    print('Hello')
print()

print('Hello 2022')
print('Hello January')
print('Hello 22')
print('Hello saturday')
print('Hello ITBANK')
print()

# 내가 이후 코드에서 사용할 함수를 정의(define)한다
# 함수를 정의할 때는 제어문 사용때와 마찬가지로 들여쓰기에 신경쓰도록 한다
def printHello(word):
    print('Hello', end=' ')     # 공통된 출력문
    print(word)                 # 실행될때 마다 다른 내용을 뒤에 출력

printHello(2022)                # 지정한 이름으로 만들어진 함수를 부른다 (호출, call)
printHello('January')           # 함수가 호출되면 정의된 내용에 따라 코드를 진행
printHello(22)
printHello('saturday')
printHello('ITBANK')
print()

# 이름과 나이를 전달받아서, 성인/미성년자 여부를 같이 출력하는 함수
# 공식을 미리 만들어두고, x값을 이후에 전달하여 코드를 실행한다

def showInfo(name, age):
    aduit = age >= 20 and '성인' or '미성년자'
    form = '{}님은 {}살이고, {}입니다'
    form = form.format(name, age, aduit)
    print(form)
    print()

showInfo('이지은', 30)
showInfo('나단비', 7)
showInfo('홍진호', 40)

