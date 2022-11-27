'''
반복문
    어떤 수행 작업을 한 번이 아니라 계속해서 수행해야 할 때 사용한다.

반복문 종류
    while, for문

while문
    특정 조건을 만족하는 동안 반복해서 수행하는 코드

while 조건식:
    반복실행코드
'''

# 주석 거는 법 command + /
n = 10
while n >= 1:
    print(n)
    n -= 1

def autoDoor(isPerson):
    time = 10
    while isPerson:
        print("문이 열립니다.")
        if time < 1:
            break
        time -= 1
    print("문이 닫힙니다.")

autoDoor(True)