
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

import matplotlib as mpl
font_name = mpl.font_manager.FontProperties(fname='c:/windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)
sj = df.sort_values(['평균'], ascending=[False])
sj.index = sj['이름']
sj['평균'].plot(kind='bar', figsize=(8, 4))

# 성적 비교 - 어느 반이 잘했나?
ban1 = df[df['반']==1]
ban2 = df[df['반']==2]
ban1_mean = ban1['총점'].sum()/(6*4)
ban2_mean = ban2['총점'].sum()/(6*4)
print(ban1_mean, ban2_mean)

# 두 집단 간의 평균은 유의미한 차이 나는가? (t검증)
# p-value 값이 0.005 이하일 때 차이가 난다고 할 수 있음
import scipy.stats as stats
result = stats.ttest_ind(ban1['평균'], ban2['평균'])
print(result)


# 과목별 평균은 유의미하게 차이가 나는가? (t검증)
for sub in subj:
  print(sub, stats.ttest_ind(ban1[sub], ban2[sub]))

# 전체 성적데이터에 대한 그래프 출력
sj.plot(kind='bar', figsize=(10, 6))
# 과목별 점수 분포 - 박스수염 그래프 출력
df[subj].boxplot(return_type='axes')
# 1반, 2반 과목별 점수 분포
ban1[subj].boxplot(return_type='axes')
ban2[subj].boxplot(return_type='axes')


# 과목별 상관관계 - '수학 : 과학'과 '국어 : 영어'
df.plot(kind='scatter', x='수학', y='과학')
print(stats.pearsonr(df['수학'], df['과학'])) # 피어슨 상관계수
df.plot(kind='scatter', x='수학', y='영어')
print(stats.pearsonr(df['수학'], df['영어']))
df.plot(kind='scatter', x='수학', y='국어')
print(stats.pearsonr(df['수학'], df['국어']))
df.plot(kind='scatter', x='국어', y='영어')
print(stats.pearsonr(df['국어'], df['영어']))
df.plot(kind='scatter', x='국어', y='과학')
print(stats.pearsonr(df['국어'], df['과학']))
df.plot(kind='scatter', x='과학', y='영어')
print(stats.pearsonr(df['과학'], df['영어']))
