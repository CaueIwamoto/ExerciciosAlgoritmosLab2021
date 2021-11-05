#Exercício 1:
def converte(dicionario, frase):
    frase = frase.upper()
    frase_morse = []

    for i in frase:
        if i in dicionario:
            frase_morse.append(dicionario[i] + " ")

    return "".join(frase_morse)
 
#Exercício 2:
def contaPalavras(frase):
  incidencia = {}

  lista = frase.replace('?', '').replace('!', '').replace(',', '').strip().split(' ')

  for i in range(len(lista)):
    if lista[i].lower() in incidencia:
      incidencia[lista[i].lower()] = incidencia[lista[i].lower()]+1
    else:
      incidencia[lista[i].lower()] = 1

  return incidencia

#Exercício 3:
centena = {
    "1" : "cento",
    "2" : "duzentos",
    "3" : "trezentos",
    "4" : "quatrocentos",
    "5" : "quinhentos",
    "6" : "seiscentos",
    "7" : "setecentos",
    "8" : "oitocentos",
    "9" : "novecentos"
}
dezena = {
    "1" : "dez",
    "2" : "vinte",
    "3" : "trinta",
    "4" : "quarenta",
    "5" : "cinquenta",
    "6" : "sessenta",
    "7" : "setenta",
    "8" : "oitenta",
    "9" : "noventa"
}
unidade = {
    "1" : "um",
    "2" : "dois",
    "3" : "três",
    "4" : "quatro",
    "5" : "cinco",
    "6" : "seis",
    "7" : "sete",
    "8" : "oito",
    "9" : "nove",
    "10" : "dez"
}
dez = {
    "1" : "onze",
    "2" : "doze",
    "3" : "treze",
    "4" : "quatorze",
    "5" : "quinze",
    "6" : "dezeseis",
    "7" : "dezesete",
    "8" : "dezoito",
    "9" : "dezenove"
}
def numero_texto (numero):
    if numero == 100:
        print("cem")
    elif 0 < numero <= 10:
        print(unidade[str(numero)])
    else:
        texto = ""
        numero = [int(a) for a in str(numero)]
        if len(numero) == 3:
            texto = centena[str(numero[0])]
            numero.pop(0)
            if numero[0] != 0 or numero[1] != 0:
                texto += " e "
        if numero[0] == 1 and numero[1] != 0:
            texto += dez[str(numero[1])]
        else:
            if numero[0] != 0:
                texto += dezena[str(numero[0])]
                if numero[1] != 0:
                    texto += " e "
            if numero[1] != 0:
                texto += unidade[str(numero[1])]
        print(texto)
