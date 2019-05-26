def fat(N):
    f=1
    for i in range (0,N):
        f=f*(N-i)
    return f


N=int(input("fatoriel de: "))
print("eh: ",fat(N))
