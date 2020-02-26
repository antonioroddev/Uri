for i in range(int(input())):
    x = int(input())
    frase = ''

    if x == 0:
        print('NULL')
    else:
        if x % 2 != 0:
            frase += 'ODD '
        else:
            frase += 'EVEN '
        if x > 0:
            frase += 'POSITIVE'
        else:
            frase += 'NEGATIVE'
        print(frase)