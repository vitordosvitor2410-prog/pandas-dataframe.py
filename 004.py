import pandas as pd

# 1. Carregar o arquivo CSV (substitua pelo nome real do seu arquivo)
df = pd.read_csv('VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data - VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data copy (cópia).csv')

# 2. Filtrar apenas os carros da Toyota
# Nota: Certifique-se de que o nome da coluna de empresa seja 'company' 
# e que os valores estejam em minúsculas ou maiúsculas conforme a sua base de dados.
carros_toyota = df[df['company'].str.lower() == 'toyota']

# 3. Imprimir todos os detalhes
print("--- Detalhes dos Carros da Toyota ---")
print(carros_toyota)