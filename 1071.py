x = int(input())
y = int(input())
soma = 0
if (x > y):
    a = y
    y = x
    x = a
x += 1
while (x < y):
    if ((x % 2)!= 0):
        soma += x
    x += 1

print(soma)
