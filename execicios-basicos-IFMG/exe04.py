# Receber três números e informar o maior deles.

n1 = 0
n2 = 0
n3 = 0

n1 = int(input('\033[2J\033[4;37;42m\033[3;2HDigite o primeiro número: \033[0m\033[?25l'))
n2 = int(input('\033[2J\033[4;37;42m\033[3;2HDigite o primeiro número: \033[0m\033[?25l'))
n3 = int(input('\033[2J\033[4;37;42m\033[3;2HDigite o primeiro número: \033[0m\033[?25l'))

if n1 > n2 and n1 > n3:
  print('\033[2J\033[4;37;42m\033[3;2HO Maior numero é ',n1,'\033[0m')