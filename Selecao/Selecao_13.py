# 13) Escreva um programa para ler um número inteiro (considere que serão lidos apenas valores positivos e inteiros) e escrever se é par ou ímpar.

#Entradas
numero = int(input("Escreva o número, para ser consultado: "))

#Processamento
sinal = "Par" if numero % int(2) == 0 else "Ímpar"

#Saídas
print(f"O número indicado é {sinal}.")
