import math
for i in range(int(input())):
    string = input()
    if len(string) % 2 == 0:
        a = math.trunc(len(string)/ 2) - 1
    else:
        a = math.trunc(len(string)/ 2)
    nova_string = ''
    for d in range(len(string)):   
        if d <= a:
            valor = 2
        else:
            valor = 3
        if (65 <= ord(string[d]) <= 90) or (97 <= ord(string[d]) <= 122):
            c = ord(string[d]) + valor 
            nova_string += chr(c)
        else:
            if valor == 2:
                nova_string += chr(ord(string[d]) - 1)
            else:
                nova_string += string[d]
        
    print(nova_string[::-1])
    
