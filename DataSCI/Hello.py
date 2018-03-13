from pylab import *

figure()
x = linspace(0, 5, 10)
y = x ** 2
plot(x, y)
xlabel('X')
ylabel('Y')
title('샘플그래프')
show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_excel('c:/java/sungjuk.xlsx')
# xlrd 패키지 설치 필요! - 엑셀을 읽어서 dataframe으로 생성하는 기능

# 총점, 평균 계산 후 df에 추가
subj = ['국어', '영어', '수학', '과학']
df['총점'] = df[subj].sum(axis=1)
df['평균'] = df['총점'] / len(subj)
df.sort_values(['평균'], ascending = [False]) # 평균으로 정렬


import numpy as np
data = np.random.rand(3, 4) # 3*4 행렬에 난수 생성
print(data)

list = [3, 4.1, 5, 6.3, 7, 8.6]
arr = np.array(list)
print('평균', arr.mean())
print('합계', arr.sum())
print('최대값', arr.max())
print('최소값', arr.min())
print('분산', arr.var())
print('표준편차', arr.std())

list = [[9, 8, 7, 6, 5], [1, 2, 3, 4, 5]] # 중첩 리스트
arr = np.array(list)
print(arr)
print(arr[0, 2]) # 7
print(arr[1, 3]) # 4
print(arr[0, :]) # 1행 출력
print(arr[:, 1]) # 2열 출력

# 자동으로 채워지는 행렬 생성
zarr = np.zeros((3, 5)) # 0으로 채워지는 3*5 행렬 생성
print(zarr)
# 정수 생성
cnt = 0
for i in np.arange(3):
  for j in np.arange(5):
    cnt += 1
    zarr[i, j] = cnt
print(zarr)

# 외부 csv 파일 읽어서 배열 생성
phone = np.genfromtxt('c:/java/phone-01.csv', delimiter=',')
print(phone)
# 화면크기 항목에 대한 평균 출력
print(np.mean(phone[:, 2]))
print(np.median(phone[:, 2]))
print(len(phone[:, 2]))

p_col3 = phone[:,2]
print(np.percentile(p_col3, 0))
print(np.percentile(p_col3, 25))
print(np.percentile(p_col3, 50))
print(np.percentile(p_col3, 75))
print(np.percentile(p_col3, 100))


from scipy.stats import describe
describe(phone[:, 2])


import matplotlib as mpl
# font_name = mpl.font_manager.FontProperties(fname='c:/windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family='Malgun Gothic')
sj = df.sort_values(['평균'], ascending=[False])
sj.index = sj['이름']
sj['평균'].plot(kind='bar', figsize=(8, 4))