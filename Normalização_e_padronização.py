import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('Clientes-v2-tratado.csv')

print(df.head())

df = df[['idade', 'salario']]

# Normalização MinMaxSacaler

scaler = MinMaxScaler()
df['IdadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['SalarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

print('MinMaxScaler: \n', df.head())

# Padronização StandardScaler

scaler = StandardScaler()
df['IdadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['SalarioStandardScaler'] = scaler.fit_transform(df[['salario']])

print('StandardScaler: \n', df.head())

# Padronização RobustScaler
scaler = RobustScaler()
df['IdadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['SalarioRobustScaler'] = scaler.fit_transform(df[['salario']])

