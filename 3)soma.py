def calcular_soma():
    indice = 12
    soma = 0
    k = 1
    while k < indice:
        k += 1
        soma += k
    return soma

resultado = calcular_soma()
print(f"O valor da variável SOMA é: {resultado}")
