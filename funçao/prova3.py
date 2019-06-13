'''

sobre :

*Matrizes
*structs
*string
*Funçoes



Fazer funçoes que receber uma cadeia de caracteres (string)
e uma caracter e retorne uma nova cadeia com a caracter passado
como parametro substituido por "*"
'''

'''#####################################################
def carater(string,cara):
	nova=''
	for i in range (len(string)):
		if string[i]==cara:
			nova=nova + '*'
			string[i]
		else:
			nova=nova+string[i]
	print(nova)

string=input("Digite uma frase: ")

cara=input("Digite uma caracter: ")

carater(string,cara)

''' #########################################


'''Dada uma estrutura com os siguientes atributos
nomep=string
nvit=int
nder=int
nemp=int

força 2 funçoes:

1--Recebe uma lista (vazia)
e insere nesta lista 5 elementos do tipo da estrutura

2--recebe a lista com os elemnetos e imprima o nome 
dos paises com o maior numero de ponto

'''


class fut():
	nomep=''
	nvit=0
	nder=0
	nemp=0


def insertime(time):
	
	for i in range (5):

		t=fut()
		t.nomep=input("Digite o nome: ")
		t.nvit=int(input("Vitoria: "))
		t.nder=int(input("Derotas: "))
		t.nemp=int(input("Empate: "))

		time.append(t)


