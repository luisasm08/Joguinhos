print('PEDRA PAPEL E TESOURA')
print('1)Pedra\n2)Papel\n3)Tesoura\n')
num = int(input('Jogador 1:\nEscolha um número:'))
import random

pc = random.randint(1, 3)
if pc == 1:
    print(f'O computador escolheu {pc}-pedra')
if pc == 2:
    print(f'O computador escolheu {pc}-papel')
if pc == 3:
    print(f'O computador escolheu {pc}-tesoura')
if pc==1 and num==1:
    print('EMPATE')
elif pc==2 and num==2:
    print('EMPATE')
elif pc==3 and num==3:
    print('EMPATE')
elif pc==1 and num==2:
    print('VOCÊ VENCEU')
elif pc==1 and num==3:
    print('COMPUTADOR VENCEU')
elif num==1 and pc==2:
    print('COMPUTADOR VENCEU')
elif num==1 and pc==3:
    print('VOCÊ VENCEU')
elif pc==2 and num==3:
    print('VOCÊ VENCEU')
elif num==2 and pc==3:
    print('COMPUTADOR VENCEU')
elif pc==3 and num==1:
    print('VOCÊ VENCEU')
elif pc==1 and num==3:
    print('COMPUTADOR VENCEU')