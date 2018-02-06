# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import codecs

movie_rank = []     # 순위
movie_title = []    # 제목
movie_grade = []    # 평점
movie_opdate = []   # 개봉일

URL = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'
source_code = requests.get(URL)
plain_text = source_code.text

# soup = BeautifulSoup(plain_text, 'html.parser')     # html 분석기(성능 떨, 검사 대충)
soup = BeautifulSoup(plain_text, 'lxml')            # xml 분석기(성능 굿, 검사 엄격)
#  print(soup)
# 순위 추출
for i in range(1, 21):
    findkey = 'span["class=ico_ranking ico_top' + str(i) + '"]'
    for title in soup.select(findkey):
        # print("".join(title.text.strip().split()))
        movie_rank.append("".join(title.text.strip().split()))
# 제목 추출
findkey = "a['class=link_g']"
for title in soup.select(findkey):
    # print(title.text.strip())
    movie_title.append(title.text.strip())
# 평점 추출
findkey = "em['class=emph_grade']"
for title in soup.select(findkey):
    # print(title.text.strip() + '/10')
    movie_grade.append(title.text.strip())
# 개봉일 추출
findkey = "dl['class=list_state']"
for title in soup.select(findkey):
    # print(title.select('dd')[0].text)
    movie_opdate.append(title.select('dd')[0].text)
# 모든 내용 출력
for i in range(0, 20):
    print(movie_rank[i] + movie_title[i] + movie_grade[i] + movie_opdate[i])

# --- 파일 저장하기(Python2.7)
fmt = '%s, %s, %s, %s \n' # 출력형식 정의
f = codecs.open('movie_rank2a.txt', 'w', 'utf-8') # 파일을 쓰기모드로 open(쓰기모드 : w, 읽기모드 : r)
# f.write('hello,python!\n')          # 파일에 내용쓰기
# f.write(rank) # 유니코드 문자 저장시 오류발생! codecs 추천!
# 파이썬2는 기본적으로 모든 문자를 ascii로 처리하기 때문에
# 파일에 기록시 먼저 ascii로 디코딩하기 때문에 오류발생!
for i in range(0, 20):
    rank = fmt % (movie_rank[i], movie_title[i], movie_grade[i], movie_opdate[i])
    f.write(rank)
f.close()                           # 파일 종료(필수!)

# --- 파일 저장하기(Python3.5)
try:
    f = open('movie_rank3.txt', 'w', encoding = 'utf-8')
    for i in range(0, 20):
        rank = fmt % (movie_rank[i], movie_title[i], movie_grade[i], movie_opdate[i])
        f.write(rank)
    f.close()
except Exception as ex:
    print(ex)

# --- 파일 읽어 출력하기(Python2.7)
# readline : 한줄씩 읽어옴(추가적으로 while 필요)
# readlines : 모든줄을 읽어옴(추가적으로 for 필요)
# read : 파일 내용 전체 읽어옴 - 바이너리 파일 처리시 사용
f = codecs.open('movie_rank2a.txt', 'r', 'utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt', 'r', 'utf-8')
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt', 'r', 'utf-8')
data = f.read()
print(data)
f.close()

# --- 파일 읽어 출력하기(Python3.5)
f = codecs.open('movie_rank2a.txt', 'r', encoding = 'utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt', 'r', encoding = 'utf-8')
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt', 'r', encoding = 'utf-8')
data = f.read()
print(data)
f.close()

# with ~ as 구문으로 파일 다루기
# 파일 작업시 파일을 열고 닫는 것은 번거로운 일임
# 파이썬이 알아서 닫아주면 편리함
with codecs.open('movie_rank2a.txt', 'r', 'utf-8') as f:
    data = f.read()
    print(data)

# 파일 읽기 / 쓰기 모드
# r : read(읽기 모드)
# w : write(쓰기 모드)
# t : text(텍스트 파일)
# b : binary(바이너리 파일 : 이미지, 압축)
# a : append(추가)
# + : update(수정)
# 파일모드의 기본값은 : rt