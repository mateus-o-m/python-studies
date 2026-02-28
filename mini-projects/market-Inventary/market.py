# Mateus Oliveira, PTI Práticas de programação

# verifica input de diferentes tipos numéricos, utiliza mensagens personalizadas
# suporta entradas vazias, verifica se o número digitado é positivo
def verifyInput (dataType, messageString, default = None):
	print (messageString, end = "")
	while (1):
		inputAux = input().strip() # espaços em branco não serão considerados
		if inputAux == "" and default is not None: # suporte á entradas vazias
			return default # retorna valor nulo
		try:
			value = dataType (inputAux)
			if value >= 0:
				return value
			print ("Somente números positivos: ", end = "")
		except ValueError:
			print ("Entrada inválida. Digite um número válido: ", end = "")

# menu com acesso a todas as funções do programa, utiliza uma lista como entrada
def menu (listStock):
	id = 1
	while (1):
		print ("\n=---------------------------------=MENU=----------------------------------=")
		print ("""1. ADICIONAR PRODUTO	2. EXIBIR QUANTIDADE TOTAL	0. SAIR DO PROGRAMA""")
		menuOption = verifyInput (int, "Digite o número correspondente á ação desejada: ",)
		# lambda: cria uma função anônima para ser usada por outra função,
		# funciona como um atalho da função
		functions = {1: (lambda: subMenu (lambda: addProduct (listStock, id))),
		2: (lambda: viewStockAmount (listStock))}
		if menuOption == 0:
			print ("Finalizando programa.")
			break
		elif menuOption in functions:
			functions [menuOption]()
		else:
			print ("Opção inválida.")
			continue
		if menuOption != 2: # apenas se a função exibir quantidade não for chamada
			viewStock (listStock)

def subMenu (function):
	function()
	while (1):
		keepGoing = verifyInput (int, "Deseja continuar fazendo?\n1. SIM\t2. NÃO\n==> ",)
		if keepGoing == 1:
			function()
		elif keepGoing == 2:
			break
		else:
			print ("Digite uma opção válida")

# adiciona produtos(dicionário) ao estoque(lista)
def addProduct (listStock, idProduct):
	print ("\n1. ADICIONAR PRODUTO")
	name = str (input("Digite o nome do produto: ").lower()) # padroniza em letras minúsculas a entrada
	for product in listStock:
		idProduct += 1 # id único para cada produto(índice) no estoque(lista)
		if product["name"] == name:
			print (f"{name} já cadastrado. Pressione enter para manter os valores atuais.")
			# instruções abaixo atualizam os valores de "price" e "amount", se o usuário desejar
			product["price"] = verifyInput (float,
			f"Preço atual R${product['price']:.2f}, digite novo preço(und): R$ ", product["price"])
			product["amount"] = verifyInput (int,
			f"Quantidade atual {product['amount']}, digite nova quantidade: ", product["amount"])
			return # recurso para sair da função, após atualização(ou não) dos valores
	# criação do dicionário
	dicProduct = {"name": name, "id": idProduct,
		"price": verifyInput (float, f"Digite o preço unitário de {name}: R$ ",),
		"amount": verifyInput (int, f"DIgite a quantidade de {name}: ",)}
	listStock.append (dicProduct) # inclusão do dicionário

# visualização formatada do estoque
def viewStock (listStock):
	if listStock == []:
		return # recurso caso não haja produtos cadastrados
	print ("\nPRODUTOS CADASTRADOS")
	# as informações de cada produto (id, nome, preço e quantidade) fazem parte de um índice único para cada um
	# e cada indice representa o dicionário de um respectivo produto, sendo possível acessar o par (chave: valor) individualmente
	for product in listStock:
		print (f"(ID {product['id']}) {product['name']}  PREÇO(UND) R${product['price']:.2f}  QUANTIDADE {product['amount']}")

# visualização do quantidade de cada produto e da quantidade total presente no estoque
def viewStockAmount (listStock):
	if listStock == []:
		print ("\nNÃO HÁ PRODUTOS CADASTRADOS")
		return
	print ("\n2. QUANTIDADE DE PRODUTOS")
	countAux = 0
	for product in listStock:
		countAux += product["amount"]
		print (f"{product['name']}   QUANTIDADE {product['amount']}")
	print (f"QUANTIDADE TOTAL: {countAux}")

# função main()
marketStock = []
print ("\t\t============== MARKET STOCK ==============")
menu (marketStock)