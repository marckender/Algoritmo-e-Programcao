'''
Um aluno de uma turma pode ser representado pelos seguintes 
dados: matrícula, nota 1 e nota 2.
Faça um programa que leia 5 alunos, guardando seus dados
 em uma estrutura. Após ler cada aluno,
chame a função media_aluno(aluno), sendo que ela recebe 
uma variável do tipo estrutura aluno e
retorna a sua média ((nota 1+nota 2)/2), que deve ser 
impressa no código principal.
'''

class media:
	matricula=0
	nota1=0
	nota2=0
def leia(lista):
	for i in range (5):
		x=media()
		x.matricula=int(input("Digite a matricula: "))
		x.nota1=float(input("Digite a 1e nota: "))
		x.nota2=float(input("Digite a 2e nota: "))
		lista.append(x)


listamedia=[]
leia(listamedia)

def media(listamedia):
	for j in range (5):
		media=(listamedia[j].nota1+listamedia[j].nota2)/2
		n=listamedia[j].matricula 
		print("Matricula: {} ||| {}".format(n,media))
media(listamedia)

