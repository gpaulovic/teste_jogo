from random import randint
from time import sleep

def imprime_matriz(matriz):
    for linha in matriz:
        print(linha)

lista = []
jogos = []
print('-'*30)
print('      jogos da LOTOMANIA      ')
print('-'*30)
quant = int(input('Quantos jogos quer fazer?: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 100)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 50:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    matriz_jogo = [l[i:i+10] for i in range(0, len(l), 10)]
    imprime_matriz(matriz_jogo)
    sleep(0.5)

print('-='*5, '< Boa sorte! >', '-='*5)
