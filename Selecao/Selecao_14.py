# 14) Escreva um programa para ler o número de gols marcados pelo Grêmio e o número de gols marcados pelo Inter em um GRENAL. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

#Entradas
time1 = str(input("Qual o time da Casa? "))
time2 = str(input("Qual o time visitante? "))
golesTime1 = int(input(f"Quantos goles o {time1} converteu? "))
golesTime2 = int(input(f"Quantos goles o {time2} converteu? "))

#Processamento
if golesTime1 > golesTime2:
    vencedor = time1
elif golesTime2 > golesTime1:
    vencedor = time2
else:
   vencedor = "Empate de goles"

#Saídas
print(f"Neste jogo o ganhador foi {vencedor}. Sendo {time1} com {golesTime1} gol (es) e o {time2} com {golesTime2} gol (es).")
