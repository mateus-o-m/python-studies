def verifyInput (dataType, messageString): # verifica input de diferentes tipos numéricos, com uma mensagem personalizada
	while (1):
		value = dataType (input(messageString))
		if value == ""
			return
		try:
			value > 0
			return value
		except ValueError:
			print ("Entrada inválida. Digite um número válido.")

def menu (listStock):
	id = 1
	options = """
		1. Adcionar novo produto ao estoque.
		2. Exibir total de produtos cadastrados.
		0. Sair do programa
		"""
	while (1):
		print (options)
		menuOption = verifyInput (int, "Digite o número correspondente á ação desejada: ")
		if menuOption == 1:
			addProduct (listStock, id)
			id += 1
		elif menuOption == 2:
			print (countProduct(listStock)
		elif menuOption == 0:
			break

def addProduct (listStock, idProduct):
	name = str (input("Digite o nome do produto: ").lower())
	for product in listStock:
		if product["name"] == dicProduct["name"]:
			print (f"{dicProduct['name']} já cadastrado")
			dicProduct["price"] = verifyInput (float, f"Preço atual {dicProduct['price']}, digite novo preço: ")
			dicProduct["amount"] = verifyInput (int, f"Quantidade atual {dicProduct['amount']}, digite nova quantidade")
		return
	dicProduct = {"name": name, "id": idProduct,
		"price": verifyInput (float, f"Digite o valor de {dicProduct['name']}: "),
		"amount": verifyInput (int, f"DIgite a quantidade de {dicProduct['name']}: ")}
	listStock.append (dicProduct)

def countProduct (listStock):
	countVar = ;0
	productAmount = []
	for product in listStock:
		countVar += product["amount"]
		dicVar = {"name": product["name"], "amount": product["amount"]}
		productAmount.append (dicVar)
	return productAmount

# main()
marketStock = []
print ("========== MARKET STOCK ==========")
menu (marketStock)