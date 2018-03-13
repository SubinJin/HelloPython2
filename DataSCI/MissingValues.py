import numpy as np
import pandas as pd

# 난수를 이용해서 5*3 데이터프레임 생성
df = pd.DataFrame(np.random.rand(5, 3), columns = ['col1', 'col2', 'col3'])
print(df)
# 결측치 삽입
df.ix[0, 0]
df.ix[1, ['col1', 'col3']] = np.nan
df.ix[2, 'col2'] = np.nan
df.ix[3, 'col3'] = np.nan
df.ix[4, 'col4'] = np.nan
df.ix[5, 'col5'] = np.nan
# 결측치 해결 1 - fillna를 이용 : 0으로 채움
df0 = df.fillna(0)
print(df0)

# 결측치 해결 2 - fillna를 이용 : 문자열로 채움
dfs = df.fillna('결측')
# dfs = df.fillna('miss')
print(dfs)

# 결측치 해결 3 - fillna를 이용 : 평균값으로 채움
df_mean = df.mean()
dfm = df.fillna(df_mean)
print(dfm)