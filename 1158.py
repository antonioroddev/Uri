for i in range(int(input())):
    l = [int(d) for d in input().split()]
    contador = 0
    soma = 0
    while contador < l[1]:
        if l[0] % 2 != 0:
            soma += l[0]
            contador += 1
        l[0] += 1
        
    print(soma)