def verifica_quimicos(lista,string):
    var = 0

    for i in range(len(string)):
        for d in lista:

            if len(d) + var  < len(string):
                if string[i:len(d) + var] == d and  60 <= ord(string[len(d) + var]) <= 90:
                    return True
            else:
                if string[i:len(d) + var] == d:
                    return True
        var += 1

    return False


n = int(input())

for i in range(0,n):
    lista_quimicos = []
    qut_quimicos = int(input())
    for a in range(qut_quimicos): 
        lista_quimicos.append(input())
    lista_result = []
    qut_prod = int(input())
    for a in range(qut_prod):
        string = input()
        if verifica_quimicos(lista_quimicos, string) == True:
            lista_result.append("Abortar")
        else:
            lista_result.append("Prossiga")

    for a in lista_result:
        print(a)
    if i != n -1:
        print()
