# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

#Entradas
valor1 = int(input("Insira o 1º valor: "))
valor2 = int(input("Insira o 2º valor: "))
valor3 = int(input("Insira o 3º valor: "))

#Processamento
if(valor1 > valor2):
      temp = valor1
      valor1 = valor2
      valor2 = temp
 
if(valor1 > valor3):
       temp = valor1
       valor1 = valor3
       valor3 = temp

if(valor2 > valor3):
       temp = valor2
       valor2 = valor3
       valor3 = temp

#Saídas
print(valor1, valor2, valor3)
