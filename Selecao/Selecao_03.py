# 3) Escreva um programa para ler as notas das duas avaliações de um aluno no semestre, calcular e escrever a média semestral e a seguinte mensagem: PARABÉNS! Você foi aprovado! somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação)

# entradas
nota01 = float(input("Qual o valor da 1ª nota, do semestre? "))
nota02 = float(input("Qual o valor da 2ª nota, do semestre? "))

# processamento
def mediaSem(nota1, nota2):
    return (nota1 + nota2) / 2

def situacaoFinal(med):
    if med >= 6:
        return "PARABÉNS! Você foi aprovado!"
    return "Não foi alcançado a nota mínima exigida."

# saídas
media = mediaSem(nota01, nota02)
print(f"No semestre a sua média foi de {media}. {situacaoFinal(media)}")
