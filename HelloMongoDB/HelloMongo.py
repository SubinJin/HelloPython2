# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pprint
import datetime
# MongoDB 외부접속을 가능하게 하려면 설정파일에 'bind_ip=아이피주소'를 추가

# 몽고디비 연결객체 만들기
# client = MongoClient()
# client = MongoClient('192.168.56.101', 27017)
client = MongoClient('mongodb://192.168.56.101:27017')

# 데이터베이스 객체 가져오기
# db = client['ronaldotree']
db = client.ronaldotree

# 컬렉션 객체 가져오기
# coll = db['inventory']
coll = db.inventory
# coll2 = db['inventory2']
coll2 = db.inventory2
# coll3 = db['restaurants']
coll3 = db.restaurants

# 단일문서 조회
print(coll.find_one())
print(coll2.find_one())
print(coll3.find_one())

# 단일문서 조회 - JSON을 보기좋게 출력(pprint)
pprint.pprint(coll.find_one())
pprint.pprint(coll2.find_one())
pprint.pprint(coll3.find_one())

# 전체문서 조회(커서를 이용해야 함)
# pprint.pprint(coll.find()) 안됨
cursor = coll.find()
for doc in cursor :
    pprint.pprint(doc)

cursor2 = coll2.find()
for doc in cursor2 :
    pprint.pprint(doc)

cursor3 = coll3.find().limit(5)
for doc in cursor3 :
    pprint.pprint(doc)

# 조건으로 질의하기(답 1개만..)
# item이 notebook
print(coll.find_one({'item' : 'notebook'}))
# qty가 50보다 작은 item 조회
print(coll2.find_one({'qty' : {'$lt' : 50}}))
# address가 10462
print(coll3.find_one({ 'zipcode.address' : '10462' }))

# 데이터 추가하기 - JSON 생성
student = {'hakbun' : 'a12345',
           'name' : '수지',
           'addr' : 'seoul, korea',
           'regdate' : datetime.datetime.now()}
many_student = [{'hakbun' : 'a12345',
                 'name' : '수지',
                 'addr' : 'seoul, korea',
                 'regdate' : datetime.datetime.now()},
                {'hakbun' : 'z98765',
                 'name' : '지수',
                 'addr' : 'busan, korea',
                 'regdate' : datetime.datetime.now()}
               ]

# 데이터 추가하고 object_id값을 objId 변수에 저장
objId = db.students.insert_one(student).inserted_id
result = db.students.insert_many(many_student)

print(objId)
print(db.student.find_one())
print(result.inserted_ids)

# 데이터 수정
# 학번 a12345인 학생의 주소를 인천으로 변경
result = db.students.update_one(
    {'hakbun' : 'a12345'},
    {'$set' : {'addr' : 'incheon, korea'}})

print(result.matched_count, result.modified_count)

# 데이터 삭제
# 학번 a12345인 학생 정보 하나만 삭제
result = db.students.delete_one({'hakbun' : 'a12345'})
print(result.deleted_count)
# 학번 a12345인 학생 정보 모두 삭제
result = db.students.delete_many({'hakbun' : 'a12345'})
print(result.deleted_count)
# 모두 삭제
result = db.students.delete_many({})
print(result.deleted_count)

# 몽고디비 접속해제
client.close()