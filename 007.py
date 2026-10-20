import pandas as pd

# 1. Carregar o arquivo CSV (substitua pelo nome real do seu arquivo)
df = pd.read_csv('VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data - VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data copy (cópia).csv')

# 2. Calcular a quilometragem média de cada fabricante
# Nota: Substitua 'average-mileage' pelo nome exato da coluna de quilometragem na sua planilha (ex: 'mileage', 'km')
quilometragem_media = df.groupby('company')['average-mileage'].mean()

print("--- Quilometragem Média por Fabricante ---")
print(quilometragem_media)