while True:
    n = int(input())

    if n == 0:
        break
    dicionario = {}
    for i in range(n):
        lista = input().split()
        dicionario.update({lista[0]:lista[1]})

    contador = 0
    alunos = int(input())

    for i in range(alunos):
        lista = input().split()
        erros = 0
        for i in  range (len(dicionario[lista[0]])):
            if dicionario[lista[0]][i] != lista[1][i]:
                erros += 1

        if erros >= 2:
            contador += 1


    print(contador)