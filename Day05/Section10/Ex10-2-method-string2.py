# join() 메소드
s = '-'.join('python')
print(s)

s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = ''.join(['a', 'b', 'c', 'd', 'e'])
print(s)

# split() ✨메소드 자주 사용✨
s = 'Life is too short'
result = s.split() # 기본적으로 공백을 기준으로 분리
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result)

data = 'bluemin|29|n잡러'
result = data.split('|')
print(result)
print('이름 : {}'.format(result[0]))

# replace()
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 공백제거
s = '          apple'
print(s)
result = s.lstrip() # 왼쪽 공백 제거
print(result)

s = 'apple          '
print(s)
result = s.rstrip() # 오른쪽 공백 제거
print(result)

s = '      apple      '
print(s)
result = s.strip() # 양쪽 공백 제거
print(result)

# 전체 공백제거
s = ' a p p l e '
print(s)
result = s.strip()
print(result)
result = s.replace(' ','') # 공백도 문자이기 때문에 공백을 공백이 없는 문자로 대체
print(result)

