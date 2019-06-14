''' D. Defina uma estrutura que irá representar bandas de música. Essa estrutura deve ter o
nome da banda, que tipo de música ela toca, o número de integrantes e em que posição
do ranking essa banda está dentre as suas 5 bandas favoritas.
2. Crie um looping para preencher as 5 estruturas de bandas criadas no exemplo
passado. Após criar e preencher, exiba todas as informações das bandas/estruturas.
3. Crie uma função que peça ao usuário um número de 1 até 5. Em seguida, seu
programa deve exibir informações da banda cuja posição no seu ranking é a que foi
solicitada pelo usuário.
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
	'''print()
	print(lista[i].nome_b)
	print(lista[i].t_mu)
	print(lista[i].num_inte)
	print(lista[i].pos)'''

def pos(lista):

	x=int(input("Digite um posiçao: "))
	if x>=1 and x<=5:
		for i in range(len(lista)):
			if x==lista[i].pos:
				print(lista[i].nome_b,lista[i].t_mu,lista[i].num_inte,lista[i].pos)

pos(lista)