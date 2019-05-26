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
#chamada da funçao2
def exo2():

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

#chamada da EXO3
################
def exo3():

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

#chamada da exo3
def exo4():
###############

    aux=1
    for i in range(1,1000):
        if primo(aux) and primo(i):
            if gemeos(aux,i):
                print(aux, "e" ,i,"Sao primos gemeos")
            aux=i

        i+=1

##############Exo6############################
def exo6():
    n=(int(input("DIGITE O NUMERO: ")))
    conta=1
    soma=0
    while conta<n:

        if n%conta==0:
            soma+=conta
            conta+=1
        else:
            conta+=1
    if soma==n:
        print("perfeito: ")
        return 1
    else:
        #print("nao e perfeito: ")
        return 0


   



#################EXO7####################################

def exo7():

    x=int(input("Digite o limite: "))
    conta=0
    soma=0
    for i in range (x):
        notas=float(input("Digite a nota: "))

        conta+=1
        soma+=notas
    media=soma/conta
    print(media)
    return media





#exo1()
#exo2()
#exo4()
#5
exo6()
#exo7()


#
