from os import system
from time import sleep

class color():
    cyan = '\033[1;36m'
    yellow = '\033[1;33m'
    red = '\033[91m'
    green = '\033[92m'
    white = '\033[1;97m'

def clear():
    system('cls')

def espera():
    sleep(2)

def main():
    secret = 'gostosa'
    digitados = []
    chances = 3


    while True:
        if chances <= 0:
            print(color.red + 'Você perdeu ;-;')
            break

        letra = input(color.white + 'Digite uma letra: ')

        letra = letra.lower()

        clear()

        if len(letra) > 1:
            print(color.red + 'Digite apenas uma letra!!!')
            espera()
            clear()
            continue

        digitados.append(letra)

        if letra in secret:
            print(color.green + f'Nice\nA letra {letra} está na palavra')
            espera()
            clear()
        else:
            print(color.red + f'Fuck\nA letra {letra} não se encontra na palavra\n')
            chances -= 1
            digitados.pop()
            print(f'Você ainda tem {chances} chances')
            espera()
            clear()

        secret_temp = ''
        for letra_secreta in secret:
            if letra_secreta in digitados:
                secret_temp += letra_secreta
            else:
                secret_temp += '*'

        if secret_temp == secret:
            clear()
            print(color.cyan + 'Boa vc ganhou...\nA palavra era' + color.green + f' {secret.upper()}'+ color.white)
            break
        else:
            print(color.yellow + f'A palavra secreta esta assim {secret_temp}')

if __name__ == '__main__':
    main()