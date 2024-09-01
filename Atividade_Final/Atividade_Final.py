# Desenvolva um programa em sua linguagem de programação que simule o sorteio de um concurso da Mega-Sena.
# A Mega-Sena é uma loteria onde 6 números diferentes são sorteados de um conjunto de 60 números (de 1 a 60). O programa deve atender aos seguintes requisitos:
# 1. Geração de números sorteados:
    # Gere Aleatoriamente 6 números distintos entre 1 e 60.
    # Exiba esses números na tela em ordem crescente.
# 1. Entrada do usuário:
    # Pedir que você insira sua aposta, que é composta por 6 números distintos entre 1 e 60.
# 1. Verificação de resposta corretas:
    # Compare os números sorteados com os números que você aposta.
    # Vou te dizer quantos números você acertou.
# 1. Prêmios:
    # Vou mostrar o número de acertos e, de acordo com as regras da Mega-Sena, indicar o prêmio fictício:
    # 4 hits: Quadra
    # 5 acertos: Quina
    # 6 acertos: sena
    # Se você não tiver pelo menos 4 acertos, exibirei uma mensagem informando que você não ganhou.
# 1. Repita: (Opcional)
    # Vou perguntar se você deseja realizar um novo sorteio. Em caso afirmativo, reinicie o processo; Caso contrário, encerre o programa.
# Dicas
    # Use funções para separar a lógica de geração de números, inserção de dados do usuário e verificação de respostas corretas.
    # Use estruturas de repetição para validar a entrada do usuário e garantir que 6 números válidos e distintos sejam inseridos.
    # Use Arrays/List para armazenar os dados de desenho.

#Entradas
aposta = []
sorteio = []

#Processamento
def obterAposta(apost):
    apost = []
    for i in range(1,7):
        apost.append(int(input(f"Qual o {i}º número, da sua aposta? ")))
    return apost


#Saídas
resposta = obterAposta(aposta)
print(resposta)
print(aposta)



