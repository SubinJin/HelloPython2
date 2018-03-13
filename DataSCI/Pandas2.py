
# 판다스 - 데이터 가공
# 데이터 취득 및 가공
import numpy as np
import pandas as pd
# 데이터 읽어 들이기 - GAP_5year.csv
gap = pd.read_csv('C:/Bigdata/R3/GAP_5year.tsv', sep='\t')
print(gap) # 많은 내용을 출력하기에 다소 불편
print( gap.head() ) # 위에서 5줄
print( gap.tail() ) # 아래에서 5줄
print( gap.info() ) # 데이터 구조 표시
print( gap.describe() ) # 기술통계 요약
print('')
# 데이터 조회
# R dplyr - filter(gap, country == '' & year == )
kor = gap.query("country == 'Korea, Rep.'") # 통계자료에서 2007년 한국 데이터 조회
print(kor)
kor = gap.query("country == 'Korea, Rep.' & year == 2007")
print(kor)
# 정렬해서 출력
# year, country 순으로 정렬 후 출력
# R dplyr - gap %>% arrange(year, country)
sort = gap.sort_values(by = ['year', 'country'])
print(sort.head())
# 부분열 선택하기
# 인구수, 1인당 GDP를 출력
# R dplyr - gap %>% select(pop, gdpPercap)
partcol = gap[['pop', 'gdpPercap']]
print(partcol)
print(partcol.head())
# 특정열 추가하기
# 총 GDP : pop(인구수) * gdpPercap(1인당 GDP)
# GDP 증가율(gdp_ratio) : lifeExp / gdpPercap
# GDP 증가비(%)(gdp_perc) : gdp_ratio * 100
gap['gdp'] = gap['pop'] * gap['gdpPercap']
gap['gdp_ratio'] = gap['lifeExp'] * gap['gdpPercap']
gap['gdp_perc'] = gap['gdp_ratio'] * 100
print(gap.head())
# 통계량 계산하기
print(gap.aggregate(['mean', 'median', 'mode']))
print(gap.agg(['sum', 'min', 'max']))
# 표본 추출을 위한 샘플링 : sample()
np.random.seed(9790)
print( gap.sample(n = 10) )

print(gap.year)
print(gap.year.unique())
print(gap.drop_duplicates(['country', 'year']).head())

# group by 연산
# 2007년 기준 대륙별 생활지수 평균값 분석
gap.query("year==2007").groupby('continent').agg({'lifeExp' : 'mean'})