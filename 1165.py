def eh_primo(numero):
    a = numero
    numero = int(numero**0.5) + 1
    contador = 0
    for d in range(1, numero):
        if a % d == 0:
            contador += 1
        if contador > 1:
            return False
    return True

for i in range(int(input())):
    n = int(input())

    if eh_primo(n):
        print('{} eh primo'.format(n))
    else:
        print('{} nao eh primo'.format(n))
