conta_dentro = 0
conta_fora = 0
for i in range(int(input())):
    x = int(input())

    if 10<=x<=20:
        conta_dentro +=1
    else:
        conta_fora += 1

print('{} in'.format(conta_dentro))
print('{} out'.format(conta_fora))
        