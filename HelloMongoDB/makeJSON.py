# -*- coding: utf-8 -*-
import codecs
import datetime
import json
from collections import OrderedDict


# JSON(JavaScript Object Notation)
# 여러 시스템 간 데이터 교환을 위해 고안한 데이터형
# XML : 데이터를 정의하는 태그 때문에 파일용량이 커짐
# CSV : XML보다 용량은 작지만, 데이터의 의미 파악이 힘듦

# 자바스크립트의 객체 표기법을 차용해서 만듦
# 객체는 키, 값의 형식으로 작성 - 경량 데이터 표기
# XML과 CSV의 장점만 따서 만든 것이라 폭팔적인 지지를 받음

# 주의! 파이썬에서는 이건과 유사한 자료구조인 dictionary가 이미 있음
# JSON과 dictionary 자료구조는 서로 구분해야 할 필요가 있기 때문에
# dictionary 자료구조로 정의된 객체는 dumps, loads 명령으로 JSON 객체로 변환해서 처리

# 성적 데이터를 JSON 데이터로 생성한 뒤 파일에 그것을 저장하는 예제

today = datetime.datetime.now()
sungjuk = {'hakbun' : 'a12345', 'name' : '수지',
           'kor' : '99', 'eng' : '88', 'mat' : '77'}
print(sungjuk)

# JSON 형식으로 인코딩 - json.dump
jsonstring = json.dumps(sungjuk)

print(jsonstring)
print(type(jsonstring))

# JSON 형식을 보기좋게 출력하려면? - indent 사용
jsonstring = json.dumps(sungjuk, indent=4)
print(jsonstring)

# JSON 형식을 python에서 처리할 수 있도록 디코딩 - loads
# 디코딩된 결과는 dictionary 형식으로 다룰 수 있음
sjDict = json.loads(jsonstring)
print('%s %s' %(u'학번', sjDict['hakbun']))
print('%s %s' %(u'국어', sjDict['kor']))

# JSON 형식을 파일에 쓰기
with codecs.open('sungjuk1.json', 'w', 'utf-8') as make_json :
    # JSON으로 변환된 객체를 파일에 기록
    make_json.write(jsonstring)
with codecs.open('sungjuk2.json', 'w', 'utf-8') as make_json:
    # 파일에 기록할 때 JSON으로 변환
    json.dump(sungjuk, make_json)

# JSON 형식 파일 읽기
with codecs.open('sungjuk2.json', 'r', 'utf-8') as read_json:
    # sungjuk2.json 내용을 json으로 변환해서 readjson에 저장
    readjson = json.load(read_json)
print(readjson)

# 파일에서 읽은 내용을 dictionary 형식으로 처리
print(readjson['mat'])
print(readjson['name'])

# 학생 데이터를 JSON으로 다루기
hakbun = '20130050'
name = u'수지'
addr = u'서울'
age = 25
birth = '1992.07.05'
depart = u'컴퓨터공학'
profid = '504'
meeting = u'목, 2교시'
# 유니코드 들어간 것은 str로 감쌀필요 없음
emdstudent = {'hakbun' : str(hakbun), 'name' : name,
           'addr' : addr, 'age' : age, 'birth' : str(birth),
           'depart' : depart, 'profid' : str(profid), 'meeting' : meeting}
print(emdstudent)

stdjson = json.dumps(emdstudent)
print(stdjson)

stdDict = json.loads(stdjson)

print(stdDict['name'])
print(stdDict['addr'])

deptname = u'컴퓨터공학'
depttel = '123-4567-8901'
deptoff = u'E동 2층'
deptchf = '504'
deptdate = u'2007년'

profid = '504'
profname = '이성계'
porfdopt = '철학'

student2 = {'hakbun' : hakbun, 'name' : name, 'addr' : addr,
            'age' : age, 'birth' : birth, 'meeting' : meeting,
            'depart' : {'deptname' : deptname,
                        'depttel' : depttel,
                        'deptoff' : deptoff,
                        'deptchf' : {'profid' : '504',
                                     'profname' : '이성계',
                                     'profdept' : '철학'},
                        'deptdate' : deptdate},
            'profid' : {'profid' : '504',
                        'profname' : '이성계',
                        'profdept' : '철학'}}
print(student2)
std2json = json.dumps(student2)
print(std2json)

std2Dict = json.loads(std2json)
print(std2Dict['name'])
# print(std2Dict['depart.departname'])
# print(std2Dict['profid.profname'])

for key in std2Dict['depart']:
    print(key)
    for doc in std2Dict['depart'][key]:
        print(doc)

# print(std2Dict['depart.deptname'])
print(std2Dict['depart']['deptname'])
# print(std2Dict['profid.profname'])
print(std2Dict['profid']['profname'])

# 또 다른 방법으로 학생 JSON 데이터 생성하기
# OrderedDict를 이용한 JSON 간단 예제
idol_group = OrderedDict()
album = OrderedDict()
albums = OrderedDict()

idol_group["name"] = u'소녀시대'
idol_group["members"] = [u'태연', u'써니', u'효연', u'유리', u'윤아']

albums['years'] = 2007
albums['name'] = u'소녀시대'
albums['1집'] = album

idol_group["albums"] = albums

idolJson = json.dumps(idol_group)
print(json.dumps(idol_group))

stud = OrderedDict()
dept = OrderedDict()
prof = OrderedDict()

stud['name'] = u'김태희'
stud['addr'] = u'경기도 고양시'
stud['age'] = 25
stud['birth'] = u'1992.07.05'
stud['meeting'] = u'목, 2교시'

dept['deptname'] = u'컴퓨터공학'
dept['depttel'] = '123-4567-8901'
dept['deptoff'] = u'E동 2층'
dept['deptchf'] = '504'
dept['deptdate'] = u'2007년'

prof['profid'] = u'504'
prof['profname'] = u'이성계'
prof['profdept'] = u'철학'

stud['depart'] = deptchf
stud['profid'] = prof