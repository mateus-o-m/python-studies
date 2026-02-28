def menu (listStock):
	id = 1
	while (1):
		print ("1. Adcionar novo produto ao estoque.")
		print ("2. Exibir total de produtos cadastrados.")
		print ("0. Sair do programa")
		menuOption = int (input("Digite o número correspondente á ação desejada: "))
		if menuOption == 1:
			addProduct (listStock, id)
			id += 1
		elif menuOption == 2:
			countProduct (listStock)
		elif menuOption == 0:
			break

def addProduct (listStock, idProduct):
	dicProduct = {}
	dicProduct["name"] = str (input("Digite o nome do produto: "))
	for product in listStock:
		if product["name"] == dicProduct["name"]:
			print ("Produto já cadastrado. Utilize os campos abaixo para editar o produto.\nSe não forem preenchidos, o valor atual será matido")
			dicProduct["price"] = float (input(f"Atualizar o valor de {dicProduct['name']}, valor atual {dicProduct['price']}: "))
			dicProduct["amount"] += int (input(f"Atualizar a quantidade de {dicProduct['name']}, quantidade atual {dicProduct['amount']}:"))
			listStock.append (dicProduct)
		return
	dicProduct["id"] = idProduct
	dicProduct["price"] = float (input(f"Digite o valor de {dicProduct['name']}: "))
	dicProduct["amount"] = int (input(f"DIgite a quantidade de {dicProduct['name']}: "))
	listStock.append (dicProduct)

def countProduct (listStock):
	countVar = 0
	productAmount = []
	for product in listStock:
		countVar += product["amount"]
		dicVar = {"name": product["name"], "amount": product["amount"]}
		productAmount.append (dicVar)
	return productAmount

# main()
marketStock = []

print ("========== MARKET STOCK ==========")
menu (products, marketStock)

print (marketStock)

# print (marketStock[0])