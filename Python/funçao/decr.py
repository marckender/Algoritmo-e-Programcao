def derc(a,b,c):

	if a>b:
		aux=a
		a=b
		b=aux
	if a>c:
		x=a
		a=c
		c=x
	if b>c:
		y=b
		b=c
		c=y
	return a,b,c


n1=int(input("Digite um numero: "))
n2=int(input("Digite um numero: "))
n3=int(input("Digite um numero: "))
print(derc(n1,n2,n3))