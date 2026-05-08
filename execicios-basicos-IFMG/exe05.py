# Testar se um número é ímpar ou par, sem usar o operador %

n = int(input('Digite um número: '))

if n & 1 == 0:
  print('O número é par')
else:
  print('O número é impar')