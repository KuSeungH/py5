# exo5.py
# 파이썬 함수의 가변인자
# 가변인자는 인자의 개수 

# 인자(값) : 함수를 호출하면서 전달하는 값
# 매개변수 : 인자를 받아서 저장하는 변수

# 함수를 호출할때 전달하는 값의 개수가 정해져있지 않다

def test1(*args):
    print(args)
    print(type(args))

    for i in range(len(args)):
        print('{}번째 요소는 {}'.format(i, args[i]))

test1(1)
test1(1,2,3)
test1('Hello', 'world')
test1('today', 'is', 'january', 22, 'th', 'sat')

# tuple : 리스트와 유사한 여러 값을 묶어서 처리하는 형태

li = [1,2,3,4]
tu = (1,2,3,4)

li.append(5)        # 튜플은 요소를 추가할 수 없다
# tu.append[0]
del li[0]
#del tu[0]          # 튜플은 요소를 삭제할 수 없다

print('li : ', end='')
for i in li:
    print(i, end='')
print()

print('tu :', end='')
for i in tu:
    print(tu, end='')
print()