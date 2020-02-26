l = list(map(int, input().split()))
soma = 0
a = l[0]
for i in range(0,l[-1]):
    soma += a + i
print(soma)