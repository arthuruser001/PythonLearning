# Criar uma função para resolver equações de segundo grau retornando as raízes dentro de uma tupla. Crie também um função principal para receber os termos A, B e C da equação e mostrar o resultado para o usuário.

a = 0
b = 0
c = 0

raizes = (0,0)

def start():
  global a
  global b
  global c
  a = int(input('Digite o valor do coeficiente A: '))
  b = int(input('Digite o valor do coeficienteB: '))
  c = int(input('Digite o valor do coeficiente C: '))
  return a , b , c

def calculate(a, b, c):
  delta = b**2-(4*a*c)
  x1 = (-b +  (delta ** 0.5)) / (2 * a)
  x2 = (-b -  (delta ** 0.5)) / (2 * a)
  if delta < 0:
    print('Essa equação não possui raizes reais')
    return "Erro! Delta < 0"
  raizes = (x1,x2)
  return raizes

def finish(raizes):
  print('As raízes da equação são ', raizes)


def main():
  try:
    a, b, c = start()
  except:
    print('Algum valor inváildo foi digitado!')
    return -1

  if calculate(a,b,c) == "Erro! Delta < 0":
    return -1
  else:
    raizes = calculate(a,b,c)

  finish(raizes)

if __name__ == "__main__":
  main()