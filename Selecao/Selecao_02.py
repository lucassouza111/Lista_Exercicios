# 2) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa. Caso o aluno não tenha feito a optativa deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o aluno foi aprovado, reprovado ou está em exame, de acordo com as informações abaixo:
# Aprovado : média >= 6.0 Reprovado: media < 3.0 Exame: média >= 3.0 e < 6.0

# entradas
nota01 = float(input("Qual o valor da 1ª nota? "))
nota02 = float(input("Qual o valor da 2ª nota? "))
notaOpt = float(input("Qual o valor da avaliação optativa? (se não tiver valor, colocar -1) "))

# processamento
def mediaFinal(nota1, nota2, notaOptativa):
    if notaOptativa > -1:
        if notaOptativa > nota1 and nota1 <= nota2:
            nota1 = notaOptativa
        elif notaOptativa > nota2:
            nota2 = notaOptativa
    return (nota1 + nota2) / 2

def situacaoFinal(med):
    if med >= 6:
        return "Aprovado"
    if med < 3:
        return "Reprovado"
    return "em Exame"

# saídas
media = mediaFinal(nota01, nota02, notaOpt)
print(f"No semestre, com a média {media}, o aluno está: {situacaoFinal(media)}")
