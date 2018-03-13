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


# DataFrame 객체 생성 : { 'key' : ['val', 'val', ...]}
data = {'이름' : ['수지', '혜교', '지현'],
        '국어' : [99, 98, 88], '영어' : [98, 89, 94], '수학' : [78, 99, 87]}
sj = pd.DataFrame(data, columns=['이름', '국어', '영어', '수학'])
print(sj)
print(sj['이름']) # 특정 칼럼만 보기

# Series : 1차원 자료구조, df에서 특정 칼럼 추출시 Series 생성
data = [4, 5, 6, 7, 8, 9, 10]
print(data) # 그냥 1차원 배열
print(pd.Series(data)) # 행번호가 있는 다차원 배열

name = ['수지', '혜교', '지현']
kor = [99, 98, 88]
eng = [98, 89, 94]
mat = [78, 99, 87]

data = { '이름' : name, '국어' : kor, '영어' : eng, '수학' : mat}
sj = pd.DataFrame(data, columns=['이름', '국어', '영어', '수학'])
print(sj)

gender = pd.Series(['남', '여', '여'])
sj['성별'] = gender
print(sj)

# dataframe 행/열 삭제
sj = sj.drop(0, axis=0) # 0,0 삭제
print(sj)
sj = sj.drop('성별', axis=1) # 성별 열 삭제
print(sj)


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %matplotlib inline # 주피터 노트북 없이도 그릴 수 있게 해줌
data = np.arange(10)
plt.plot(data)
plt.show()

# 산점도 - 100의 표준정규분포 난수 생성
list = []
for i in range(100) :
  x = np.random.normal(0, 1)
  y = x + np.random.normal(0, 1)
  list.append([x, y])
x_data = [v[0] for v in list]
y_data = [v[1] for v in list]

plt.plot(x_data, y_data, 'ro')
plt.show()