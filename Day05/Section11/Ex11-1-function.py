'''
함수(function)
    하나의 특별한 목적의 작업으르 수행하기 위해
    독립적으로 설계된 프로그램 코드의 집합.

def 함수이름(매개변수)
    코드 실행문
    return 반환값

    *** 매개변수(parameter)와 반환값은 없을수도 있음.
'''

# welcome() 함수 정의
def welcome(): # 매개변수 x, 리턴 x
    print('Hello Python')
    print('Nice to meet you')

welcome() # 함수 호출

# 매개변수 o, 리턴 x
def introduce(name, age):
    print('내 이름은 {}이고, 나이는 {}살입니다.'.format(name,age))

introduce('bluemin',29)

# 가변 매개변수 함수
def show(*args): # * = 가변 매개변수를 받는 키워드, 모든 인수를 하나의 튜플로 만들어 줌.
    print(type(args))
    for item in args:
        print(item)

show('python')
show('python', 'happy', 'birthday')

# 반환(return)값이 있는 함수
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

result = address()
print(result)

# 매개변수 o, 리턴 o
def plus(num1, num2):
    return num1 + num2

print(plus(1,3))
print(plus(1343,3234))




area = 0
def move():
    global area # 전역 변수를 변경하고 싶을때는 내부 선언을 해줘야 한다.
    area += 1
    return area

result = move()
print('유닛이 오른쪽으로 {}칸 이동했습니다.'.format(result))
result = move()
print('유닛이 오른쪽으로 {}칸 이동했습니다.'.format(result))
result = move()
print('유닛이 오른쪽으로 {}칸 이동했습니다.'.format(result))
result = move()
print('유닛이 오른쪽으로 {}칸 이동했습니다.'.format(result))






