n = int(input())


for i in range(n):
    alunos = int(input())
    lista_definitiva = []
    
    lista_nomes = input().split()
    lista_faltas = input().split()

    for d in range(len(lista_faltas)):
        contador_aulas = 0
        contador_presenca = 0
        for c in lista_faltas[d]:
            if c == 'P':
                contador_aulas +=1
                contador_presenca += 1
            elif c == 'A':
                contador_aulas += 1
        if (contador_presenca / contador_aulas) < 0.75:
            lista_definitiva.append(lista_nomes[d])


    if len(lista_definitiva) == 0:
        print()
    else:
        for i in lista_definitiva[0:-1]:
            print(i, end=' ')
        print(lista_definitiva[-1])
