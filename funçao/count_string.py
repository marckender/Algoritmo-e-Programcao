'''
Faça um programa que possua uma função 
que recebe uma string e um caractere, e retorne o
número de vezes que esse caractere aparece 
na string. Por exemplo, se a função 
receber “teste de
mesa” e o caractere “s”, ela deve retornar 2.

'''
def string(string,caractere):


	cont=0
	for i in range(len(string)):
		if caractere==string[i]:
			cont+=1
	return cont


x=input("Digite uma string: ")
y=input("Digite uma cractere: ")

print(string(x,y))