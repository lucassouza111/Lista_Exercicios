# 5) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

# entradas
valor = float(input("Escreva um valor qualquer: "))

# processamento
def ePositivo(val):
    if val >= 0:
        return True
    return False

#saídas
#resposta = "Positivo" if ePositivo(valor) == True else "Negativo"
resposta = "Positivo" if ePositivo(valor) else "Negativo"
print (f"O valor é {resposta}")
