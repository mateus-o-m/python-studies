import pandas as pd
import kagglehub
path = kagglehub.dataset_download("jealousleopard/goodreadsbooks")

# extração de dados
dfbook = pd.read_csv(f"{path}/books.csv", sep = ",", on_bad_lines = "skip")

print (dfbook.head())
print (dfbook.sample (5))
dfbook.info()

# analizando dados
print ("\n Quantdade de valores nulos: \n",
	dfbook.isnull().sum())
print ("\n Atributos numéricos: \n",
	dfbook.describe())
print ("\n Checagem de linhas duplicadas: \n",
	dfbook [dfbook.duplicated()])
print ("\n Checagem de valores isbn duplicados: \n",
	dfbook [dfbook.duplicated ("isbn")])
print ("\n Checagem de valores isbn13 duplicados: \n",
	dfbook [dfbook.duplicated ("isbn13")])
print ("\n Checagem de valores bookID duplicados: \n",
	dfbook [dfbook.duplicated ("bookID")])
print ("\n Livros com reviews em texto maiores que reviews totais: \n",
	dfbook [dfbook.text_reviews_count > dfbook.ratings_count].shape)
print ("\n Livros sem reviews: \n",
	dfbook [dfbook.ratings_count == 0].shape)
print ("\n Livros com menos de 30 páginas: \n",
	dfbook [dfbook["  num_pages"] < 30].shape)
print ("\n Checagem de títulos e idiomas duplicados: \n",
	dfbook [dfbook.duplicated (["title", "language_code"])].sort_values ("title"))

# limpando dados
print ("\n Estrutura de dados inicial: \n",
	dfbook.info())
dfbook.drop (["isbn", "isbn13", "bookID"], axis = 1, inplace = True)
print ("\n Estrutura de dados após remoção de isbn, isbn13 e bookID: \n", 
	dfbook.info())
dfbook.rename (columns = {"  num_pages":"num_pages"}, inplace = True)
print ("\n Estrutura de dados após correção do texto num_pages: \n", 
	dfbook.info())
dfbook.drop (dfbook [(dfbook.ratings_count == 0) | (dfbook.num_pages < 30)].index, inplace = True)
dfbook.reset_index (drop = True, inplace = True)
print ("\n Estrutura de dados após remoção dos livros sem reviews e com menos de 30 páginas: \n", 
	dfbook.info())

# formatando datas de publicação
invalidDates = []
for index, bookDate in enumerate (dfbook["publication_date"]):
	try:
		pd.to_datetime (bookDate, format = "%d/%m/%Y")
	except ValueError:
		invalidDates.append ((index, bookDate))
dfbook.drop (index = [index for (index, _) in invalidDates], inplace = True)
print ("\n Estrutura de dados após remoção de datas de publicação inválidas: \n", 
	dfbook.info())
dfbook["publication_date"] = pd.to_datetime (dfbook["publication_date"], format = "%d/%m/%Y")
print ("\n Coluna publication_date após formatação: \n", 
	dfbook.publication_date.dt.strftime ("%d/%m/%Y"))

# agrupando dados
aggregDf = dfbook.groupby (["title", "language_code"]).agg ({
	"authors": lambda str: "/".join (set(str)),
	"average_rating": "mean",
	"num_pages": "max",
	"ratings_count": "sum",
	"text_reviews_count": "sum",
	"publication_date": "min",
	"publisher": lambda str: "/".join (set(str))
}).reset_index()
dfbook = aggregDf
print ("\n Dados após agrupamento: \n", 
	dfbook.info())

