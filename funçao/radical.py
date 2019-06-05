def radical(raiz,in):
	raiz=raiz**1/2
	if raiz<0:
		return'radicando invalido.digite radicando:'
    if in <=1:
    	return'indice invalido.digite indice:'
    if raiz>0 and in>1:
    	return raiz

for i in range(3):
	rad=float(input("Digite o Radical: "))
	indi=int(input("Digite o indice: "))
	print(radical(rad,indi))
