# 2) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa. Caso o aluno não tenha feito a optativa deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o aluno foi aprovado, reprovado ou está em exame, de acordo com as informações abaixo:
# Aprovado : média >= 6.0 Reprovado: media < 3.0 Exame: média >= 3.0 e < 6.0

# entradas
nota01 = float(input("Qual o valor da 1ª nota? "))
nota02 = float(input("Qual o valor da 2ª nota? "))
notaOpt = float(input("Qual o valor da avaliação optativa? (se não tiver valor, colocar zero) "))

# processamento
def mediaFinal():
    nota011 = 0
    if notaOpt == 0:
        notaOpt == -1
    elif nota01 < nota02:
        nota011 == notaOpt
    else:
        nota02 == notaOpt
    
    return (nota011 + nota02) / 2

def situacaoFinal():
    if mediaFinal() >= 6:
        return "Aprovado"
    elif mediaFinal() < 3:
        return "Reprovado"
    else:
        return "em Exame"

# saídas
print("No semestre, com a média ", mediaFinal(), ", o aluno está: ", situacaoFinal())
