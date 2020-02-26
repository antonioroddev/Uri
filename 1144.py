contador = 1
for i in range(int(input())):
    print('{}'.format(contador**1),end=' ')
    print('{}'.format(contador**2),end=' ')
    print('{}'.format(contador**3))
    print('{}'.format(contador**1 ),end=' ')
    print('{}'.format(contador**2 + 1),end=' ')
    print('{}'.format(contador**3 + 1))
    contador += 1