aluno=1
while aluno<=10:
	n1,n2=[float(x) for x in input().split()]
	aluno=aluno+1
	media=(n1+n2)/2
	print("a media eh: ",media)

	if media>=6:
		print("Aluno approvado")
		print()
	else:
		print("Aluno reprovado")
		print()