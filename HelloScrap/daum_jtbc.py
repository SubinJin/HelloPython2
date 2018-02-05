# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 다음 JTBC 뉴스 스크래핑 예제
# http://media.daum.net/cp/98?page=2&regDate=20180203

# URL 변수 지정
press = [310]       # JTBC 310
date = [20180205]   # 날짜
page = [1, 2, 3]            # 페이지
new_title = []      # 뉴스 제목
new_desc = []       # 뉴스 간략소개

# URL 변수 적용
URL = 'http://media.daum.net/cp/' + str(press[0]) + '?page=' + str(page[0]) + '&regDate=' + str(date[0])

# 스크래핑해서 소스를 source_code에 저장
source_code = requests.get(URL)

# 중간 결과 출력
# print(source_code.text)

# 텍스트 추출을 위해 lxml로 태그 분석(메모리 적재)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'lxml')

# 기사 제목 출력
cnt = 1
for title in soup.select("a['class=link_txt']"):
    if cnt > 15: break
    print(title.text.strip())
    cnt += 1

# 기사 간략 출력
cnt = 1
for desc in soup.select("span['class=link_txt']"):
    if cnt > 15: break
    print(desc.text.strip())
    cnt += 1

# 기사 제목 저장
cnt = 1
for title in soup.select("a['class=link_txt']"):
    if cnt > 15: break
    new_title.append(title.text.strip())
    cnt += 1
# 기사 간략 저장
cnt = 1
for desc in soup.select("span['class=link_txt']"):
    if cnt > 15: break
    new_desc.append(desc.text.strip())
    cnt += 1
# 기사 제목, 간략 출력
for i in range(0, 15):
    print(new_title[i])
    print("%s\n" %(new_desc[i]))