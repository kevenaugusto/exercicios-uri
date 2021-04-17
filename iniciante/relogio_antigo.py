while True:
    try:
        valores = input().split(' ')
        print('{:02.0f}:{:02.0f}'
                                .format(int(valores[0])/30, int(valores[1])/6))

    except EOFError:
        break