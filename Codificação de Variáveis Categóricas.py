import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)
df = pd.read_csv('clientes-v2-tratado.csv')

print(df.head())

# Codificação para concatenar
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix= 'estado_civil')], axis=1)

print('\nCodificação one-hot (concatenação)\n', df.head())

# Codificação Ordinal
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós Graduação': 4}
df['Nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print("\nCodificação ordinal para 'nivel_educacao'\n", df.head())

# Transformar 'área de atuação' em categorias usando cat.codes

df['area_atuacao_cod'] = df['area_atuacao'].astype('Category').cat.codes
