# Simular uma calculadora simples. O código deve solicitar ao usuário a operação desejada (soma, multiplicação, divisão, subtração ou potência) ou então sair. Quando o usuário escolher uma operação, o código deve solicitar dois números, realizar a operação sobre estes números e exibir o resultado. O código deve sempre solicitar uma nova operação até que o usuário escolha sair

n1 = 0
n2 = 0
res = 0
ans = ''
continuar = True

while continuar:
  ans = input('Digite um número para escolher a operação: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nDigite... ')
  if ans == '1':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número'))
    print('Resultado: ', res)
    res = n1 + n2
  if ans == '2':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número'))
    res = n1 -n2
    print('Resultado: ', res)
  if ans == '3':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número'))
    res = n1 * n2
    print('Resultado: ', res)
  if ans == '4':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número'))
    res = n1 / n2
    print('Resultado: ', res)
  ans = input('Você deseja continuar?(s ou n) ')
  if ans == 's':
    continar = True
  else:
    continuar = False