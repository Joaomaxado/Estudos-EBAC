import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Nome': ['Alice', 'Joao', 'Charlie', 'David', 'Eva', 'Diego', 'Denize', 'Claudio'],
    'Idade': [25, 30, 35, 40, 45, 60, 22, 24],
    'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Médico','Engenheiro', 'Estudante','Estudante'],
    'Salário': ['4500', '8000', '5000', '10000', '12000','15000', '1200','1500'],
    'Limite_Credito': ['2500', '4000', '4000', '1000', '10000','2000', '500','250'],
    'Historico_Inadimplencia': ['0', '0', '0', '1', '0','1', '0','1'],
    'Estado_Civil': ['Casamento', 'Casamento', 'Solteiro', 'Solteiro', 'Casamento','Solteiro', 'Solteiro','Solteiro'],
    'Imovel_Proprio': ['0', '0', '0', '1', '1','1', '0','0']
}

df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)
print(df)

# Pessoas com idade avançada possuem salários maiores. Isso se dá ao fato da experiência adiquirida.
# Gráfico de barra
plt.figure(figsize=(6,6))

plt.bar(df['Salário'], df['Idade'], label='Idade', color='skyblue')
plt.ylabel('Idade')
plt.xlabel('Salário')
plt.title('Impacto da idade no salário')
plt.grid(True, linestyle='-')
plt.show()


# Gráfico de dispersão
# Porém, inadimplentes não conseguem crédito alto independente do seu salário.
df['Historico_Inadimplencia'] = df['Historico_Inadimplencia'].astype(int)
df['Limite_Credito'] = df['Limite_Credito'].astype(float)
df['Saário'] = df['Salário'].astype(float)
# Converti todos as strings para float e inte para que o código flua melhor.

em_dia = df[df['Historico_Inadimplencia'] == 0]
ina = df[df['Historico_Inadimplencia']== 1]
# Filtrei os indadimplentes dos que estão em dia

plt.figure(figsize=(6,6))

# Pontos de quem está em dia
plt.scatter(em_dia['Salário'], em_dia['Limite_Credito'], label='Em dia')

# Ponto de quem não está em dia
plt.scatter(ina['Salário'], ina['Limite_Credito'], color='red', label='Inadimplente', marker='X')
plt.title('O impacto de ser inadimplente no limite de crédito')
plt.xlabel('Salário')
plt.ylabel('Limite Credito')
plt.legend(title='Status financeiro')
plt.grid(True, linestyle='-')
plt.annotate(

  'Inadimplencia influencia no\nno crédito baixo',

  xy=(15000, 2000),    # ponto que será destacado

  xytext=(15000, 3625),   # posição do texto

  arrowprops=dict(facecolor='black', arrowstyle='->')

)
plt.show()




