'''
for 문과 range 함수

range()
    연속된 숫자를 만들어주는 함수
'''

'''
range(stop)
0 <= n < stop
'''
# 0~9 range
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(10):
    print('{} x {} = {}'.format(dan, n, dan * n), end='')
print()

'''
range(start, stop)
'''
# 1~9 range
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10):
    print('{} x {} = {}'.format(dan, n, dan * n), end='')
print()

'''
range(start, stop, step)
start <= n < stop 사이에서 step만큼 증가하면서 출력
'''
# 1부터 2씩 증가 < 10

dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10, 2):
    print('{} x {} = {}'.format(dan, n, dan * n), end='')
print()