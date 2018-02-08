# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://kr.investing.com/currencies/'

# 웹 브라우저 자동화를 위해 드라이버 초기화
driver = webdriver.Firefox(executable_path = 'C:\Program Files\Mozilla Firefox\geckodriver.exe')

# 브라우저를 지정한 URL로 이동시킴
driver.get(URL)

# 웹 페이지 오른쪽 '원자재'탭의 xpath 정의
# alink = driver.find_element_by_xpath("//li[@id='QBS_7']/a")
alink = driver.find_element_by_xpath("//*[@id='QBS_3']")

# 마우스, 단축키 이벤트 처리를 위해 ActionChains 사용
mouse = webdriver.ActionChains(driver)

# 해당 링크를 마우스클릭으로 처리하기 위해 move_to_element를 사용
mouse.move_to_element(alink).click().perform()

# 클릭 후 보여지는 페이지 내용을 source_code에 저장
source_code = driver.page_source
# print(source_code)

# 웹 페이지 내용을 parsing하기 위해 bs4로 초기화
soup = BeautifulSoup(source_code, 'html.parser')

comcode = ['sb_commodities-gold', 'sb_commodities-silver', 'sb_commodities-us-corn']
comcurcode = ['8830', '8836', '8918']

for i in range(0, len(comcode)):
    # 원자재
    findkey = 'a["data-gae=' + str(comcode[i]) + '"]'
    for title in soup.select(findkey):
        print((title.text).encode('utf-8'))

    # 원자재 환율
    findkey = 'td["id=sb_last_' + str(comcurcode[i]) + '"]'
    for title in soup.select(findkey):
        print((title.text).encode('utf-8'))