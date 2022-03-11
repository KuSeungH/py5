# ex06.py
# 가변인자 활용 함수

def showMenbers(day, * member):
    text = '{}일 참여하는 멤버의 목록은 아래와 같습니다'.format(day)
    print(text)

    for m in member:
        print('- {}'.format(m))

    print('이상 {}명 끝'.format(len(member)))
    print()

showMenbers(22, '원종래', '이지은', '홍진호', '나단비')
showMenbers(23, '임요한', '홍지호')
