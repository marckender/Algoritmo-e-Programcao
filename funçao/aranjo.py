def anjo(n,p):
	x=n-p
	fat=1
	fatx=1
	faty=1
	for i in range(n,0,-1):
		fat=fat*i
	for j in range(x,0,-1):
		fatx=fatx*j
	for y in range(y,0,-1):
		faty=faty*y

	A=fat/(faty*fatx)
	return A


n=int(input("Digite o fatoriel: "))
if n<0:
	n=int(input("Digite o fatoriel: "))
	#
p=int(input("Digite algo: "))
if p>n:
	p=int(input("Digite algo: "))

print(anjo(n,p))