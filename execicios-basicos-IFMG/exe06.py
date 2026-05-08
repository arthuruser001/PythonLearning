# Calcular o imposto de renda de um salário considerando as seguintes alíquotas:
# Até R$ 1.903,98: isento;
# De R$ 1.903,99 até R$ 2.826,65: 7,5%;
# De R$ 2.826,66 até R$ 3.751,05: 15%;
# De R$ 3.751,06 até R$ 4.664,68: 22,5%;
# Acima de R$ 4.664,68: 27,5%.

salario = float(input('Digite o seu salário: '))
if salario < 1903.99:
  print('Seu imposto de renda é isento.')
elif salario < 2826.66:
  print('Seu imposto de renda é ', (salario/100)*7.5)
elif salario < 3751.06:
  print('Seu imposto de renda é ', (salario/100)*15)
elif salario < 4664.68:
  print('Seu imposto de renda é ', (salario/100)*22.5)
else:
  print('Seu imposto de renda é ', (salario/100)*27.5)