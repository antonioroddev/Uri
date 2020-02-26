for i in range(int(input())):
    l = [float(i) for i in input().split()]  
    print('{:.1f}'.format((l[0] *2 + l[1] * 3 + l[2] * 5)/10))