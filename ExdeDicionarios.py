#Exercício 1:
def converte(dicionario, frase):
    frase = frase.upper()
    frase_morse = []

    for i in frase:
        if i in dicionario:
            frase_morse.append(dicionario[i] + " ")

    return "".join(frase_morse)
 
#Exercício 2:

#Exercício 3:
