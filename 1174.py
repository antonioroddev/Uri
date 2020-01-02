lista = []

for i in range (0,100):
    lista.append(float(input()))


for i in range (len(lista)):
    if lista[i] <= 10:
        print("A[{}] = {}".format(i,lista[i]))

        
