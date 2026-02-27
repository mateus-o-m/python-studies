# while (1)
print ("MARKET STOCK")
print ("Digite o número correspondente á ação desejada:")
print ("1. Adcionar novo produto ao estoque.")
print ("2. Exibir total de produtos cadastrados.")
print ("0. Sair do programa")

def addProduct (dicProduct, listStock):
	dicProduct["id"] = 5
	dicProduct["name"] = str (input("Digite o nome do produto: "))
	dicProduct["price"] = float (input("Digite o valor de {dicProduct['name']}:"))
	dicProduct["amount"] = int (input("DIgite a quantidade de {dicProduct['name']}:"))
	listStock.append(dicProduct)

def countProduct (listStock):
	productAmount = []
	for name in listStock:
		countVar = 0
		# countVar = countVar + listStock[listStock.index(name)]
		dicVar = {"name": listStock["name"], "amount": listStcock["amount"]}
		productAmount.append (dicVar)
	return productAmount

# main()
products = {"name": "nome", "id": 0, "price": 0.0, "amount": 0}
marketStock = []
# print (type(products))

addProduct (products, marketStock)
print (countProduct (marketStock))

print (marketStock)