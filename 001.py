#Exercício 1: A partir do conjuto de dados fornecido imprima as cinco primeira  e as ultima linhas.
import pandas as pd

# 1. Carregue a sua planilha (exemplo com CSV ou Excel)
df = pd.read_csv('VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data - VICTOR EMANUEL OLIVEIRA DA SILVA - Automobile_data copy (cópia).csv')
# ou para Excel: df = pd.read_excel('sua_planilha.xlsx')

# 2. Exiba as 5 primeiras linhas
print(df.head())