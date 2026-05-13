# Crie a função input_int(mensagem) semelhante à função input(). A função deve receber uma mensagem, exibi-la ao usuário e garantir que o número digitado seja válido. Enquanto o usuário digitar um número inválido, a função deve informar o erro e solicitar e digitação novamente. Dica: utilize a instrução try.

def input_int(msg):
  try:
    return int(input(msg))
  except:
    print('Você digitou algum número incorretamente ou inválidamente. Tente novamente')

input_int('Digite um número: ')