# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

movie_rank = []     # 순위
movie_title = []    # 제목

URL = 'https://kr.investing.com/currencies/'

# firefox를 띄워 브라우저에 나타난 소스를 스크래핑함
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
# 웹 브라우저를 자동화작업 할 수 있도록 특수하게 컴파일된 브라우저인 geckodriver.exe를 다운로드 후 지정한 위치에 저장
# github.com/mozilla/geckodriver에서 다운로드
driver.get(URL)
source_code = driver.page_source    # firefox로 가져온 소스를 source_code 변수에 저장
#plain_text = source_code.text

# soup = BeautifulSoup(plain_text, 'html.parser')     # html 분석기(성능 떨, 검사 대충)
soup = BeautifulSoup(source_code, 'lxml')            # xml 분석기(성능 굿, 검사 엄격)

currid = [1, 2, 3, 125, 5, 6, 7, 8, 650, 159]   # 종목번호
# 종목 추출
findkey = 'td["class=left noWrap"]'
for title in soup.select(findkey):
    print(title.text.strip().split())
# 현재가 추출
for i in range(1, len(currid)):
    findkey = 'td["class=pid-"' + str(currid[i]) + '"-last"]'
    for title in soup.select(findkey):
        print(title.text.strip().split())