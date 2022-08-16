# Matheus Henrique Reich Favarin Zagonel

# Uniao de dois conjuntos:

def uniao(vetX,vetY):
    somaU = vetX + vetY

    tam = len(somaU)
    vetUniao = []

    for i in range(0, tam):
        if (somaU[i] not in vetUniao):
            vetUniao.append(somaU[i])
    return vetUniao

# INTERSECÇÃO

def inter(vetX,vetY):
    somaI = vetX + vetY

    tamI = len(somaI)
    vetInt = []

    for i in range(tamI):
        for j in range(i+1, tamI):
            if (somaI[i] == somaI[j]) and (somaI[i] not in vetInt):
                vetInt.append(somaI[i])
    return vetInt

# Diferença

def diff(vetX,vetY):
    dif = []
    for i in range(len(vetX)):
        if (vetX[i] not in vetY):
            dif.append(vetX[i])
    return dif

# PRODUTO CARTESIANO

def pcartesiano(elemento,vetY):
    tempX = []
    for i in (vetY):
        tempX.append([elemento, i])
    return tempX

def produto(vetX,vetY):
    res = []
    for j in (vetX):
        res.append([pcartesiano(j,vetY)])
    return res

#TRANSFORMO CONJUNTO EM STRING

def conjunto_string(x):
    element = ""
    for i in x:
        element += str(i) + ","
    return element[:-1]

#LEIO O ARQUIVO DE TEXTO

path = "./teste1.txt"

def main():
    file = open(path)

    linhas = file.readlines()

    numFun = int(linhas[0])

    for i in range(numFun):
        proxFun = linhas[1+i*3].strip('\n')

        conj1 = [x.replace("\n","") for x in linhas[2+i*3].split(",")]
        conj2 = [x.replace("\n","") for x in linhas[3+i*3].split(",")]

        if (proxFun == "U"):
            uniao_fun = uniao(conj1,conj2)

            x = conj1
            y = conj2
            z = uniao_fun

            print("União: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" % (conjunto_string(x),conjunto_string(y),conjunto_string(z)))

        elif (proxFun == "I"):
            inter_fun = inter(conj1,conj2)

            x = conj1
            y = conj2
            z = inter_fun

            print("Intersecção: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" % (conjunto_string(x),conjunto_string(y),conjunto_string(z)))

        elif (proxFun == "D"):
            dif_func = diff(conj1,conj2)

            x = conj1
            y = conj2
            z = dif_func

            print("Diferença: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" % (conjunto_string(x),conjunto_string(y),conjunto_string(z)))

        elif (proxFun == "C"):
            pcart_fun = produto(conj1,conj2)

            x = conj1
            y = conj2
            z = pcart_fun

            print("Produto Cartesiano: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" % (conjunto_string(x),conjunto_string(y),conjunto_string(z)))
        
    file.close

if __name__ == "__main__":
    main()