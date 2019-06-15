import math
def raiz(num):
	a=math.sqrt(num)
	if a==int(a):
		return 1
	else:
		return 0


print(raiz(int(input("Digite algo: "))))
