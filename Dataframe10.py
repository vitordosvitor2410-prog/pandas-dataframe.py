import pandas as pd

# Criando o dicionário com os dados
dados = {
    'company': ['toyota', 'HONDA', 'nissan', 'mitsubishi'], 
    'price': [29995, 23600, 61500, 58900]
}

# Convertendo em DataFrame do Pandas
df = pd.DataFrame(dados)

# Exibindo o DataFrame
print(df)