# Escrever um código para receber uma lista de números. Percorrer a lista e utilizar um dicionário para sumarizar a quantidade de vezes que cada número aparece na lista

numeros = []
vezes = {}
i = 0
ans = ''
continuar = True

def inputValues(continuar, numeros):
    while continuar:
        numeros.append(int(input("Digite o numero para o adicionar ")))
        ans = input("Deseja continuar? (s ou n) ")
        if ans == 's':
            continuar = True
        elif ans == 'n':
            continuar = False
    return numeros
            
def getRepetitionTimes(numeros, vezes):
    for i in numeros:
        vezes[i] = vezes.get(i, 0)
        vezes[i] += 1
    return vezes

def output(vezes):
    print("Dos valores informados, houveram as repetições:")
    print(vezes)

def main(continuar, numeros, vezes):
    numeros = inputValues(continuar, numeros)
    vezes = getRepetitionTimes(numeros, vezes)
    output(vezes)

if __name__ == "__main__":
    main(continuar, numeros, vezes)