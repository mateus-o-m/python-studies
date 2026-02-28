# Mateus Oliveira, PTI Práticas de programação

# manu com acesso a todas as funções do programa, utiliza uma lista como entrada
def menu (listStock):
	id = 1
	options = """1. ADICIONAR PRODUTO	2. EXIBIR QUANTIDADE TOTAL	0. SAIR DO PROGRAMA"""
	while (1):
		print ("\n=---------------------------------=MENU=----------------------------------=")
		print (options)
		menuOption = verifyInput (int, "Digite o número correspondente á ação desejada: ",)
		if menuOption == 1:
			subMenu (lambda: addProduct (listStock, id)) # criando uma função anônima de addProduct, para ser usada em subMenu
			viewStock (listStock)
		elif menuOption == 2:
			viewStockAmount (listStock)
		elif menuOption == 0:
			print ("Finalizando programa.")
			break
		else:
			print ("Tente novamente.")

def subMenu (function):
	function()
	while (1):
		keepGoing = verifyInput(int, "Deseja continuar fazendo?\n1. SIM\t2. NÃO\n==> ",)
		if keepGoing == 1:
			function()
		elif keepGoing == 2:
			break
		else:
			print ("Digite uma opção válida")

# verifica input de diferentes tipos numéricos, utiliza mensagens personalizadas, e suporta entradas vazias
# verifica também se o número é positivo
def verifyInput (dataType, messageString, default = None):
	print (messageString, end = "")
	while (1):
		inputAux = input().strip() # espaços em branco não serão considerados
		if inputAux == "" and default is not None: # suporte á entradas vazias
			return default
		try:
			value = dataType (inputAux)
			if value >= 0:
				return value
			print ("Somente números positivos: ", end = "")
		except ValueError:
			print ("Entrada inválida. Digite um número válido: ", end = "")

# adiciona produtos(dicionário) ao estoque(lista)
def addProduct (listStock, idProduct):
	print ("\n1. ADICIONAR PRODUTO")
	name = str (input("Digite o nome do produto: ").lower()) # padroniza em letras minúsculas a entrada
	for product in listStock:
		idProduct += 1
		if product["name"] == name:
			print (f"{name} já cadastrado. Pressione enter para manter os valores atuais.")
			# instruções abaixo atualizam os valores de "price" e "amount", se o usuário desejar
			product["price"] = verifyInput (float, f"Preço atual R${product['price']:.2f}, digite novo preço: R$ ", product["price"])
			product["amount"] = verifyInput (int, f"Quantidade atual {product['amount']}, digite nova quantidade: ", product["amount"])
			return # recurso para sair da função, após atualização(ou não) dos valores
	# criação do dicionário
	dicProduct = {"name": name, "id": idProduct,
		"price": verifyInput (float, f"Digite o valor de {name}: R$ ",),
		"amount": verifyInput (int, f"DIgite a quantidade de {name}: ",)}
	listStock.append (dicProduct) # inclusão do dicionário

# visualização formatada do estoque
def viewStock (listStock):
	print ("\nPRODUTOS CADASTRADOS")
	# as informações de cada produto (id, nome, preço e quantidade) fazem parte de um índice único para cada um
	# e cada indice representa o dicionário de um respectivo produto, sendo possível acessar o par (chave: valor) individualmente
	for product in listStock:
		print (f"ID: {product['id']}   PRODUTO: {product['name']}   PREÇO: R${product['price']:.2f}   QUANTIDADE: {product['amount']}")

# visualização do quantidade de cada produto e da quantidade total presente no estoque
def viewStockAmount (listStock):
	if listStock == []:
		print ("\nNÃO HÁ PRODUTOS CADASTRADOS")
		return
	print ("\n2. QUANTIDADE DE PRODUTOS")
	countVar = 0
	for product in listStock:
		countVar += product["amount"]
		print (f"PRODUTO: {product['name']}   QUANTIDADE: {product['amount']}")
	print (f"\tQUANTIDADE TOTAL: {countVar}")

# função main()
marketStock = []
print ("\t\t============== MARKET STOCK ==============")
menu (marketStock)