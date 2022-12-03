'''
for 문
    값의 범위나 횟수가 정해져 있을 때
    사용하면 편리한 반복문
    while문 보다 자주 사용된다.

for 변수 in 반복가능한객체:
    반복실행문
'''
pwd = input('비밀번호를 입력하세요 >>> ')
ch_count = 0
num_count = 0

for ch in pwd:
    # pwd = 문자열이다.
    # 반복가능한 객체 중 문자열, list, tuple 등 인덱싱이 되는 객체들은 인덱스번호가 하나씩 들어가면서 반복문이 실행된다.
    if ch.isalpha(): # ch가 알파벳인지
        ch_count += 1
    elif ch.isnumeric(): # ch가 숫자인지
        num_count += 1

if ch_count > 0 and num_count > 0: #and 연산자
    print('가능한 비밀번호 입니다.')
else:
    print('불가능한 비밀번호 입니다.')
