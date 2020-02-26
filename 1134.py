alcool = 0
gas = 0
diesel = 0
while True:
    a = int(input())
    if a == 1:
        alcool += 1
    elif a == 2:
        gas += 1
    elif a == 3:
        diesel += 1
    elif a == 4:
        break
print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gas))
print('Diesel: {}'.format(diesel))
