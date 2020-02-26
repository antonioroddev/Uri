qut_ratos = 0
qut_coelhos = 0
qut_sapos = 0
qut_total = 0
for i in range(int(input())):
    l = input().split()
    l[0] = int(l[0])
    if l[1] == 'C':
        qut_coelhos += l[0]
    elif l[1] == 'R':
        qut_ratos += l[0]
    elif l[1] == 'S':
        qut_sapos += l[0]
    qut_total += l[0]
print('Total: {} cobaias'.format(qut_total))
print('Total de coelhos: {}'.format(qut_coelhos))
print('Total de ratos: {}'.format(qut_ratos))
print('Total de sapos: {}'.format(qut_sapos))
print('Percentual de coelhos: {:.2f} %' .format((qut_coelhos/qut_total)*100) )
print('Percentual de ratos: {:.2f} %'.format((qut_ratos/qut_total)*100))
print('Percentual de sapos: {:.2f} %'.format((qut_sapos/qut_total)*100))
