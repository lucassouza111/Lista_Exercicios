# 8) Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

import datetime

#Entradas
ano = int(input("Qual o seu ano de nascimento? "))

#Processamento
def podeVotar(anoNascimento):
    anoAtual = datetime.datetime.now().year
    if anoAtual - anoNascimento > 15:
        return True
    return False

#Saídas
resposta = "Positivo" if podeVotar(ano) else "Negativo"
print(f"Pode votar: {resposta}")
