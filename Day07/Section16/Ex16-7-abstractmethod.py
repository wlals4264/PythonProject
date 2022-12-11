'''
추상메소드(Abstract Method)
    선언만하고 구현되지 않은 미완성 메소드

추상클래스(Abstract Class)
    추상메소드를 하나 이상 가지고 있는 클래스
'''
from abc import * # abc metaclass 상속이 필요.

class Family(metaclass=ABCMeta):
    @abstractmethod
    def introduce(self):
        pass # 슈퍼클래스 자체에서 구현은 x 설계만. 상속받는 클래스에서 정의하여 구현.

class Person(Family):
    def introduce(self):
        print('저는 사람입니다.')

a = Person()
a.introduce()

