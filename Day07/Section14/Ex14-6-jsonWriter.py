'''
JSON (JavaScript Object Notation)
    - 딕셔너리 비슷하다.
    - 구조
    { K : V }
'''
import json

# 방법1
'''
dict_list = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [
            175.5,
            70.5
        ]
    },
    {
        'name': 'alice',
        'age': 21,
        'spec': [
            168.5,
            60.5
        ]
    }
]
json_string = json.dumps(dict_list)

with open('dictList.json', 'w') as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다')
'''

# 방법2
dict_list = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [
            175.5,
            70.5
        ]
    },
    {
        'name': '홍길동',
        'age': 21,
        'spec': [
            168.5,
            60.5
        ]
    }
]
# indent 들여쓰기, ensure_ascii=False 아스키코드로 읽는것을 false로. 즉, 한글로 읽을 수 있게 하기.
json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)

with open('dictList.json', 'w') as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다')
