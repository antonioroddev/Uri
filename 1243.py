while True:

    try:


        frase = input().split()
        contador = 0
        conta_palavras = 0
        for palavra in frase:
            flag = 0
            contador_l = 0
            for i in palavra:
                
                if  65 <= ord(i) <= 90 or  97 <= ord(i) <= 122:
                    contador_l += 1
                elif i == '.':
                    flag += 1
                else:
                    flag = 2
                    break
            
            if palavra[-1] == '.' and flag == 1:
                conta_palavras += 1
                contador += contador_l
            elif flag == 0:
                conta_palavras += 1
                contador += contador_l
                
        if conta_palavras > 0:
            contador = contador // conta_palavras
        
        else:
            contador = 0

        if contador <= 3:
            print(250)
        elif contador <= 5:
            print(500)
        else:
            print(1000)
    except EOFError:
        break