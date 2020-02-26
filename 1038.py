l = [int(i) for i in input().split()]

soma = 0
i = l[0]
if i == 1:
    soma+=4
elif i == 2:
    soma+= 4.5
elif i == 3:
    soma+= 5
elif i == 4:
    soma+= 2
elif i == 5:
    soma+= 1.5

soma *= l[1]


print('Total: R$ {:.2f}'.format(soma))
