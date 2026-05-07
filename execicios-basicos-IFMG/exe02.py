#  Escreva um código que receba um número de segundos e converta este número em horas, minutos e segundos. Escreva também um código que faça o contrário.

segundos = 0
minutos = 0
horas = 0

segundos = int(input('Digite o valor de tempo em segundo para recebe-lo em horas: '))

minutos = segundos // 60
horas = minutos //60

segundos %= 60
minutos %= 60

print('Horas: ' , horas , "Minutos: " , minutos , "Segundos: ", segundos)

# Concluido