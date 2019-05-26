Num=1
par=0
impar=0
while Num !=0:
	Num=int(input("Digite um numero: {}".format(Num)))
	

	if Num % 2==0:
		par=par+Num
	elif Num % 2  !=0:
		impar=impar+Num
print("soma par: {} ||| impar: {}".format(par,impar))