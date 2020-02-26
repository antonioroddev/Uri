a = -1
b = -1
while True:
    a = float(input())
    if not (0 <= a <=10):
        print('nota invalida')
    else:
        break
while True:
    b = float(input())
    if not (0 <= b <=10):
        print('nota invalida')
    else:
        break
print('media = {:.2f}'.format((a + b)/2))    