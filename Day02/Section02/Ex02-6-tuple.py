'''
튜플
    단일 변수에 여러 항목을 저장하는데 사용된다.
    순서가 있고 변경할 수 없는 List
    둥근 괄호로 작성된다. ()
'''
thistuple = ("피카츄", "라이츄", "파이리")
print(thistuple)
# 튜플 길이 len()
print(len(thistuple))
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])
# 튜플값 변경 방법
thistuple = ("피카츄", "라이츄", "파이리")
thiscast = list(thistuple)
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(thistuple)
# !리스트보다 리소스 사용을 적게 쓰기 때문에 변경이 필요 없다면 튜플 사용하는게 좋다!

# 튜플 압축풀기 (튜플안의 값을 각각 변수에 할당하기)
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
(p1, p2, p3, p4) = thistuple
print(p1)
print(p2)
print(p3)
print(p4)
print(type(p1))

# 두개 튜플 조인
thistuple1 = ("피카츄", "라이츄", "파이리", "꼬부기")
thistuple2 = ("버터풀", "야도란", "피존투", "또가스")
thistuple3 = thistuple1 + thistuple2
print(thistuple3)

