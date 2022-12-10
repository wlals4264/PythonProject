'''
생성자
    인스턴스를 생성할 생성자가 자동으로 호출된다.(인스턴스화 할 때, 클래스를 메모리 위에 올릴 때)
    객체 초기화 용으로 사용한다.
'''
class USB:
    #생성자
    def __init__(self,capacity):
        self.capacity = capacity

    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(64)
usb.info()










