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

print(perfeito(int(input("DIGITE O NUMERO: "))))
