# Receber três números e informar o maior deles.

n1 = 0
n2 = 0
n3 = 0

n1 = int(input('\033[2J\033[4;37;42mDigite o primeiro número: \033[0m\033[?25l'))
n2 = int(input('\033[2J\033[4;37;42mDigite o segundo número: \033[0m\033[?25l'))
n3 = int(input('\033[2J\033[4;37;42mDigite o teceiro número: \033[0m\033[?25l'))

if n1 > n2 and n1 > n3:
  print('\033[2J\033[4;37;42mO Maior numero é ',n1,'\033[0m')
if n2 > n1 and n2 > n3:
  print('\033[2J\033[4;37;42mMaior numero é ',n2,'\033[0m')
if n3 > n1 and n3 > n2:
  print('\033[2J\033[4;37;42mO Maior numero é ',n3,'\033[0m')