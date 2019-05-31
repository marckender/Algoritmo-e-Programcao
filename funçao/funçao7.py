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
print("media: {:.2f}".format(mid(conta,soma)))
