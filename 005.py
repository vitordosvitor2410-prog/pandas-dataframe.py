import pandas as pd

# 1. Carregar o arquivo CSV (substitua pelo nome real do seu arquivo)
df = pd.read_csv('VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data - VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data copy (cópia).csv')

# 2. Contar o total de carros por empresa
# Opção A: Usando value_counts() (mais direto e prático)
total_por_empresa = df['company'].value_counts()

print("--- Total de Carros por Empresa ---")
print(total_por_empresa)

# Opção B: Usando groupby() (outra forma muito comum)
# total_por_empresa_gb = df.groupby('company').size()
# print(total_por_empresa_gb)