soma = 0
cont = 0
while True:
    a = int(input())
    if a < 0:
        break
    soma += a
    cont += 1
print('{:.2f}'.format(soma/cont))