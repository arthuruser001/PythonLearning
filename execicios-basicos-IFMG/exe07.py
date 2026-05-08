# Leia uma quantidade indeterminada de números. A cada número informado, o usuário deve informar se deseja continuar ou parar. Ao final, o código deve retornar o maior e o menor número recebido.

n = 0
maior = 0
menor = 0
total = 0
resposta = ''
continuar = True

while continuar:
  n = int(input('Digite um número: '))
  resposta = input('Você deseja continuar (s ou n)?')

  if n > maior:
    maior = n
  if n < menor:
    menor = n

  if resposta == 's':
    continuar = True
  else:
    continuar = False

print('O maior número é {} e o menor é {}'.format(maior, menor))