while True:
    lista = []
    try:

        n = int(input())

        for i in range(0,n):
            lista.append(input().split(" "))
        lista_num = []
        cont = 0
        index = 0
        for i in lista:
            for j in i[:-1]:
                cont += 3
                index += 1

            lista_num.append(cont + len(i[index]))
            cont = 0
            index = 0
        
        for contador in lista_num:
            print(chr(96+contador))


    except EOFError:
        break