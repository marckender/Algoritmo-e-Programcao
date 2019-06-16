'''
. Faça um programa que leia os dados de 5 estádios de futebol
 e armazene-os em uma lista, sendo
sua estrutura representada pela estrutura abaixo:
class Estadio:
nome = ""
capacidadePublico = 0
recordPublico = 0
Após ler os dados dos estádios, faça duas funções:
maior_capacidade(lista): percorre a lista de estádios, 
retornando o estádio com maior capacidade.
maior_publico(lista): percorre a lista de estádios, 
retornando o estádio com maior record de
publico;
Ao final, imprima o nome do estádio com maior capacidade
 e com maior record de público que
foram retornados pelas funções.
'''

class estadio:
	nome=''
	capacidadePublico=0 
	recordPublico=0 
def insere(lista):
	for i in range(3):
		dados=estadio
		dados.nome=input('digite um nome:')
		dados.capacidadePublico=int(input('digite capacidadePublico:'))
		dados.recordPublico=int(input('digite recordPublico:'))
		lista.append(dados)
lista=[]
insere(lista)
def maior_capacidade(lista):
	maiorc=0 
	for j in range(len(lista)):
		if lista[j].capacidadePublico>maiorc:
			maiorc=lista[j].capacidadePublico 
			n=lista[j].nome
	print(n)
maior_capacidade(lista)
def maior_public(lista):
	maiorp=0 
	for j in range(len(lista)):
		if lista[j].recordPublico>maiorp:
			maiorp=lista[j].recordPublico
			n=lista[j].nome 
	print(n) 
maior_public(lista)

