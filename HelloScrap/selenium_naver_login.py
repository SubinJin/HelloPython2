# -*- coding: utf-8 -*-

import time

from BeautifulSoup import BeautifulSoup
from selenium import webdriver

URL = 'https://naver.com/'

# 웹 브라우저 자동화를 위해 드라이버 초기화
driver = webdriver.Firefox(executable_path = 'C:\Program Files\Mozilla Firefox\geckodriver.exe')

# 브라우저를 지정한 URL로 이동시킴
driver.get(URL)

# 로그인창에 아이디 / 비번 입력 후 로그인 버튼 클릭
# html 요소중 id가 id인 요소를 찾음
userid = driver.find_element_by_id('id')

# @id=id인 요소에 아이디를 입력
userid.send_keys('jeensb0705')

# html 요소중 id가 pw인 요소를 찾음
passwd = driver.find_element_by_id('pw')

# @id=pw인 요소에 비밀번호를 입력
passwd.send_keys('wlstnqls92!')

# 로그인 버튼을 찾아 클릭
loginbtn = driver.find_element_by_xpath('//input[@title="로그인"]')
loginbtn.submit()

# 처리 속도가 빨라서 로그인 완료 페이지가 뜨기 전에 메일 확인 페이지로 이동하려고 함
# 로그인 완료 페이지가 뜨는 것을 확인하기 위해 일정시간동안 브라우저를 대기시킴
# driver.implicitly_wait(10) 이건 왠지모르게 잘 안됨
time.sleep(3)

# 메일 페이지로 이동
MailURL = 'https://mail.naver.com/?n=1518057980364&v=f'
driver.get(MailURL)

source_code = driver.page_source
soup = BeautifulSoup(source_code, 'html.parser')

# 안 읽은 메일 (span[class=cnt], //span[@class="cnt"])
findkey = 'span["class=cnt"]'
for title in soup.select(findkey):
    print(title.text)

# 로그아웃버튼 클릭 - 로그아웃
# time.sleep(3)
# mouse = webdriver.ActionChains(driver)
# logoutbtn = driver.find_element_by_id("gnb_logout_button")
# mouse.move_to_element(logoutbtn).click().perform()
#
# time.sleep(3)
# logoutbtn = driver.find_element_by_id("//span[@id='gnb_name1']")
# mouse.move_to_element(logoutbtn).click().perform()
time.sleep(3)
driver.get('http://nid.naver.com/nidlogin.logout?returl=http://naver.com')
