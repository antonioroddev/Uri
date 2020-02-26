while True:
    n = int(input())

    if n == 0:
        break
    soma = 0
    for i in range(n,0,-1):
        soma += i**2

    print(soma)