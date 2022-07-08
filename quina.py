from random import randint
from time import sleep
lista = []
jogos = []
print('-'*30)
print('      jogos da QUINA      ')
print('-'*30)
quant = int(input('Quantos jogos quer fazer?: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1,80)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=5:
            break
    lista.sort()
    jogos.append(lista [:])
    lista.clear()
    total +=1
print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('-='*5, '< Boa sorte! >', '-='*5)