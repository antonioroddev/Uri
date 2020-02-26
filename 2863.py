while True:
    try:

        n = int(input())
        lista = []
        for i in range(n):
            lista.append(float(input()))
        print('{:.2f}'.format(min(lista)))

    except EOFError:
        break