notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

saque = float(input(''))

print('NOTAS:')
for nota in notas:
    quantidade_notas = int(saque / nota)
    print('{} nota(s) de R$ {:.2f}'. format(quantidade_notas, nota))
    saque -= quantidade_notas * nota

print('MOEDAS:')
for moeda in moedas:
    quantidade_moedas = int(round(saque, 2) / moeda)
    print('{} moeda(s) de R$ {:.2f}'. format(quantidade_moedas, moeda))
    saque -= quantidade_moedas * moeda

