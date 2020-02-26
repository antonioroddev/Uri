l = []
for i in range(20):
    l.append(int(input()))
contador = 0
for i in l[::-1]:
    print('N[{}] = {}'.format(contador,i))
    contador += 1

