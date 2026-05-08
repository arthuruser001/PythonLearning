# Calcule o fatorial de um número. O fatorial de um número n, representado por n!, é calculado como n! = n × (n − 1) × ... × 2 × 1. Sendo que 1! = 0! = 1.

n = 0
nF = 1

n = int(input('Digite um número: '))

for count in range(1, n + 1):
  nF *= count

print('A fatorial do número é: ', nF)