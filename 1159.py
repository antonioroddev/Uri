while True:
    n = int(input())

    if n == 0:
        break

    contador = 0
    soma = 0
    while contador < 5:
        if n % 2 == 0:
            soma += n
            contador += 1
        n += 1
        
    print(soma)