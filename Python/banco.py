class cadastro:
	modelo=''
	marca=''
	ano_f=0

def leia(lista):
	return lista
lista=[]
for i in range(3):
	print("\nCarro***",i+1)
	b=cadastro
	b.modelo=input("Digite o modelo: ")
	b.marca=input("Digite a Marca: ")
	b.ano_f=int(input("Digite o ano: "))
	lista.append(b)
for i in range(len(lista)):
	print()
	print(leia(lista[i].modelo))
	print(leia(lista[i].marca))
	print(leia(lista[i].ano_f))
