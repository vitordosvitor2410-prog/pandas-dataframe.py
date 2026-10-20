import pandas as pd

# 1. Carregar o arquivo CSV original
df = pd.read_csv('VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data - VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data copy (cópia).csv')

# 2. Limpeza dos dados:
# Substitui textos indesejados (como '?', 'n.a', 'NaN') por valores nulos reconhecidos pelo Pandas
df = df.replace(['?', 'n.a', 'NaN'], None)

# Opção A: Remover todas as linhas que contenham dados nulos (mais comum)
df_limpo = df.dropna()

# Opção B: Preencher valores nulos em colunas específicas (exemplo: preço zerado ou média)
# df['price'] = df['price'].fillna(0)

# 3. Atualizar o arquivo CSV com os dados limpos
df_limpo.to_csv('seu_arquivo.csv', index=False)

print("Conjunto de dados limpo e arquivo CSV atualizado com sucesso!")
print(df_limpo.head())