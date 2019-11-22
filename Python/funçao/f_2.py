def dobra(num):
	num*=2
	return num


def entra():
	for  i in range (3):
		num=int(input("Digite o valor: "))
		print(dobra(num))
entra()