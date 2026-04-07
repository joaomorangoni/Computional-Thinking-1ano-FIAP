def fibonnaci(n):
    ante = 0
    seq = 0
    nfinal = 0
    for i in range(n):
        nfinal = seq + ante
        ante = seq
        seq = nfinal
        if nfinal == 0:
            ante = 1
    
    return nfinal
        


esimo = int(input("Digita um número: "))

print(fibonnaci(esimo))