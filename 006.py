import pandas as pd

# 1. Carregar o arquivo CSV (substitua pelo nome real do seu arquivo)
df = pd.read_csv('VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data - VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data copy (cópia).csv')

# 2. Encontrar o preço mais alto de cada empresa
carro_mais_alto_por_empresa = df.groupby('company')['price'].max()

print("--- Preço mais alto de cada empresa ---")
print(carro_mais_alto_por_empresa)

# --- Bônus: Se você quiser ver a linha completa (todos os detalhes) do carro mais caro de cada empresa ---
# df_ordenado = df.sort_values('price', ascending=False)
# carro_mais_caro_detalhado = df_ordenado.drop_duplicates(subset=['company'])
# print("\n--- Detalhes do carro mais caro de cada empresa ---")
# print(carro_mais_caro_detalhado)