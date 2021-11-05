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
