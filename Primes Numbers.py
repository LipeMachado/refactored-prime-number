# -*- coding: utf-8 -*-
import os

run = 'running'

while run != 'finish':
    try:
        number = número = int(input('Digite um número para saber se ele é primo ou não: '))
    except ValueError:
        print('Value Error')
        
    é_primo = True
    divisoes = 2
    
    while divisoes < número and é_primo:
        if número % divisoes == 0:
            é_primo = False
        divisoes += 1
        
    if é_primo and número != 1:
        print(f'O {número} é primo.')
    else:
        print(f'O {number} não é primo.')
        
    try:
        choice = str(input('Deseja continuar testando? [s/n]: '))
    except ValueError:
        print('Value Error')
    
    if choice == 'S' or choice == 's':
        os.system("clear || cls")
    elif choice == 'N' or choice == 'n':
        run = 'finish'
    else:
        print('Incorret digit.')
        run = 'finish'