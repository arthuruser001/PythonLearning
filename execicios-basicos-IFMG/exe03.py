# Considere a fórmula para cálculo de juros simples, J = (C × I × T) / 100, onde J, C, I e T correspondem a juros, capital, taxa e tempo, respectivamente. Construa um código que solicite ao usuário os valores de C, I e T e calcule J.

j = 0
c = 0
i = 0
t = 0

c = float(input('\033[2;0H\033[5 q\033[2J\033[1;30;47mDigite o Capital:\033[0m' + ' '))
i = float(input('\033[2;0H\033[2J\033[1;30;47mDigite a Taxa:\033[0m' + ' '))
t = float(input('\033[2;0H\033[2J\033[1;30;47mDigite o Tempo:\033[0m' + ' '))

j = (c * i * t)/100

print('\033[2;0H\033[2J\033[1;30;47mValor do Juros é:',j,'\033[0m')