'''
r (read mode) : 읽기 전용 모드 / 파일이 없으면 에러

절대경로 예) C:/hello.txt
상대경로 예) ../hello.txt (상위 디렉터리 기준, 상대적인 경로)
      .. -> 상위폴더
      . -> 현재폴더
'''

file = open('hello.txt', 'rt', encoding='UTF-8')
str=file.read()
print(str, end='')
file.close()

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    str = file.read()
    print(str, end='')