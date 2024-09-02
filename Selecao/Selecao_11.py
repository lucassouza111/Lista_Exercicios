# 11) Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:
    # ACESSO PERMITIDO caso a senha seja válida.
    # ACESSO NEGADO caso a senha seja inválida.

#Entradas
senha = int(input("Digite a senha, do sistema: "))
senhaPadrao = 1234

#Processamento
def verificarSenha(senh,padrao):
    if senh == padrao:
        return "ACESSO PERMITIDO"
    return "ACESSO NEGADO"


#Saídas
print(verificarSenha(senha,senhaPadrao))
