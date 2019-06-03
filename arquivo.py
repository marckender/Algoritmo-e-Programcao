''' implementar 2 programas/ funçoes
1-ler lestras textuas informados pelo usuario e gravar em arquivo le texto
2-imprimir o conteudo do arquivo

'''
def prog1():
    f=open("texto.txt",'w+')
    type=""
    type=True
    while True:
        type=input("")
        if type =="@":
            break
            f.close()
        f.write(type+"\n")
prog1()

def read():
    f=open("texto.txt","r")
    lines=f.readlines()
    for i in lines:
        print(i)
    f.close
read()
