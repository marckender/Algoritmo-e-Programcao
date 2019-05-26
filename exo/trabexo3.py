'''
Faça um programa que lê cinco (5) nomes 
digitados pelo usuário e no final imprime 
esses nomes ordenados. Guarde os nomes em
uma lista para serem ordenados no final
'''

lista=[]
for i in range (0,5):
	lista.append(input("Add a nome: "))

lista_ordenada=sorted(lista)

print(lista)
print("Lista Ordenada: ",lista_ordenada)