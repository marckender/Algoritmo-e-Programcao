def media(n1,n2):
    M=(n1+n2)/2
    return M

#codigo principal
for i in range (5):
    aluno=input("Digite um  nome {0}: ".format(i+1))
    n1=float(input("Digite a nota 1: "))
    n2=float(input("Digite a nota 2: "))
    print("media",media(n1,n2))
    print()
