def soma(l1,l2):
	v=[]
	for i in range(len(l1)):
		mult=l1[i]*l2[i]
		v.append(mult)
	soma=0 
	for j in v:
		soma=soma+j
	return soma 



l1=[]
l2=[]
while True:
	n1=int(input('digite um numero 1:'))


	if n1==-1:
		break
	l1.append(n1)
	n2=int(input('digite um numero 2:'))
	l2.append(n2)
print(soma(l1,l2))


