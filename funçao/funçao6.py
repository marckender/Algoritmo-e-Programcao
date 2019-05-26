def perfeito(n):
    conta=1
    soma=0
    while conta<n:

        if n%conta==0:
            soma+=conta
            conta+=1
        else:
            conta+=1
    if soma==n:
        #print("perfeito: ")
        return 1
    else:
        #print("nao e perfeito: ")
        return 0
a=perfeito(int(input("DIGITE O NUMERO: "))
