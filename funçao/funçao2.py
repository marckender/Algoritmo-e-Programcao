def min(X,Y):
    if X>Y:
        return X
    elif Y>X:
        return Y

#CODIGO PRINCIPAL
X=int(input("Digite o numero 1: "))
Y=int(input("Digite o numero 2: "))
print("o maior: ",min(X,Y))
