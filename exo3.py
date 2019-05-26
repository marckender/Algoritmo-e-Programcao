N1=int(input("informe o primeiro numero: "))
N2=int(input("infor,e o d=segundo numero: "))
quoc=0
while N1>=N2:
	N1=N1-N2
	quoc=quoc+1
print("o quoc: {}| o resto: {}".format(quoc,N1)