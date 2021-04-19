while True:
    try:
        valores = input().split(' ')
        hora = int(valores[0])/30
        minutos = int(valores[1])/6
        print('{:02.0f}:{:02.0f}'.format(hora, minutos))

    except EOFError:
        break