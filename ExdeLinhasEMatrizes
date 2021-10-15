#Exercício 1:
M = []
maior = 0

for num_linha in range(2):
    linha = []
    for num_coluna in range(2):
        linha.append(int(input('Digite o elemento da linha %d e coluna %d: ' % (num_linha,num_coluna))))
    M.append(linha)

for linha in range(2):
    for coluna in range(2):
        if M[linha][coluna] > maior:
            maior = M[linha][coluna]

print('Matriz resultante:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        M[linha][coluna] = M[linha][coluna] * maior
        print('%3d' % M[linha][coluna], end=' ')
    print()

#Exercício 2:
loja=[]
prod=[]
preço=[]



for iloja in range(3):
    loja.append(input("Digite o nome da loja: "))

for iprod in range(5):
    prod.append(input("Digite o nome do produto: "))

for iloja in range(3):
    linha=[]
    for iprod in range(5):
        linha.append(int(input("Digite o preco do produto {0} na loja {1}: " .format(iprod, iloja))))
    preço.append(linha)


print("\nLojas:")
for iloja in range(3):
    print(loja[iloja])

print("\nProdutos:")
for iprod in range(5):
    print(prod[iprod])

print("\nPreços:")
for iloja in range(3):
    for iprod in range(5):
        print("{0:3d}".format(preço[iloja][iprod]), end=" ")
    print()

print("\nPreços menores que R$ 50.00:")
for iloja in range(3):
    for iprod in range(5):
        if preço[iloja][iprod] < 50:
            print("Loja: {0}, produto {1} e preço {2}".format(loja[iloja], prod[iprod], preço[iloja][iprod]))
    print()

#Exercício 3:
from random import randint
M = []
somatoria = []
soma = 0

for num_linha in range(20):
    linha = []
    for num_coluna in range(10):
        linha.append(randint(0, 10))
    M.append(linha)

print('Matriz original:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print('%3d' % M[linha][coluna], end=' ')
    print()

print('\nVetor com a somatória de cada linha:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        soma = soma + M[linha][coluna]
    somatoria.append(soma)
print(somatoria)

print('\nmatriz depois da multiplicação:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        M[linha][coluna] = M[linha][coluna] * somatoria[linha]
        print('%5d' % M[linha][coluna], end=' ')
    print()

#Exercício 4:
M = []
i = 0

for num_linha in range(4):
    linha = []
    for num_coluna in range(2):
        linha.append(int(input('Digite o elemento da linha %d e coluna %d: ' % (num_linha,num_coluna))))
    M.append(linha)

print('Matriz original:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print('%3d' % M[linha][coluna], end=' ')
    print()
print()
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        if M[linha][coluna] > 10:
            print('%d é maior que 10!' % M[linha][coluna])
            i += 1
print('No total, %d elementos são maiores que 10!' % i)

print('\nMatriz sem os números maiores que 10:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        if M[linha][coluna] > 10:
            M[linha][coluna] = 0
        print('%3d' % M[linha][coluna], end=' ')
    print()
