valor = input().split('.')

notas = int(valor[0])
moedas = int(valor[1])

# Tratando as Notas:

cem = notas//100
notas %= 100

cinquenta = notas//50
notas %= 50

vinte  = notas//20
notas %= 20

dez = notas//10
notas %= 10

cinco = notas//5
notas %= 5

dois = notas//2
notas %= 2

# Tratando as moedas:

m_um = notas

m_cinquenta = moedas//50
moedas %= 50

m_vintecinco = moedas//25
moedas %= 25

m_dez = moedas//10
moedas %= 10

m_cinco = moedas//5
moedas %= 5

m_umcentavo = moedas

# Exibindo os resultado

print('NOTAS:\n{} nota(s) de R$ 100.00'.format(cem))
print('{} nota(s) de R$ 50.00'.format(cinquenta))
print('{} nota(s) de R$ 20.00'.format(vinte))
print('{} nota(s) de R$ 10.00'.format(dez))
print('{} nota(s) de R$ 5.00'.format(cinco))
print('{} nota(s) de R$ 2.00'.format(dois))

print('MOEDAS:\n{} moeda(s) de R$ 1.00'.format(m_um))
print('{} moeda(s) de R$ 0.50'.format(m_cinquenta))
print('{} moeda(s) de R$ 0.25'.format(m_vintecinco))
print('{} moeda(s) de R$ 0.10'.format(m_dez))
print('{} moeda(s) de R$ 0.05'.format(m_cinco))
print('{} moeda(s) de R$ 0.01'.format(m_umcentavo))