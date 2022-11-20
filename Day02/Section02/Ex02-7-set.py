'''
Set
   순서가 없다
   변경할 수 없다(추가는 가능)
   인덱싱도 되지 않는 컬렉션(배열성이 있는 자료구조 데이터 객체)
   중복값은 없다
'''
thisset = {"피카츄", "라이츄", "파이리"}
# 실행할 때 마다 순서가 변경
print(thisset)
# 항복 가져오기
for x in thisset:
    print(x)

# 값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset) #리턴은 bool값
print("꼬부기" in thisset)

# 항목 추가하기
thisset.add("꼬부기")
print(thisset)

# 다른 set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "라이츄"} # 라이츄는 중복값, 중복값은 추가가 안됨
thisset1.update(thisset2)
print(thisset1)

# 항목제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
# thisset.remove("피카츄")
# print(thisset) error 뜸

thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset) #error 방지용으로 discard를 사용하는게 안전

# 항목제거
thisset.pop()
print(thisset) #무작위로 1개 삭제 (순서가 없기 때문)

# 비우기
thisset.clear()
print(thisset)