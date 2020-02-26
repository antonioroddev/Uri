for i in range(int(input())):
    n = int(input()) 
    a = (n // 2) + 1
    soma = 0
    for i in range(1,a):
        if n % i == 0:
            soma += i

    if soma == n:
        print('{} eh perfeito'.format(n))
    else:
        print('{} nao eh perfeito'.format(n))