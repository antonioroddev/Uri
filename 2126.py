casos = 1
while True:
    contador = 0
    ult = 0
    try:

        str1 = input()
        str2 = input()

        var = 1
        for i in range (len(str2)):
            if len(str1)-1 * var < len(str2):
                if (str2[i:len(str1)-1 + var] == str1):
                    contador +=1
                    ult = i
            var +=1
        if len(str1) > len(str2):
            print("Caso #{}:\nNao existe subsequencia".format(casos))

        elif contador == 0:
            print("Caso #{}:\nNao existe subsequencia".format(casos))
        
        else:
           print("Caso #{}:\nQtd.Subsequencias: {}\nPos: {}".format(casos,contador,ult+1))     
            


    except EOFError:
        break
    casos +=1
    print()