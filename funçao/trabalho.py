def media(n1,n2):
    M=(n1+n2)/2
    return M

###Chamada da exo1:
def exo1():

#codigo principal
    for i in range (5):
        aluno=input("Digite um  nome {0}: ".format(i+1))
        n1=float(input("Digite a nota 1: "))
        n2=float(input("Digite a nota 2: "))
        print("media",media(n1,n2))
        print()


#####################################EXO2#################



def min(X,Y):
    if X>Y:
        return X
    elif Y>X:
        return Y
#chamada da ,
def exo2():
#
#CODIGO PRINCIPAL
    X=int(input("Digite o numero 1: "))
    Y=int(input("Digite o numero 2: "))
    print("o maior: ",min(X,Y))


###########EXO3###################################

def fat(N):
    f=1
    for i in range (0,N):
        f=f*(N-i)
    return f

#
def exo3():
#
    N=int(input("fatoriel de: "))
    print("eh: ",fat(N))



##################EXO4########################
def primo(N):
    i=2
    primo=True
    for i in range (2, N):
        if N%i==0:
            primo=False
    if primo:
        return True
    else:
        return False
#
def gemeos(aux,i):
    if i-aux==2:
        return True

#
def exo4():
#

    aux=1
    for i in range(1,1000):
        if primo(aux) and primo(i):
            if gemeos(aux,i):
                print(aux, "e" ,i,"Sao primos gemeos")
            aux=i

        i+=1


#################Exo5######################

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

def exo5():
    n1=[4,2,4,1]
    n2=[3,7,7,2]

    v=somalista(n1,n2)
    print(v)
    somalista(n1,n2)


##############Exo6############################
def perfeito(n):

    conta=1
    soma=0
    while conta<n:

        if n%conta==0:
            soma+=conta
        conta+=1

    if soma==n:
        return 1
    else:
        return 0
#
def exo6():
#
    print(perfeito(int(input("DIGITE O NUMERO: "))))


#################EXO7####################################
def mid(conta,soma):

    media=soma/conta
    return media

conta=0
soma=0
while True:
    notas=float(input("Digite a nota: "))
    if notas <0:
        break

    conta+=1
    soma+=notas
def exo7():
    print("media: {:.2f}".format(mid(conta,soma)))


#Fiz a chamada das funçoes aqui,so tirar o comantario pra rodar o execicio desejada.

exo1()
#exo2()
#exo3()
#exo4()
#exo5()
#exo6()
#exo7()
