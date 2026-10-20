import pandas as pd

# 1. Criando o primeiro dicionário (ex: preços)
dicionario_preco = {
    'company': ['toyota', 'HONDA', 'nissan', 'mitsubishi'],
    'price': [29995, 23600, 61500, 58900]
}

# 2. Criando o segundo dicionário (ex: cavalos de potência / horsepower)
dicionario_potencia = {
    'company': ['toyota', 'HONDA', 'nissan', 'mitsubishi'],
    'horsepower': [141, 130, 150, 160]
}

# Convertendo os dicionários em DataFrames
df_preco = pd.DataFrame(dicionario_preco)
df_potencia = pd.DataFrame(dicionario_potencia)

# 3. Combinando os dois DataFrames usando a coluna 'company' como condição/chave
df_combinado = pd.merge(df_preco, df_potencia, on='company')

print("--- DataFrame Combinado (Merge) ---")
print(df_combinado)