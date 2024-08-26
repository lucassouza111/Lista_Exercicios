# 1) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência conforme a tabela abaixo:
#Observação: Caso o código não seja nenhum dos especificados o produto deve ser encarado como Importado.

# Entradas
cod = int(input ("Entre com o Código: "))

#Processamento
def obterRegiao (codigo):
    print (codigo)
    codigo = codigo + 2
    match codigo:
        case 1:
            return "Sul"
        case 2:
            return "Norte"
        case 3:
            return "Leste"
        case 4:
            return "Oeste"
        case 5 | 6:
            return "Nordeste"
        case 7 | 8 | 9:
            return "Sudeste"
        case 10:
            return "Centro-Oeste"
        case 11:
            return "Noroeste"
        case _:
            return "Importado"

#Saídas
print ("Este produto é de origem", obterRegiao (cod), ".")
print (cod)