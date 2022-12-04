'''
random - 난수 생성 모듈
'''
import random

# randint - 두 인수 사이 난수
print(random.randint(1, 10))  # 1 ~ 10

# randrange - range 함수 비슷
print(random.randrange(10))  # 0 ~ 9
print(random.randrange(1, 10))  # 1 ~ 9
print(random.randrange(1, 10, 2))  # 1 ~ 9 중 홀수만 , 1 +2씩 증감

# random 0이상 1미만 난수
print(random.random())

if random.random() < 0.5:
    print('안녕하세요')

# choice() 함수 - 리스트에서 랜덤
seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons))

# shuffle() 함수 - 임의로 섞는 함수
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)


# 예제 실습 - 주사위 게임 만들어 보기!

dice = random.randint(1, 6)
while True:
    user = int(input('주사위 값은 얼마일까요? >>> '))
    if dice == user:
        print('{}! 정답입니디다! 🥳'.format(dice))
        break
    else:
        print('오답입니다. 다시 시도하세요. 😢')