#1
'''############################################

1. Escreva um programa que leia um número de 1 a 12 (usando input) e, com base neste número,
imprima o mês correspondente. O programa deve guardar e procurar o mês correspondente ao
número em uma lista.


mes=["janeiro","fevereiro","marco","April","Maio","Junho","Julho","Augosto","setembro","Otubro","novembro","Dezembro"]
for i in range (len(mes)):
	v=int(input("Informe o mes desejo: "))
	if v>=1 and v<=12:
		print(mes[v-1])
	else:
		print("numero invalida")
'''

#2
''' ############################################
2. Escreva um programa que leia 10 palavras 
com um laço FOR, 
armazenando-as em uma lista. Ao
final, deve-se imprimir qual foi
 a palavra digitada que possui mais caracteres.


palavras=[]
maior=0

for i in range (0,10):
	palavras.append(input("Digite uma palavra: "))
maiorpalavra=[]
for v in palavras:
	if len(v)>maior:
		maior=len(v)
		maiorpalavra=v
print(maiorpalavra)
'''


#3
###################################################

'''
3. Escreva um programa que leia 20 números
 para uma lista. A seguir, troque o 1o elemento
 com oúltimo, o 2o com o penúltimo e etc.,
 até o 10o com o 11o. Por fim, escreva o vetor 
 com as modificações realizadas. 
Obs.: não utilizar o método reverse().
'''



#4
#######################################
'''
4. Faça um programa que leia 20 números 
para uma lista. A seguir, verifique e 
remova todos os números que não são pares. 
Por fim, escreva o vetor com as modificações realizadas.

lista=[]
for i in range (1,21):
	lista.append(int(input("Digite o numero {0}: ".format(i+1))))
for i in lista:
	if i%2!=0:
		lista.remove(i)
print(lista)
'''


#5· 
'''

Escreva um programa que leia uma lista de 13 posições, 
sendo ela o gabarito de um teste de
loteria esportiva, contendo os valores 1 (coluna 1)
 2 (coluna 2) e 3 (coluna do meio). Na sequência,
leia mais uma lista de 13 posições contendo uma aposta.
 Após isso, compare as listas, verificando o
número de acertos. No fim, escrever a quantidade de acertos,
e se a aposta possuir 13 acertos,
acrescentar a mensagem: "GANHADOR, PARABÉNS".

'''

################################################
gabarito=[]
aposta=[]
#acerto=0
for i in range (13):
	gabarito.append(int(input("digite um numero {0}:".format(i+1))))

print("*****")
for i in range (13):
	aposta.append(int(input("Digite um numero {0}:".format(i+1))))

#acertos
acerto=0
for i in range(13):
	if gabarito[i]==aposta[i]:
		acerto+=1
print("quantidade de acerto: ",acerto)