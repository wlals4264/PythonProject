'''
그 외 파이썬 내장함수들
'''
result = format(10000) # str(10000)과 같다.
print(type(result))
result = format(10000, ',') # 천단위 쉼표
print(result)

# abs() : 절대값 반환
result = abs(10)
print(result)
result = abs(-10)
print(result)

# max() : 최대값 반환
# min() : 최소값 반환
result = max(1,10)
print(result)
li = [5, 3, 4, 2, 1]
result = max(li)
print(result)
result = min(li)
print(result)

# pow() : 거듭제곱 함수
result = pow(10, 2)
print(result)

# sorted() : 정렬
my_li = [5, 6, 3, 4, 1, 2]
print(my_li)
print(my_li[0])
result = sorted(my_li) # 디폴트 오름차순 정렬
print(result)
print(result[0])
result = sorted(my_li, reverse=True) # 내림차순으로 변경
print(result)

# zip() : 같은 인덱스 번호끼리 튜플로 묶어 반환
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)

names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for name, score in zip(names, scores):
    print('{}의 점수는 {}점 입니다.'
          .format(name, score))

