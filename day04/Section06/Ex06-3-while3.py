
my_list = []
n = 1 # 단순 초기 입력값

while n != 0:
    n = int(input('정수를 입력하세요(종료는 0입니다) >>> '))
    my_list.append(n)
my_list.pop() # 0을 빼기 위해서
print(my_list)

'''
while2 예제와 같은 결과지만 코드가 다름.
while문은 리소스를 많이 잡아 먹기 때문에 최대한 짧게 쓰는게 좋다.
최적화된 코드 중요 but, 초기에는... 실행되는 코드가 우선...🥲
'''

