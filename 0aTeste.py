lista = ["0001000","000200","00030"]


comp0 = lista[0][::-1]
comp1 = lista[1][::-1]
comp2 = lista[2][::-1]

print(comp0)
print(comp1)
print(comp2)

if int(comp0) + int(comp1) == int(comp2):
    print('True')

else:
    print('False')


