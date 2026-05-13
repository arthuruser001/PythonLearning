#  Implemente um módulo com as funções: ano_bissexto(ano), retorna True se o ano for bissexto e False, em caso negativo; dias_mes(ano, mes): retorna a quantidade de dias do mês, deve usar a função ano_bissexto(). Construa um script que receba uma data do usuário (mês e ano) e mostre o resultado das funções implementadas.

qtdDiasMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def anoBissexto(ano):
  if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) and (ano > 0):
    return True
  else:
    return False
  
def diasMes(ano, mes):
  if anoBissexto(ano) == False:
    return qtdDiasMes[mes]
  else:
    if mes == 2:
      return 29
    else: 
      return qtdDiasMes[mes]

def main():
  mes = int(input('Digite o mes: '))
  ano = int(input('Digite o ano: '))
  print('A quantidade de dias do seu mês é {}'.format(diasMes(ano, mes)))

if __name__ == "__main__":
    main()