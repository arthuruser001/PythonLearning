# Construir um script capaz de calcular a velocidade média de uma viagem a partir das velocidades de cada trecho. O usuário deve informar o número de trechos e, em seguida, informar a distância e velocidade de cada trecho. O cálculo da velocidade média é feito somando o produto da distância pela velocidade de cada trecho e dividindo essa soma pela soma das distâncias. Após o cálculo da velocidade média, o programa deve os trechos com velocidade acima da média

trechos = 0
distanciaPorTrecho = []
velocidadePorTrecho = []

i = 0
distanciaTotal = 0
tempoTotal = 0
velocidadeMedia = 0


def inputValues(i):
  i = 1

  trechos = int(input('Digite o número de trechos: '))
  for i in range(trechos):
    distanciaPorTrecho.append(int(input('Digite a distância do trecho {} '.format(i + 1))))
  i = 1
  for i in range(trechos):
    velocidadePorTrecho.append(int(input('Digite a Velocidade Média do trecho {} '.format(i + 1))))
  return distanciaPorTrecho, velocidadePorTrecho, trechos

def calcularVelociadeMedia(trechos, distanciaPorTrecho, velocidadePorTrecho):
  distanciaTotal = 0
  tempoTotal = 0
  for i in range(trechos):
    distanciaTotal += distanciaPorTrecho[i]
    tempoTotal += distanciaPorTrecho[i] * velocidadePorTrecho[i]
  return tempoTotal / distanciaTotal

def finalizar(velocidadeMedia):
  print('Velocidade média é {}'.format(velocidadeMedia))

def main():
  distanciaPorTrecho, velocidadePorTrecho, trechos = inputValues(i)
  velocidadeMedia = calcularVelociadeMedia(trechos, distanciaPorTrecho, velocidadePorTrecho)
  finalizar(velocidadeMedia)

if __name__ == "__main__":
  main()