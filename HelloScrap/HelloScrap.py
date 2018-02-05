# -*- coding: utf-8 -*-

# 필수 패키지
# request
# beautifulsoup4

# 파이썬 패키지 설치 방법
# 1. 미리 설치하고 작업 : pip 패키지 관리자
# 2. 작업중 설치 : alt + enter

from bs4 import BeautifulSoup
import requests
import lxml
# py3에서는 bs4로 설치
# py2에서는 BeautifulSoup로 설치

# 지정한 URL로부터 HTML 소스를 가져옴
source_code = requests.get('http://naver.com')
#source_code.encoding ='euc-kr'
# print('%s'%source_code.text)

# 웹 사이트에서 HTML 소스를 출력함 - 보기 불편
print(source_code.text)

# 지정한 웹페이지 소스를 변수에 저장
plain_text = source_code.text

# 웹 소스를 보기 좋게 변환(lxml 이용)
soup = BeautifulSoup(plain_text, 'lxml')
print(soup)
# 웹 소스를 단순히 피싱
soup = BeautifulSoup(plain_text, 'html.parser')
print (soup)

for title in soup.select('h3'):
    print(title.text)

for title in soup.select("h3['class=tit']"):
    print(">>>" + title.text)

