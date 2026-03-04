import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/Users/Maria/OneDrive/Documentos/João A/clientes-v3-preparado.csv')

print(df.head().to_string())

# Histograma
plt.hist(df['salario'])
plt.show()

# Histograma - Parâmetros
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='red', alpha=1)
plt.title('Histograma - Distribuição de salários')
plt.ylabel('Frequência')
plt.xlabel('Salário')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.grid(True)
plt.show()

# Múltiplos Gráficos
plt.figure(figsize=(10,6))
plt.subplot(2,1,1) # 2 Linhas, 1 Coluna, 1ºGráfico

# Gráfico de Dispersão
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salário e Salário')
plt.subplot(1, 2, 2) # 1 linha, 2 colunas, 2º Gráfico
plt.scatter(df['salario'], df['anos_experiencia'], alpha=0.6, s=30)
plt.title('Dispersão - Salario e ano experiencia')
plt.xlabel('Salario')
plt.ylabel('Anos de experiência')

# Mapa calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2,2,3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.tight_layout() # Ajustar espaçamentos
plt.show()




