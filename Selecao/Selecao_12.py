# 12) Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:
  # - para homens : (72.7 * h) – 58
  # - para mulheres : (62.1 * h) – 44.7
  # Observação: Altura = h (na fórmula acima).

#Entradas
altura = float(input("Informe a sua altura, em metros: "))
sexo = str(input("Informe qual o seu gênero (M/F): "))

#Processamento
def eFeminino():
    if sexo == "F":
        return True
    return False

calculo = ((62.1 * altura) - 44.7) if eFeminino() else ((72.7 * altura) - 58)

#Saídas
print(f"O seu peso ideal é: {calculo}")
