def capicua(num):
	num=str(num)
	lista=[]
	lista2=[]

	for j in range(len(num)):
		lista.append(num[j])
	for i in range(len(num)-1,-1,-1):
		lista2.append(lista[i])


	if lista == lista2:
		return 'e capitua'
	else:
		return 'nao e capitua'


print(capicua(int(input("Digite algo: "))))