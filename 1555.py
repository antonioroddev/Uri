n = int(input())

for i in range(n):
    lista = input().split()
    x = int(lista[0])
    y = int(lista[1])

    rafael = (3*x)**2 + y**2
    beto = 2 * (x**2) + (5*y)**2
    carlos = -100 * x + y**3

    if rafael >= beto and rafael >= carlos:
        print('Rafael ganhou')
    elif carlos >= beto and carlos >=rafael:
        print('Carlos ganhou')
    elif beto >= carlos and beto >= rafael:
        print('Beto ganhou')
