qnt = int(input())

aux1 = 1
aux2 = 2
fibo = None

for i in range(qnt):
    if i >= 4:
        fibo = aux1+aux2
        print(' {}'.format(fibo), end='')
        aux1 = aux2
        aux2 = fibo
    elif i == 3:
        print(' 2', end='')
    elif i > 0 and i < 3:
        print(' 1', end='')
    else:
        print('0', end='')

print()