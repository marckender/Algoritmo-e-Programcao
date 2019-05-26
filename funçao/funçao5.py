def somalista(lista1,lista2):
	r=len(lista1)
	s=0
	b=0
	vetor=[]
	for i in range (r):
		vetor.append(0)

	for i in range(r-1,-1,-1):
		s=lista1[i]+lista2[i]+b
		if s>9 and i !=0:
			a=str(s)
			b=int(a[0])
			vetor[i]=int(a[1])
		else:
			vetor[i]=s

	return vetor




n1=[8,5]
n2=[2,5]

v=somalista(n1,n2)
print(v)
somalista(n1,n2)