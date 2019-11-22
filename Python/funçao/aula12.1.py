class data:
	ano=0
	mes=0
	dia=0

def insere(lista):
	for i in range(3):
		x=data()
		x.ano=int(input("Digite o ano: "))
		x.mes=int(input("Digite o mes: "))
		x.dia=int(input("Digite o dia: "))
		lista.append(x)
listadata=[]
insere(listadata)
def com(listadata):
	menor_ano=9999999999999
	
	for j in range(len(listadata)):
		if listadata[j].ano<menor_ano:
			menor_ano=listadata[j].ano
			mes1=listadata[j].mes 
			dia1=listadata[j].dia
	print("menor ano:  {}/{}/{} ".format(dia1,mes1,menor_ano))
com(listadata)
