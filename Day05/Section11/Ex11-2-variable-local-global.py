'''
지역변수(local)
    함수 내부선언
    함수 내부에서만 사용가능

전역변수(global)
    함수 외부선언
    함수 내부 외부 모두 사용가능

'''

gVar = '전역'

def globalAndlocal():
    lVar = '지역'
    print(gVar, '변수 입니다.') # 전역변수 참조만 가능.(변경은 불가능)
    print(lVar, '변수 입니다.')

globalAndlocal()

gVar = '전역'
def globalAndlocal():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역'
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')
globalAndlocal()

print(gVar)

print()

# 전역변수 선언
total = 0
def gift(dic, who, money):
    global total # 전역변수 total을 사용하겠다
    total += money
    dic[who] = money

wedding = {}
gift(wedding, '영희', 5) # {'영희' : 5}, total = 5
print(type(wedding))
print(wedding)
print(total)
gift(wedding, '철수', 6) # {'영희' : 5, '철수' : 6} , total = 11
print(wedding)
print(total)
gift(wedding, '이모', 10) # {'영희' : 5, '철수' : 6, '이모' : 10} , total = 21
print(wedding)
print(total)

print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))

