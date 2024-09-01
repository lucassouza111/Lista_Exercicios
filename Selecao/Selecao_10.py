# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

#Entradas
valor1 = int(input("Insira o 1º valor: "))
valor2 = int(input("Insira o 2º valor: "))
valor3 = int(input("Insira o 3º valor: "))

#Processamento
def compararNumeros(val,valComparar):
    if val > valComparar:
        return True
    return False

def trocarNumeros(val,valTrocar):
    valBackup = val
    return val == valTrocar and valTrocar == valBackup

#print(trocarNumeros(valor1,valor2))
print(valor1)
valor1 = trocarNumeros(valor1,valor2) if compararNumeros(valor1,valor2) else valor1
print(valor1)



#Saídas
print(valor1,valor2,valor3)
