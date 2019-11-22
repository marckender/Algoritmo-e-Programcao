salarioUp=0
salarioDown= 9999999999
conta=1
#
nome=''
nomeMaisAlt=''
nomeMaisBaixo=''
while True:
	print()
	nome=input("Digite o nome: ")
	if nome !='fim':
		salario=float(input("informe o salario: "))
		
	else:
		break
	#conta=conta+1
###
	if salario>salarioUp:
		salarioUp=salario
		nomeMaisAlt=nome

###
	if salario<salarioDown:
		salarioDown=salario
		nomeMaisBaixo=nome

	media=salario/conta
print()
print("Nome: {} ||| salario mais Alto: {}".format(nomeMaisAlt,salarioUp))
print("Nome: {} ||| salario mais Baixo: {}".format(nomeMaisBaixo,salarioDown))
print("media: ",media)
