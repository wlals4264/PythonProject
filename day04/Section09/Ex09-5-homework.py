'''
[회원가입]
아이디를 입력하세요(3글자 이상) >>>
((3글자가 아닌경우))
> 3글자 이상 입력해주세요

아이디를 입력하세요(3글자 이상) >>>
((3글자 이상인 경우))

패스워드를 입력하세요(영문 숫자 포함 8자이상) >>>
> 영문 숫자 포함 8자 이상 입력해 주세요!

패스워드 확인, 한번 더 입력해주세요 >>>
> 일치하지 않습니다. 다시 입력해 주세요!

패스워드를 입력하세요(영문 숫자 포함 8자이상) >>>

패스워드 확인, 한번 더 입력해주세요 >>>

회원가입 완료!!


[로그인]
아이디를 입력하세요 >>>
> 아이디가 일치하지 않습니다.

아이디를 입력하세요 >>>

패스워드를 입력하세요 >>>
> 패스워드가 일치하지 않습니다.

패스워드를 입력하세요 >>>

로그인 성공!!
ㅇㅇㅇ님 환영합니다 :)
'''

id = None
pwd = None

# 아이디 입력
while True: # 무한루프
    id = input('id를 입력하세요 (3글자 이상) >>> ')
    # id_count = 0
    # for ch in id:
    #     id_count += 1
    # if id_count > 2:
    #     break
    if len(id) > 2:
        break # while문 종료
    print('> 3글자 이상 입력해 주세요.')

# 패스워드 입력
while True:
    pwd = input('패스워드를 입력하세요(영문, 숫자 포함 8자 이상) >>>')
    isContainAlpha = False # 기본값 설정
    isContainNumeric = False

    if len(pwd) < 8:
        print('> 영문, 숫자 포함 8자 이상 입력해 주세요!')
        continue # 다시 while문의 처음으로 돌아가기 위해서 아래 코드 실행하지 않기

    for ch in pwd:
        if ch.isalpha():
            isContainAlpha = True
        elif ch.isnumeric():
            isContainNumeric = True

    # 영문 포함 유효성 검사
    if not isContainAlpha:
        print('> 영문, 숫자 포함 8자 이상 입력해 주세요!')
        continue

    # 숫자 포함 유효성 검사
    if not isContainNumeric:
        print('> 영문, 숫자 포함 8자 이상 입력해 주세요!')
        continue

    # 패스워드 일치 유효성 검사
    pwdChk = input('패스워드를 한번 더 입력하세요 >>> ')
    if pwd != pwdChk:
        print('> 일치하지 않습니다. 다시 입력해 주세요!')
        continue

    break

print('회원가입 완료!😀')

# 로그인 아이디
while True:
    loginId = input('아이디를 입력하세요 >>> ')
    if id == loginId:
        break
    print('> 아이디가 일치하지 않습니다.')

# 로그인 패스워드
while True:
    loginPwd = input('패스워드를 입력하세요 >>> ')
    if pwd == loginPwd:
        break
    print('> 패스워드가 일치하지 않습니다.')

print('로그인 성공!')
print('{}님 환영합니다!! :)'.format(id))
