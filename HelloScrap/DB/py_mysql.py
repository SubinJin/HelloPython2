#-*- coding: utf-8 -*-

#파이썬에서 MySQL을 사용하려면 Python 표준 DB API를 지원하는 MySQL DB 모듈을 다운로드한 후 설치해야 함 - PyMySQL

import pymysql

# MySQL connection 생성
conn = pymysql.connect(host='192.168.31.128', user='ronaldotree', password='Abcdef_12', db='ronaldotree')
# connection에서 cursor 생성
curs = conn.cursor()
# sql문 작성 후 실행
sql = 'select * from employees'
curs.execute(sql)
# 필요하다면, 실행한 sql로부터 데이터 처리
rows = curs.fetchall()
for row in rows:
    print(row[0], row[1], row[2])
    # print(row[0], row['email'], row['jobTitle'])
# connection 닫기
curs.close()
conn.close()

#--- 사전식 커서 사용
conn = pymysql.connect(host='192.168.31.128', user='ronaldotree', password='Abcdef_12', db='ronaldotree')
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = 'select * from customers where state = %s and city = %s'
curs.execute(sql,('NY', 'NYC'))
rows = curs.fetchall()
for row in rows:
    print(row['phone'], row['city'], row['state'])
curs.close()
conn.close()

#--- 간단한 CRUD 테스트
#--- delete from index_test
#--- insert into index_test values('ronaldotree','987654')
#--- update index_test set uid = 'ronaldotree' where uid = 'ronaldotree'
#--- select * from index_test
conn = pymysql.connect(host='192.168.31.128', user='ronaldotree', password='Abcdef_12', db='ronaldotree')

curs = conn.cursor()
sql = 'delete from index_test'
curs.execute(sql)
curs.close()
conn.commit()   # insert, update, delete시 필요!

curs = conn.cursor()
sql = 'insert into index_test values(%s, %s)'
curs.execute(sql,('ronaldotree','123456'))
curs.close()
conn.commit()

curs = conn.cursor()
sql = 'update index_test set uid = %s where uid = %s'
curs.execute(sql,('RONALDOTREE', 'ronaldotree'))
curs.close()
conn.commit()

# 데이터 조회
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = 'select * from index_test'

curs.execute(sql)
rows = curs.fetchall()

for row in rows:
    print(row['uid'], row['pwd'])
curs.close()
conn.close()
