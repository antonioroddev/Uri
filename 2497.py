contador = 1
while True:
    n = (int(input()))

    if n == -1:
        break

    if n % 2 != 0:
        n = n-1
    
    print('Experiment {}: {} full cycle(s)'.format(contador,int(n/2)))

    contador +=1