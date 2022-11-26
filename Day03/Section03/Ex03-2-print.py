'''
print() 함수 사용법
    sep : 출력할 value의 구분 문자
    end : value 출력 후 출력할 문자 (기본값 '\n')
    file : 출력 방향 지정 
'''
print("재미있는", "파이썬")
print("Python", "Java", "C", sep=",")

print("안녕", end="") # 디폴트 값은 end="\n", 줄바꿈을 지워줘서 7-8행은 이어서 출력
print("하세요")

fos = open("sample.py", mode="wt")
print('print("Hello World")', file=fos)
fos.close()