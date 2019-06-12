def calcule(n ,p):

	fat=1
	for i in range(n,0,-1):
		fat=fat*i
	A=n-p
	fatoriel=1
	for j in range(A,0,-1):
		fatoriel=fatoriel*j

	Aranja=fat/fatoriel

	return Aranja




x=int(input("Digite o valor de n: "))
if x<0:
	x=int(input("Digite de novo valor de n"))

y=int(input("Digite o valor de p: "))
if y>x:
	y=int(input("Digite de novo valor de p"))

print(calcule(x,y))
