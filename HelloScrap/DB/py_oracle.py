#-*- coding: utf-8 -*-
import cx_Oracle
import os
# 파이썬에서 oracle을 사용하려면 먼저 Oracle Instant Client와 부속 파일을 설치해야 함
# 1. oracle.com에서 Oracle instant Client 윈도우 x64 다운로드
#    instant client basic, instant client sqlplus
#    C:/java 아래에 압축해제
# 2. visual studio 2013 재배포 패키지 x64 다운로드
# 3. 환경변수 설정
#    ORACLE_HOME, TNS_ADMIN, LD_LIBRARY_PATH, PATH
# 4. cx_Oracle 모듈 설치

os.environ['NLS_LANG'] = '.AL32UTF8'
#os.putenv('NLS_LANG', 'KOREAN_KOREA.KO16KSC5601') # 오라클 환경변수로 인코딩 설정(한글입력가능!)

# id/pwd@ip:port/oracleSID
conn = cx_Oracle.connect('hr/hr@192.168.31.128:1521/xe')
print(conn.version)
curs = conn.cursor()
sql = 'select * from ZIPCODE_SEOUL'
curs.execute(sql)
rows = curs.fetchall()
for row in rows:
    print(row)
    # 오라클에서는 Dict커서를 공식적으로 지원하지 않음
cols = dict((name, col) for col, name in enumerate(curs.description))
print(cols['EMAIL'])
curs.close()
conn.close()