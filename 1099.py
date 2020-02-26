for i in range(int(input())):
    l = [int (i) for i in input().split()]
    if l[0] > l[1]:
        l_inf = l[1] + 1
        l_sup = l[0]
    else:
        l_inf = l[0] + 1
        l_sup = l[1] 

    soma = 0

    for c in range(l_inf, l_sup):
        if c % 2 != 0:
            soma += c

    print(soma)
    