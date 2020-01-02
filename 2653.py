lista = []
while True:

    try:

        inputt = input()

        if inputt not in lista:
            lista.append(inputt)


    except EOFError:
        break
print(len(lista))