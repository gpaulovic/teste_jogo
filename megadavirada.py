import sqlite3
from random import randint
from time import sleep

def create_table():
    conn = sqlite3.connect('megadavirada.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numeros TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_jogo(jogo):
    conn = sqlite3.connect('megadavirada.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO jogos (numeros) VALUES (?)', (' '.join(map(str, jogo)),))
    conn.commit()
    conn.close()

def check_duplicate(jogo):
    conn = sqlite3.connect('megadavirada.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM jogos WHERE numeros = ?', (' '.join(map(str, jogo)),))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def imprime_lista(jogo):
    print(', '.join(map(str, jogo)))

lista = []
jogos = []
create_table()

print('-'*30)
print('    jogos da MEGA DA VIRADA    ')
print('-'*30)
quant = int(input('Quantos jogos quer fazer?: '))
total = 1

while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()

    if not check_duplicate(lista):
        jogos.append(lista[:])
        save_jogo(lista)
        total += 1

    lista.clear()

print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    imprime_lista(l)
    sleep(0.5)

print('-='*5, '< Boa sorte na MEGA DA VIRADA! >', '-='*5)
