A=0
B=1
N=int(input("Digite um numero: "))
print(A)
print(B)
for i in range(N-2 ):
	s = A + B	
	print(s)
	aux = A
	A = B
	B = s