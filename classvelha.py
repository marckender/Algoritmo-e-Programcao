class cadastro:
	nome=''
	idade=0
	peso=0


def pessoa(lista):

	for i in range (5):
		print("\nCadastro: ",i+1)
		b=cadastro()
		b.nome=input("Digite o nome: ")
		b.idade=int(input("Digite a sua idade: "))
		b.peso=float(input("Digite seu peso: "))
		lista.append(b)

listacadastro=[]
pessoa(listacadastro)

def imprime(listacadastro):
	maior=0
	for i in range(len(listacadastro)):
		x=listacadastro[i].idade
		if x>maior:
			maior=x
	print(maior)
imprime(listacadastro)