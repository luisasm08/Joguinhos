print('JOGO PAR OU ÍMPAR')

while True:
    valor = input('Você quer par ou ímpar?').lower()
    import random

    pc = random.randint(0, 10)
    num = int(input('Escolha um número de 1 a 10:'))
    if valor == "par" and (num + pc) % 2 == 0:
        print(f'O computador escolheu {pc}\nVocê venceu!')
    if valor == "par" and (num + pc) % 2 != 0:
        print(f'O computador escolheu {pc}\nVocê perdeu!')
        break
    if valor == "ímpar" and (num + pc) % 2 == 0:
        print(f'O computador escolheu {pc}\nVocê perdeu!')
        break
    if valor == "ímpar" and (num + pc) % 2 != 0:
        print(f'O computador escolheu {pc}\nVocê venceu!')
