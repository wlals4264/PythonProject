'''
CSV(comma-separated Values)
    필드를 쉼표(,)로 구분한
    텍스트 데이터 파일
'''
student_list = []
with open('학생명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline() # 첫 줄 읽고 다음으로 넘어가기 == 첫줄제거
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',') # ','단위로 각부분을 잘라서 리스트로 반환
        student_list.append(student)
print(student_list)