'''
Autor: Guilherme Saraiva
Objetivo: Jogo de adivinhar o número secreto.
'''
from random import randint

numero = randint(1,10)
vidas = 4
menu = 0

# inicia o jogo mostrando tela de menu com opções
while True:
    print()
    print(f"{'JOGO NÚMERO SECRETO':-^50}")
    print('''
1 - Tentar Adivinhar
2 - Dica
3 - Reiniciar Jogo
4 - Sair
''')    
    try:        
        menu = int(input('Digite o número da opção escolhida: '))
        print()
        if menu < 1 or menu > 4:            
            print('Digite um número entre 1 e 4.')
            continue
    except ValueError:        
        print('Opção inválida.')

    # tentando adivinhar o número secreto
    if menu == 1:
        print(f'\033[31mVIDAS: {vidas}\033[m')
        while True:
            try:
                jogada = int(input('Tente acertar o número: '))
                print()
                if jogada < 1 or jogada > 10:
                    print('Jogue um número entre 1 e 10.')
                    continue
                if jogada == numero:
                    print('PARABÉNS VOCÊ VENCEU!')
                    numero = randint(1,10)
                    vidas = 4
                    break                    
                elif jogada < numero:
                    print('Muito baixo!')
                    vidas -= 1
                    print(f'\033[31mVIDAS: {vidas}\033[m')
                    if vidas == 0:
                        print()
                        print('GAME OVER!')
                        numero = randint(1,10)
                        vidas = 4
                        break
                else:
                    print('Muito alto!')
                    vidas -= 1
                    print(f'\033[31mVIDAS: {vidas}\033[m')
                    if vidas == 0:
                        print()
                        print('GAME OVER!')
                        numero = randint(1,10)
                        vidas = 4
                        break
            except ValueError:
                print('Opção inválida!')

    # dicas do número secreto
    elif menu == 2:                
        continuar = input('Dica custa 1 vida. Continuar? [s/n] ').lower().strip()
        print()

        while continuar not in ('s','n'):                     
            print('INVALIDO')
            continuar = input('Dica custa 1 vida. Continuar? [s/n] ').lower().strip()

        if continuar == 's':
            if vidas <= 1:                
                print('GAME OVER')
                print()
                break
            if numero % 2 == 0:                
                print('\033[33mO número é par.\033[m')                               
            else:                
                print('\033[33mO número é ímpar.\033[m')     
            vidas -= 1
            print(f'\033[31mVIDAS: {vidas}\033[m')                          
               
        elif continuar == 'n':            
            print('\033[33mTudo bem.\033[m')
            print(f'\033[31mVIDAS: {vidas}\033[m')
                
    # reiniciando o jogo
    elif menu == 3:
            print()
            numero = randint(1,10)
            cont_jogada = 0
            vidas = 4
            print('Jogo reiniciado.')
            print(f'\033[31mVIDAS: {vidas}\033[m')

    # finalizando o programa
    else:
        break