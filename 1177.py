n = int(input())
contador = 0
for i in range(1000):
    if contador == n:
        contador = 0
    print('N[{}] = {}'.format(i,contador))
    contador += 1