import pandas as pd

df = pd.read_csv('C:/Users/Maria/OneDrive/Documentos/João A/clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())

print(df.info())
print('Análise de dados nulos \n', df.isnull().sum()) # .isnull e .sum faz a conta dos dados ausentes
df.dropna(inplace=True)
print('Confirmar remoção de dados nulos \n', df.isnull().sum().sum())

print('Análise de dados duplicados \n', df.duplicated().sum())

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('Clientes-v2-tratado.csv', index=False)


