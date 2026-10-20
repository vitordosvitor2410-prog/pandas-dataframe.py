import pandas as pd

# 1. Carregar o arquivo CSV (substitua pelo nome real do seu arquivo)
df = pd.read_csv('VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data - VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data copy (cópia).csv')

# 2. Encontrar a montadora com o carro mais caro
# Opção A: Se você quiser apenas a linha do carro com o maior preço absoluto
carro_mais_caro = df.loc[df['price'].idxmax()]
montadora_mais_cara = carro_mais_caro['company']
preco_mais_caro = carro_mais_caro['price']

print(f"A montadora com o carro mais caro é: {montadora_mais_cara} (Preço: {preco_mais_caro})")

# Opção B: Se a tabela tiver vários carros por montadora e você quiser a média ou o maior preço por empresa:
# montadora_mais_cara = df.groupby('company')['price'].max().idxmax()
# print(f"A montadora com o preço máximo mais alto é: {montadora_mais_cara}")