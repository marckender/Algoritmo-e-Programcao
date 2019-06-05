def media():
	media=soma/conta
	return media

#codigo principal
soma=0
conta=0
for i in range(1,4):
	notas=int(input("Digite a nota: "))
	soma+=notas
	conta+=1

print(media())


#codigo2
def media(a,b,c):
	soma=a+b+c
	media=soma/3
	return media

#codigo principal
a=int(input("Digite a nota: "))
b=int(input("Digite a nota: "))
c=int(input("Digite a nota: "))

print(media(a,b,c))