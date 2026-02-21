import pandas as pd

dataframe = pd.read_csv("dados_populacionais_1000_linhas.csv")

# visualise first lines
print (dataframe.head())

# structure
dataframe.info()

# imprting matplotlib with the pyplot module
import matplotlib.pyplot as plt

# counts faixas etárias, and plots faria_etaria x quantity of them
dataframe["faixa_etaria"].value_counts().plot(kind = "bar")

# show graphicaly
plt.title ("Distribuição por faixa etária")
plt.xlabel ("Faixa Etária")
plt.ylabel ("Quantidade")
plt.show()

# top 5 careers
dataframe["profissao"].value_counts().head(5).plot(kind = "barh")

plt.title ("Profissões mais populares")
plt.ylabel ("Profissão")
plt.xlabel ("Quantidade")
plt.show()

# career per state distribuction
dataframe["estado"].value_counts().plot(kind = "pie", autopct='%1.1f%%')

plt.title ("Quantidade de emprego po estado")
plt.xlabel ("")
plt.ylabel ("")
plt.show()