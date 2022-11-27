'''
enumerate() 함수
    List, Tuple, String 등 자료형을 입력받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려준다.
'''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(type(enumerate(months))) # 인덱스 번호과 값을 같이 준다.
for month, day in enumerate(months):
    print('{}월은 {}일까지 있다.'.format(month+1, day))
