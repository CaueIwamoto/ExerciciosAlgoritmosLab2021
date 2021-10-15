#Exercício 1:
from math import *

carro = []
km=[]
i = 0
n = 0
while i < 5:
    carro.append(input())
    i += 1
while len(km)< len(carro):
    km.append(int(input()))

for indice in range(len(km)):
    if km[indice] == max(km):
        print(carro[indice])

while n < 5:
    print(round(1000/km[n]))
    n += 1

#Exercício 2:
numero = []
pos = []
neg = []

while True:
  num = int(input(''))
  if num == 0:
    break
  elif num > 0:
    pos.append(num)
  elif num < 0:
    neg.append(num)

for i in neg:
  numero.append(i)
for i in pos:
  numero.append(i)

  
print(numero)

#Exercício 3:
from math import *
x = []
soma = 0
dpi = 0
N = int(input('Qual o tamanho da lista: '))

print('Digite os valores:')
for i in range(N):
  x.append(float(input('')))

for i in x:
  soma += i
media = soma / len(x)

sun = 0
for i in x:
  sun += ((i-media)**2)
  dpi = sqrt((sun/N))

print('Média = {0:.2f} e Desvio = {1:.4f}'.format(media, dpi))


#Exercício 4:
num = []
n = 0
result = ''
# par = []
par = ''
# impar = []
impar = ''

while n < 20:
  num.append(int(input()))
  n+=1

for i in num:
  result += '{0} '.format(i)
  if i % 2 == 0:
    # par.append(i)
    par += '{0} '.format(i)
  else:
    # impar.append(i)
    impar += '{0} '.format(i)

print(result)
print(impar)
print(par)


#Exercício 5:
a = []
b = []
tam = int(input('Digite a dimensão dos vetores: '))
soma = 0
n = 0
m = 0

print('Digite o vetor 1:')
while n < tam:
  a.append(int(input()))
  n+=1

print('Digite o vetor 2:')
while m < tam:
  b.append(int(input()))
  m += 1
  
for i, j in zip(a, b):
  # for j in range(len(b)):
    soma += i * j

print(soma)

#Exercício 6:
def quadrado(lista):
  listaQuadrada = []
  for i in lista:
    listaQuadrada.append(i**2)
  return listaQuadrada
