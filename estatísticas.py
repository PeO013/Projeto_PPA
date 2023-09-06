# Importar as bibliotecas necessárias
import json
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo JSON
with open('respostas.json', 'r') as f:
    data = json.load(f)

# Converter o JSON em um DataFrame do pandas
df = pd.DataFrame(data)

# Gerar estatísticas sobre as respostas
print(df.describe())

# Procurar correlações entre os dados
corr = df.corr()
print(corr)

# Gerar um gráfico com as respostas
df.plot(kind='bar')
plt.show()

