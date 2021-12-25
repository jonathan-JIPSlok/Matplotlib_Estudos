from matplotlib import pyplot as plt

"""
Um grafico de Disperção é a escolha certa para visualizar o relacionamento entre dois pares de conjuntos de dados.

EX: O relacionamento entre o número de amigos que seus usuários tem e o número de minutos que eles passam no site por dia
"""

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes) #Desenha o grafico de disperção (x, y)

#Nomeia cada posição
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                        xy = (friend_count, minute_count), #Coloca o rotulo com sua posição
                        xytext = (5, -5), #mas compensa um pouco
                        textcoords = 'offset points')
                        
plt.title("Minutos Diários vs Número de Amigos")

plt.xlabel("# de Amigos")

plt.ylabel("Minutos diarios passados no site")

plt.show()