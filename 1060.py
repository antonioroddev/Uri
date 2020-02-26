contador = 0
for i in range(6):
    if float(input()) > 0:
        contador += 1
print('{} valores positivos' .format(contador))