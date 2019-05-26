def mid(x):
    return media

x=int(input("Digite o limite: "))
conta=0
soma=0
for i in range (x):
    notas=float(input("Digite a nota: "))
    conta+=1
    soma+=notas
media=soma/conta
print("media: {:.2f}".format(mid(x)))
