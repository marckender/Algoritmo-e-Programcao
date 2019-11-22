class nome:
	nome=''
	sobrenome=''

def leianome(lista):
	n=nome()
	n.nome=input("Digite o nome: ")
	n.sobrenome=input("Digite o sobrenome: ")
	print(n.nome + " " + n.sobrenome)



	nomecontrario=' '
	nome2=''
	for i in n.nome:
		nomecontrario= i+ nomecontrario
	for j in n.sobrenome:
		nome2=j + nome2
	print(nome2,"",nomecontrario)

leianome(nome)