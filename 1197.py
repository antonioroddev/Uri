while True:
    try:
        lista = input().split()
        print(2*int(lista[0]) * int(lista[1]))
    except EOFError:
        break
