inter = 0
gremio = 0
empate = 0
total = 0
while True:
    l = [int(i) for i in input().split()]
    print('Novo grenal (1-sim 2-nao)')
    if l[0] > l[1]:
        inter += 1
    elif l[0] < l[1]:
        gremio += 1
    else:
        empate += 1
    total += 1
    a = int(input())
    if a == 2:
        break
a = 'Inter venceu mais'
if gremio > inter:
    a = 'Gremio venceu mais'
if gremio == inter:
    a = 'Nao houve vencedor'
print('{} grenais\nInter:{}\nGremio:{}\nEmpates:{}'.format(total,inter,gremio,empate))
print(a)

