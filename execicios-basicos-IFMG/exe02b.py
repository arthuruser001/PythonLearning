# Leia o Anterior

totalCalculado = 0
segundos = 0
minutos = 0
horas = 0

print('\033[37mH:M:S para SEGUNDOS: ')
horas = int(input('\033[36mDigite o valor em H: '))
minutos = int(input('\033[36mDigite o valor em M: '))
segundos = int(input('\033[36mDigite o valor em S: '))

totalCalculado = segundos
totalCalculado += minutos *  60
totalCalculado += horas * 3600

print('\033[30;47mValor em Segundos: ', totalCalculado)