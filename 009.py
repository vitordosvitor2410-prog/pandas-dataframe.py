import pandas as pd

# Dicionários do Exercício 9
german_cars = {
    'company': ['ford', 'mecedes', 'BMW', 'AUDI'], 
    'price': [23845, 135925, 717995, 714600]
}

japanese_cars = {
    'company': ['toyota', 'HONDA', 'nissan', 'mitsubishi'], 
    'price': [29995, 23600, 61500, 58900]
}

# Criando os DataFrames
df_german = pd.DataFrame(german_cars)
df_japanese = pd.DataFrame(japanese_cars)

# Concatenando
df_concatenado = pd.concat([df_german, df_japanese], ignore_index=True)

print("--- Exercício 9: DataFrame Concatenado ---")
print(df_concatenado)