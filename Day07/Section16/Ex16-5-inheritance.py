'''
죽음의 다이아몬드
다중 상속
'''
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B, C):
    pass # 세부사항은 필요없고 빈껍데기만 필요할 때 사용하는 키워드

x = D()
x.greeting()
print(D.mro()) # 상속 우선순위 출력 B > C > A > Object 순
