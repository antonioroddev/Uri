if __name__ == '__main__':
    lista = [input() for i in range (0,3)]
    valor = float(lista[1]) + (float(lista[2]) * 0.15)
    print('TOTAL = R$ {:.2f}'.format(valor))