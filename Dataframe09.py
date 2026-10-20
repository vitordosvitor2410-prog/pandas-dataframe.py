import pandas as pd

# Criando o dicionário com os dados dos carros
german_cars = {
    'company': ['ford', 'mecedes', 'BMW', 'AUDI'],
    'price': [23845, 135925, 717995, 714600]
}

# Convertendo o dicionário em DataFrame
df_german = pd.DataFrame(german_cars)

# Exibindo o DataFrame
print(df_german)