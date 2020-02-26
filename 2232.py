n = int(input())

for i in range(n):
    linhas = int(input())
    soma = 0
    for i in range(linhas):
        soma += 2**i
    
    print(soma)

