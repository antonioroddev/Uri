n = True
lista_nome =[]
lista_soma =[]
if __name__ == '__main__':
    while n != 0:
        
        n = int(input())
        if (n >= 1 and n <= 100):
            lista = [input().split(' ') for i in range(0,n)]
            for i in range(0,n):
                lista_nome.append(lista[i][0])
                lista_soma.append((int(lista[i][1])) - (int(lista[i][2])))      
            print(lista_nome[lista_soma.index(min(lista_soma))])
            lista.clear()
            lista_nome.clear()
            lista_soma.clear()