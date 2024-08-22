# 5) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

# entradas
valor = int(input("Escreva um valor qualquer: "))

# processamento
resposta = ""
if valor >= 0:
    resposta = "Positivo"
else:
    resposta = "Negativo"

#saídas
print ("O valor é ", resposta)
