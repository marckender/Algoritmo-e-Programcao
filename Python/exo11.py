n=int(input("Digite um numero: "))
cont=1
soma=0
while cont<n:
	if n%cont==0:
		soma+=cont
		cont+=1
	else:
		cont=cont+1
if soma==n:
	print("e perfeito")
else:
	print("nao e perfeito")