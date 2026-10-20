import pandas as pd

# 1. Carregar o arquivo CSV (substitua pelo nome real do seu arquivo)
df = pd.read_csv('VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data - VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data copy (cópia).csv')

# 2. Ordenar todos os carros pela coluna 'price' (em ordem crescente - do mais barato para o mais caro)
carros_ordenados_crescente = df.sort_values(by='price', ascending=True)

print("--- Carros ordenados por preço (Crescente) ---")
print(carros_ordenados_crescente)

# Se preferir ordenar do mais caro para o mais barato (decrescente), basta usar ascending=False:
# carros_ordenados_decrescente = df.sort_values(by='price', ascending=False)
# print(carros_ordenados_decrescente)