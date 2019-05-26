v=int(input("digite um numero: "))
for N in range (v):
	N=int(input("digite um numero: "))
	i=2
	primo=0
	while i<=N:
		if N%i==0:
			primo=primo+1
		i=i+1
		

	if primo==1:
		print("eh primo")
	else:
		print("nao eh primo")
