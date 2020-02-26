def calc_fatorial(n):
    if n == 0:
        return 1
    return n * calc_fatorial(n-1)

while True:
    n = input()

    if int(n) ==0:
        break
    
    indice = len(n) -1
    contador = 1
    soma = 0
    for i in range(len(n)):
        soma += int(n[indice]) * calc_fatorial(contador)
        contador +=1
        indice -=1

    print(soma)


