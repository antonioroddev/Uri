for i in range(int(input())):
    l = [int(i) for i in input().split()]
    if l[1] == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(l[0]/l[1]))