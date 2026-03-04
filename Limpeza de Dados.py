from operator import index
import pandas as pd

base = pd.read_csv('C:/Users/Maria/OneDrive/Documentos/João A/clientes.csv')

# Remover Dados
base.drop('pais', axis=1, inplace=True)
base.drop(2, axis=0, inplace=True)

# Normalizar campos de texto
base['Nome'] = base['nome'].str.title()
base['endereco'] = base['endereco'].str.lower()
base['estado'] = base['estado'].str.upper()

# Tratar valores nulos (Ausentes)
base.fillna (0)    # Substituir valores nulos por 0
base.dropna ()   # Remover registro com valores nulos
base.dropna(thresh=4)   # Manter registro com no mínimo 4 valores não nulos
base.dropna(subset=['cpf'])   # Remover registro com CPF nulo

base['idade corrigida'] = base['idade'].fillna(base['idade'].mean())

# Tratar formato de dados
base['data corrigida'] = pd.to_datetime(base['data'], format='%d/%m/%y', errors='coerce')

print('Quantidade de registros atuais:', base.shape[0])
base.drop_duplicates()
print('Valores nulos:', base.isnull().sum())
print(base.head())

base_salvar = base[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
base_salvar.to_csv('Clientes_limpeza.csv', index=False)

print('Novo data frame: \n', pd.read_csv('Clientes_limpeza.csv'))