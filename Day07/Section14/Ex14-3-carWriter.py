'''
+ 인코딩과 디코딩에 대해서
    인코딩(Encoding)
        문자 -> 바이너리(0과 1)로 변환
        컴퓨터가 읽을 수 있는 바이너리로 변환
        암호학 - 암호화

    디코딩(Decoding)
        바이너리 -> 문자로 변환
        암호학 - 복호화
'''
import csv

# 방법1
'''
with open('차량관리.csv', 'w', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다.')
'''

# 방법2
'''
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다.')
'''

# 방법3
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',', quotechar='"') # quotechar='"'가 디폴트
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다.')

