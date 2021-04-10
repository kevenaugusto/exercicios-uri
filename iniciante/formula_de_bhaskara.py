from math import sqrt

variaveis = input().split(' ')

A = float(variaveis[0])
B = float(variaveis[1])
C = float(variaveis[2])

delta = B*B-4*A*C


if delta < 0 or (2*A) < 0:
    print('Impossivel calcular')
else:
    print('R1 = {:.5f}'.format((-B+sqrt(delta))/(2*A)))
    print('R2 = {:.5f}'.format((-B-sqrt(delta))/(2*A)))