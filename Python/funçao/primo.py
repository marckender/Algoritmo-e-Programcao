def primo(num):
	primo=True
	i=2
	for i in range (2,num):
		if num%i==0:
			primo=False
			break
	if primo:
		return "True"
	else:
		return "False"

print(primo(int(input("Digite o numero: "))))

