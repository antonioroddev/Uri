l = []
c_neg = 0
c_impar = 0
c_par = 0
c_pos = 0
for i in range(5):
    n = int(input())

    if n % 2 ==0:
        c_par += 1
    else:
        c_impar += 1
    if n > 0:
        c_pos += 1
    if n < 0:
        c_neg += 1

print('{} valor(es) par(es)'.format(c_par))
print('{} valor(es) impar(es)'.format(c_impar))
print('{} valor(es) positivo(s)'.format(c_pos))
print('{} valor(es) negativo(s)'.format(c_neg))