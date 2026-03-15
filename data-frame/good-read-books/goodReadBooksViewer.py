import matplotlib.pyplot as plt
import matplotlib as mat
import tkinter as tk

def mainViewer (df):
   # seleciona os 10 livros mais avaliados
   mostRated = df.sort_values ("ratings_count", ascending = False).head(10).set_index("title")
   mostrarBarhMatplot (mostRated)

# importando paleta de cores variadas
def paletaCores():
   return plt.get_cmap ("tab10").colors

# cria o gráfico de barras horizontal com matplotlib
def mostrarBarhMatplot (df):
   plt.figure (figsize = (10, 6))
   df["ratings_count"].plot (kind = "barh", color = paletaCores())
   plt.xlabel ("Número de Avaliações")
   plt.ylabel ("Livros")
   plt.title ("Top 10 Livros Mais Avaliados")
   plt.gca().invert_yaxis()
   plt.tight_layout()
   plt.show()