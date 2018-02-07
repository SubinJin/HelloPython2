# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# selenium
# 웹 응용프로그램의 작동여부를 알아보기 위해 사용하는 자동 웹 사용성 테스트 프로그램
# 웹 사용성 테스트는 주로 웹브라우저를 이용

# selenium 설치
# firefox용 webdriver 설치

movie_rank = []     # 순위
movie_title = []    # 제목

URL = 'http://movie.daum.net/main/new#slide-1-0'

# firefox를 띄워 브라우저에 나타난 소스를 스크래핑함
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
# 웹 브라우저를 자동화작업 할 수 있도록 특수하게 컴파일된 브라우저인 geckodriver.exe를 다운로드 후 지정한 위치에 저장
# github.com/mozilla/geckodriver에서 다운로드
driver.get(URL)
source_code = driver.page_source    # firefox로 가져온 소스를 source_code 변수에 저장
#plain_text = source_code.text

# soup = BeautifulSoup(plain_text, 'html.parser')     # html 분석기(성능 떨, 검사 대충)
soup = BeautifulSoup(source_code, 'lxml')            # xml 분석기(성능 굿, 검사 엄격)
#  print(soup)
# 순위 추출
for i in range(1, 10):
    findkey = 'em["class=num_rank rank_0' + str(i) + '"]'
    for title in soup.select(findkey):
        print("".join(title.text.strip().split()))
# 제목 추출
    findkey = 'a["class=link_txt #top #ranking #title @' + str(i) + '"]'
    for title in soup.select(findkey):
        print(title.text.strip())