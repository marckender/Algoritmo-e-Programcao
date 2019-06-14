''' Defina uma estrutura que ira apresentar bandas de musicas
essa estrutura deve ter o nome da banda , que tipo de musica ela toca
o numero de integrantes e em que posiçao do ranking essa banda esta
 dentre as suas 5  bandas favoritas

'''

class banda:
	nome_b=''
	t_mu=''
	num_inte=0
	pos=0

lista=[]
for i in range (5):
	print("\nBanda",i+1)
	b=banda()
	b.nome_b=input("informe o nome da banda:")
	b.t_mu=input("Informe o tipo de musica: ")
	b.num_inte=int(input("Insere os membros: "))
	b.pos=int(input("Digite a posiçao: "))
	lista.append(b)
for i in range (len(lista)):
	print()
	print(lista[i].nome_b)
	print(lista[i].t_mu)
	print(lista[i].num_inte)
	print(lista[i].pos)

