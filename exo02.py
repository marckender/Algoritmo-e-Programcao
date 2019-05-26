'''n=int(input("Tabuada: "))
for i in range (1,10+1):

	print("{} X {} = {} ".format(n,i,n*i))
	'''

'''a=0
b=1
n=int(input("digite o numero: "))

print(a)
print(b)
for i in range (n-2):
	s=a+b
	print(s)
	aux=a
	a=b
	b=s
'''

n = 10
for i in range(n):
	for j in range(n):
		if i == j:
			print("1 ",end="")
		else:
			print("0 ",end="")
	print()