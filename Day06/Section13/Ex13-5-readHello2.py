'''
file 객체 read() -> 전체 읽어오기
        read(인자값) -> 인자값만큼 불러오기
'''
file = open('hello.txt', 'rt', encoding='UTF-8')
while True:
    str = file.read(5)
    if not str: # 읽을 값이 없으면 True
        break
    print(str, end='')
file.close()