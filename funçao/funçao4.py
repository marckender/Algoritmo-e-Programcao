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


    aux=1
    for i in range(1,1000):
        if primo(aux) and primo(i):
            if gemeos(aux,i):
                print(aux, "e" ,i,"Sao primos gemeos")
            aux=i
        i+=1
