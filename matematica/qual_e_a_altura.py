from math import sqrt

qnt_testes = int(input())

for i in range(qnt_testes):
    coeficientes = input().split(' ')
    coeficientes.reverse()

    a = int(coeficientes.pop())
    b = int(coeficientes.pop())
    c = int(coeficientes.pop())

    delta = b*b-(4*a*c)

    print('{:.2f}'.format((-delta)/(4*a)))