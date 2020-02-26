n = int(input())

for i in range(n):
    l = [int (i) for i in input().split()]

    print('{} cm2'.format(int((l[0]*l[1])/2)))