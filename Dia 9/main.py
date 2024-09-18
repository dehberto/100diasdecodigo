import pandas as pd
import numpy as np

data = {'vendas:': [100, 200, 300, 400, 500, 600, 700, 800, 900, 100]}
df = pd.DataFrame(data)


#operações
media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()

# Resultados
print("Média:" , media)
print("Mediana:" , mediana)
print("Desvio Padrão:" , desvio_padrao)
print("Máximo:" , maximo)
print("Minimo:" , minimo)