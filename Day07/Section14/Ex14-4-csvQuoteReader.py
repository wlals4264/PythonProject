member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"') # 큰따옴표(") 제거
        member[2] = member[2].strip('\n') # 줄바꿈 제거, 데이터 전처리 작업, 순수한 데이터를 담기 위해
        member_list.append(member)
print(member_list)
