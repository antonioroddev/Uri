contador = 1
for i in range(int(input())):
    for d in range(1,3):
        print('{}'.format(contador**d),end=' ')
    print(contador**3)
    contador += 1
    