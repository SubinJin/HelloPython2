
# 파이썬으로 상관분석, 회귀분석 테스트
import numpy as np
import pandas as pd
# csv 파일 읽어오기
hdr = ['V1','V2','V3','V4','V5','V6','V7','V8','V9' ]
df = pd.read_csv('C:/Bigdata/R3/phone-02.csv', header=None, names=hdr)
print(df)
# 상관분석 실시
dfc = df.corr()
print(dfc) # V7, V9가 상관관계 유의미
print('')
df97 = df.V9.corr(df.V7) # df97 = df['V9'].corr(df['V7']) 도 가능
print('핸드폰 사용량-데이터 소모량 관계 :', df97)
print('')
# 회귀분석 실시
from scipy import stats
lm = stats.linregress(df.V7, df.V9)
print(lm) # 나오는 순서 : 기울기, 절편, 상관계수, 오류지수p, 표준오차
print('')
# 회귀식 : y = 기울기x + 절편
# 어떤 공장의 월별생산량(x)과 전기사용량(y)을 이용해서 회귀분석
# x : 독립변수, y : 종속변수
from scipy import polyval
make = [ 3.52, 2.58, 3.31, 4.07, 4.62, 3.98, 4.29, 4.83, 3.71, 4.61, 3.90, 3.20 ]
# 단위 : 억
power = [ 2.48, 2.27, 2.47, 2.77, 2.98, 3.05, 3.18, 3.46, 3.03, 3.25, 2.67, 2.53]
data = {'매출' : make, '전기' : power}
mp = pd.DataFrame(data, index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
slope, intercept, rvalue, pvalue, stderr = stats.linregress(make, power)
print(slope, intercept, rvalue, pvalue, stderr)
# 회귀식 y = slope * x + intercept
# 만약에 매출이 4억이면 전기사용량은 얼마인가?
y = slope * 4 + intercept
print(y)
import matplotlib.pyplot as plt
import matplotlib
krfont = {'family' : 'Malgun Gothic', 'weight' : 'bold', 'size' : 10}
matplotlib.rc('font', **krfont)
ry = polyval([slope, intercept], make)
plt.plot(make, power, 'b.') # 파랑색 점
plt.plot(make, power, 'b,')
plt.plot(make, power, 'bo')
plt.plot(make, power, 'b^')
plt.plot(make, power, 'b>')
plt.plot(make, power, 'b1')
plt.plot(make, power, 'bs') # 사각형
plt.plot(make, power, 'bp') # 오각형
plt.plot(make, power, 'bh') # 육각형
plt.plot(make, power, 'b*') # 별
plt.plot(make, power, 'bD') # 다이아몬드
plt.plot(make, ry, 'r.-') # 빨간색 점, 실선
plt.plot(make, ry, 'r.--')
plt.plot(make, ry, 'r.-.')
plt.plot(make, ry, 'r.:')
plt.title('회귀분석 결과')
plt.legend(['실제 데이터', '회귀분석을 따르는 모델'])
plt.show()