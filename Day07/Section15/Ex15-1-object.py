'''
클래스
    객체를 만드는 설계도

객체(object)
    현실 세계 존재하는 물리적, 추상적 식별할 수 있는 모든것.
    예) 컴퓨터, 학생, 주문, 배송

객체 구성 요소
    생성자 - 초기화용
    속성 값 - 변수
    기능 - 메소드(함수)
'''

# Computer 클래스 정의
class Computer:

    # 첫번째 매개변수가 self 이므로 인스턴스 메소드이다.
    # self를 제외한 나머지 매개변수에 실제로 사용될 데이터가 전달된다.

    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))

desktop = Computer()
desktop.set_spec('i7', '16GB', 'GTX3060', '512GB')
desktop.hardware_info()
print()

macbook = Computer()
macbook.set_spec('M2', '16GB', 'RETINA Display', '512GB')
macbook.hardware_info()
print()

print(id(desktop))
print(id(macbook))











