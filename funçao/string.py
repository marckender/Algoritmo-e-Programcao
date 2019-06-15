def string(num,letra):

	for i in range(len(num)):
		mult=letra[i]*num[i]
	
num=[]
letra=[]
for i in range (6):
	num.append(int(input("Digite um numero: ")))
for j in range(6):
	letra.append(input("Digite uma letra: "))


print(string(num,letra))