# Escreva um módulo com funções para calcular o máximo divisor comum (MDC) e o mínimo múltiplo comum (MMC) de dois números. Para o MDC, você deve adaptar o algoritmo de Euclides já estudado. No caso do MMC, pode ser usada a fórmula MMC(n1, n2) = n1 * n2 / MDC(n1, n2). Implemente também um script com chamadas a essas funções sobre números digitados pelo usuário.

def MMC(n1, n2):
  return n1 * n2 / MDC(n1, n2)

def MDC(n1, n2):
  while True:
    resto = n1 % n2
    if resto == 0:
      mdc = n2
      break
    else:
      n1 = n2
      n2 = resto
  return mdc

def main():
  ans = int(input('Você deseja calcular o MMC ou o MDC?\n1-MMC\n2-MDC\n'))
  if ans == 1:
    try:
      n1 = int(input('Digite o primeiro e maior número: '))
      n2 = int(input('Digite o segundo e menor número: '))
      print('O MMC dos números fornecidos é ',MMC(n1, n2))
    except:
      print('Erro! Algum valor inválido foi digitado.')
  if ans == 2: 
    try:
      n1 = int(input('Digite o primeiro e maior número: '))
      n2 = int(input('Digite o segundo e menor número: '))
      print('O MDC dos números fornecidos é ',MDC(n1, n2))
    except:
      print('Erro! Algum valor inválido foi digitado.')

if __name__ == "__main__":
    main()