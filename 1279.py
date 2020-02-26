contador = 0
while True:

    try:
        ano = int(input())
        if contador != 0:
            print()
        bissexto = ((ano  % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0) 
        hucululu = (ano % 15 == 0)
        bukululu = bissexto and (ano % 55 == 0)
        todos = hucululu or bukululu or bissexto
        if bissexto:
            print('This is leap year.')
        if hucululu:
            print('This is huluculu festival year.')
        if bukululu:
            print('This is bulukulu festival year.')
        if  not todos:
            print('This is an ordinary year.')
        contador = 1
    except EOFError:
        break
