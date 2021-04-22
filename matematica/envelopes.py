qnt_testes = int(input())

for i in range(qnt_testes):
    dimensoes = input().split(' ')
    dimensoes.reverse()

    dim1 = int(dimensoes.pop())
    dim2 = int(dimensoes.pop())
    dim3 = int(dimensoes.pop())
    dim4 = int(dimensoes.pop())
    
    if (dim1 < dim3 and dim2 < dim4) or (dim2 < dim3 and dim1 < dim4):
        print('S')
    else:
        print('N')