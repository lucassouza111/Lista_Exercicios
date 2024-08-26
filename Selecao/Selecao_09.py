# 9) As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

# Entradas
qtdMaca = int(input("Quantas maças serão compradas? "))

#Processamento
def calculaCompra(quantMaca, valorUnitario):
    return quantMaca * valorUnitario

def obterValorUnitario(quantMaca):
    if quantMaca > 11:
        return 0.25
    return 0.30

#Saídas
valorUnitario = obterValorUnitario(qtdMaca)
resposta = str(calculaCompra(qtdMaca, valorUnitario))
print(f"O valor total da compra é de: R$ {resposta.replace('.',',')}")
