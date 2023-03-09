numero = 0

while numero < 10:
    if numero == 0: 
        print(' o número', numero, 'é zero!')
        print('------------------------------\n')
    elif numero % 2 == 0:
        print('o número', numero, 'é par!')
        print('------------------------------\n')
    else:
        print('o número', numero, 'é ímpar!')
        print('------------------------------\n')
    numero += 1