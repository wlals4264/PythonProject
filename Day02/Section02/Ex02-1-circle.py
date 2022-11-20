'''
개요 : 반지름을 전달하면 원의 넓이를 반환하는 get_area() 함수
'''

#math 모듈 포함
import math

#get_area() 함수 정의
def get_area(radius):
    """반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수"""
    area = math.pi * math.pow(radius, 2) #math.pi === 원주율 / math.pow(a,2) === a를 제곱
    return area

radius = 1.5
print(radius)

# get_area() 함수 호출 결과를 area 변수에 저장
area = get_area(radius)
print(area)
print(get_area.__doc__) # Docsting 확인 === 함수나 모듈의 공식적인 설명을 주석으로 달아주는 것
