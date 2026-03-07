import pandas as pd
import kagglehub
path = kagglehub.dataset_download("jealousleopard/goodreadsbooks")

# extração de dados
dfbook = pd.read_csv(f"{path}/books.csv", sep = ",", on_bad_lines = "skip")

print (dfbook.head())
print (dfbook.sample (5))
dfbook.info()

# analisando dados
print ("\n Quantity of null values: \n",
	dfbook.isnull().sum())
print ("\n Numeric statistics atributes: \n",
	dfbook.describe())
print ("\n Duplicated lines check: \n",
	dfbook [dfbook.duplicated()])
print ("\n Duplicated isbn values check: \n",
	dfbook [dfbook.duplicated ("isbn")])
print ("\n Duplicated isbn13 values check: \n",
	dfbook [dfbook.duplicated ("isbn13")])
print ("\n Duplicated bookID values check: \n",
	dfbook [dfbook.duplicated ("bookID")])
print ("\n Books with text review counts higher than rating counts \n",
	dfbook [dfbook.text_reviews_count > dfbook.ratings_count].shape)
print ("\n Books with no reviews: \n",
	dfbook [dfbook.ratings_count == 0].shape)
print ("\n Books with less than 30 pages: \n",
	dfbook [dfbook["  num_pages"] < 30].shape)
print ("\n Duplicated titles and language: \n",
	dfbook [dfbook.duplicated (["title", "language_code"])].sort_values ("title"))

# limpando dados
print ("\n Original data frame structure: \n",
	dfbook.info())
dfbook.drop (["isbn", "isbn13", "bookID"], axis = 1, inplace = True)
print ("\n Data frame after isbn, isbn13 and bookID removal: \n", 
	dfbook.info())
dfbook.rename (columns = {"  num_pages":"num_pages"}, inplace = True)
print ("\n Data frame after num_pages rename: \n", 
	dfbook.info())
dfbook.drop (dfbook [(dfbook.ratings_count == 0) | (dfbook.num_pages < 30)].index, inplace = True)
dfbook.reset_index(drop = True, inplace = True)
print ("\n Data frame after ratings_count == 0 and num_pages < 30 removal: \n", 
	dfbook.info())

# formatando datas de publicação
invalidDates = []
for index, bookDate in enumerate (dfbook["publication_date"]):
	try:
		pd.to_datetime (bookDate, format = "%d/%m/%Y")
	except ValueError:
		invalidDates.append((index, bookDate))
dfbook.drop (index = [index for (index, _) in invalidDates], inplace = True)
print ("\n Data frame after invalid dates removal: \n", 
	dfbook.info())
dfbook["publication_date"] = pd.to_datetime (dfbook["publication_date"], format = "%d/%m/%Y")
print ("\n publication_date column after formating: \n", 
	dfbook.publication_date.dt.strftime("%d/%m/%Y"))
# grouping 