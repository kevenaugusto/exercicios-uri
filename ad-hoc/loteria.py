aposta = input().split(' ')
sorteio = input().split(' ')
qnt_acerto = 0

for i in range(6):
    if sorteio.pop() in aposta:
        qnt_acerto += 1
    
if qnt_acerto == 3:
    print('terno')
elif qnt_acerto == 4:
    print('quadra')
elif qnt_acerto == 5:
    print('quina')
elif qnt_acerto == 6:
    print('sena')
else:
    print('azar')