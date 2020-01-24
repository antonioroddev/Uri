n = int(input())

for i in range(n):

    string = input()
    lista = string.split('x')
    a = int(lista[0])
    b = int(lista[1])

    if a == b:
        for d in range(5,11):
            print('{} x {} = {}' .format(a,d,a*d))
    else:
        for d in range(5,11):
            print('{} x {} = {} && {} x {} = {}' .format(a,d,a*d,b,d,b*d))


