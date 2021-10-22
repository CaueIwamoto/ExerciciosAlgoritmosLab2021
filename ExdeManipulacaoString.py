#Exercício 1:
def contaPalavras(x):
    lista = x.split(" ")
    i=0
    while i < len(lista):
        i+=1
    return i
  
  #Exercício 2:
  def criptCesar(p, n):
    lista = []
    for i in p:
        x = ord(i)
        letra = x + n
        if (x >= 65  and x <= 90):
            if letra < 65:
                letra = 91 - (65 - letra)
            elif letra > 90 and letra < 97:
                letra = 64 + (letra - 90)
        elif (x >= 97  and x <= 122):
            if letra > 90 and letra < 97:
                letra = 123 - (97 - letra)
            elif letra > 122:
                letra = 96 + (letra - 122)
        else:
            letra = x
        lista.append((chr(letra)).upper())
    
    for i in lista:
        print(i, end="")
        
#Exercício 3:
def nomeCitacao(x):
    lista = x.split(" ")

    print(lista[len(lista) -1] + ",", end=" ")
    print(lista[0])
    
#Exercício 4:
def spellChecker(x):
    lista=[]
    nrec=[]
    arquivo = open("words.txt", "r")
    for i in arquivo.readlines():
        lista.append(i.lower().strip())
    fraselow = x.lower().replace(",","").split()
    for i in range(len(fraselow)):
        if fraselow[i] in lista:
            pass
        else:
            nrec.append(fraselow[i])
    return nrec
  
#Exercício 5:
