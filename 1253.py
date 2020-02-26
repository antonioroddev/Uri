for i in range(int(input())):
    frase = input()
    quant = int(input())
    nova_frase = ''
    for d in range(len(frase)):
        a = int(ord(frase[d])  - quant)
        if a < 65:
            a = 91 - (65 - a)
        
        nova_frase += chr(a)
        
    print(nova_frase)


