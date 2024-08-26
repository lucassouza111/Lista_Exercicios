# 6) Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for digitado o valor zero, escrever a palavra zero.

# entradas
valor = float(input("Escreva um valor qualquer: "))

# processamento
def ePositivo(val):
    if val > 0:
        return True
    return False

def verificaNumero(val):
    if val == 0:
        return "Zero"
    return "Positivo" if ePositivo(val) else "Negativo"

#saídas
resposta = verificaNumero(valor)
print (f"O valor é {resposta}")
