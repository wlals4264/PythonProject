'''
내장 데이터 유형
    Python 변수는 다른 유형의 데이터를 저장할 수 있으며
    다른 유형은 다른 작업을 수행할 수 없다.

텍스트 유형 : str
숫자 유형 : int, float, complex
시퀀스 유형 : list, tuple, range
매핑 유형 : dict
세트 유형 : set
부울(논리) 유형 : bool
바이너리 유형 : bytes, bytearray
값이 없음 유형 : NoneType
'''
# str
x = "Hello Wolrd"
print(type(x))
# int
x = 20
print(type(x))
# float
x = 20.5
print(type(x))
# complex
x = 1j
print(type(x))
# list
x = ["피카츄", "라이츄", "파이리"]
print(type(x))
# tuple
x = ("피카츄", "라이츄", "파이리")
print(type(x))
# range
x = range(6)
print(type(x))
# dict
x = {"name" : "피카츄", "기술" : "백만볼트"}
print(type(x))
# set
x = {"피카츄", "라이츄", "파이리"}
print(type(x))
# bool®®
x = True
print(type(x))

# NoneType
d = None
print(type(d))