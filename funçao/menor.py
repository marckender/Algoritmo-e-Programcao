def menor(lista):
	menor=99999999999999999999999
	for i in range(len(lista)):
		if lista[i]<menor:
			menor=lista[i]
	return menor



lista=[]
while True:
	n=int(input("Digite um numero: "))
	
	if n==0:
		break
	lista.append(n)


print(menor(lista))