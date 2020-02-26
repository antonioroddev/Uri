contador = 0
for i in range(10):
    x = int(input())

    if x <= 0:
        print('X[{}] = 1'.format(contador))
    else:
        print('X[{}] = {}'.format(contador,x))

    contador += 1