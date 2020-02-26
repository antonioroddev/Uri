while True:
    l = [int(i) for i in input().split()]
    if l[0] == 0 or l[1] == 0:
        break

    if l[0] > 0 and l[1] < 0:
        print('quarto')
    elif l[0] > 0 and l[1] > 0:
        print('primeiro')
    elif l[0] < 0 and l[1] < 0:
        print('terceiro')
    elif l[0] < 0 and l[1] > 0:
        print('segundo')