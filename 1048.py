n = float(input())

if 0 <= n <= 400:
    reajuste_pc = 15
    reajuste = n * 0.15
elif 400.01 <= n <= 800:
    reajuste_pc = 12
    reajuste = n * 0.12
elif 0 <= n <= 1200:
    reajuste_pc = 10
    reajuste = n * 0.10
elif 0 <= n <= 2000:
    reajuste_pc = 7
    reajuste = n * 0.07
elif n > 2000:
    reajuste_pc = 4
    reajuste = n* 0.04

print('Novo salario: {:.2f}'.format(n+reajuste))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(reajuste_pc))