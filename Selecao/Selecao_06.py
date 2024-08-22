# 6) Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for digitado o valor zero, escrever a palavra zero.

# entradas
valor = int(input("Escreva um valor qualquer: "))

# processamento
resposta = ""
if valor == 0:
    resposta = "Zero"
elif valor > 0:
    resposta = "Positivo"
else:
    resposta = "Negativo"

#saídas
print ("O valor é ", resposta)
