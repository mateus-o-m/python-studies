from goodReadBooksViewer import mainViewer
import pandas as pd
import kagglehub

path = kagglehub.dataset_download("jealousleopard/goodreadsbooks")

def printOnConsole (str, func):
	print ("\n", str, "\n", func)

# extração de dados
dfbook = pd.read_csv(f"{path}/books.csv", sep = ",", on_bad_lines = "skip")

print (dfbook.head())
print (dfbook.sample (5))
dfbook.info()

# analisando dados
printOnConsole ("Quantdade de valores nulos:", dfbook.isnull().sum())
printOnConsole ("Atributos numéricos:", dfbook.describe())
printOnConsole ("Checagem de linhas duplicadas:", dfbook [dfbook.duplicated()])
printOnConsole ("Checagem de valores isbn duplicados:", dfbook [dfbook.duplicated ("isbn")])
printOnConsole ("Checagem de valores isbn13 duplicados:", dfbook [dfbook.duplicated ("isbn13")])
printOnConsole ("Checagem de valores bookID duplicados:", dfbook [dfbook.duplicated ("bookID")])
printOnConsole ("Livros com reviews em texto maiores que reviews totais:",
	dfbook [dfbook.text_reviews_count > dfbook.ratings_count].shape)
printOnConsole ("Livros sem reviews:", dfbook [dfbook.ratings_count == 0].shape)
printOnConsole ("Livros com menos de 30 páginas:", dfbook [dfbook["  num_pages"] < 30].shape)
printOnConsole ("Checagem de títulos e idiomas duplicados:",
	dfbook [dfbook.duplicated (["title", "language_code"])].sort_values ("title"))

# limpando dados
printOnConsole ("Estrutura de dados inicial:", dfbook.info())

dfbook.drop (["isbn", "isbn13", "bookID"], axis = 1, inplace = True)
printOnConsole ("Estrutura de dados após remoção de isbn, isbn13 e bookID:", dfbook.info())

dfbook.rename (columns = {"  num_pages":"num_pages"}, inplace = True)
printOnConsole ("Estrutura de dados após correção do texto num_pages:", dfbook.info())

dfbook.drop (dfbook [(dfbook.ratings_count == 0) | (dfbook.num_pages < 30)].index, inplace = True)
dfbook.reset_index (drop = True, inplace = True)
printOnConsole ("Estrutura de dados após remoção dos livros sem reviews e com menos de 30 páginas:",
	dfbook.info())

# formatando datas de publicação
invalidDates = []
for index, bookDate in enumerate (dfbook["publication_date"]):
	try:
		pd.to_datetime (bookDate, format = "%d/%m/%Y")
	except ValueError:
		invalidDates.append ((index, bookDate))
dfbook.drop (index = [index for (index, _) in invalidDates], inplace = True)
printOnConsole ("Estrutura de dados após remoção de datas de publicação inválidas:", dfbook.info())

dfbook["publication_date"] = pd.to_datetime (dfbook["publication_date"], format = "%d/%m/%Y")
printOnConsole ("Coluna publication_date após formatação:",
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
printOnConsole ("Dados após agrupamento:", dfbook.info())

mainViewer (dfbook)