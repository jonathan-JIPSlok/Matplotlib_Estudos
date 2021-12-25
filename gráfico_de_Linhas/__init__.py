from matplotlib import pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#Podemos fazer multiplas chamadas usando plt.plot() para mostrar multiplas series no mesmo grafico

#linha verde solida
plt.plot(xs, variance, 'g-', label = "variance")

#linha com linha de ponto tracejada vermelha
plt.plot(xs, bias_squared, "r-", label = "bias^2")

#linha com ponto azul
plt.plot(xs, total_error, 'b:', label = "total_error")

#Porque atribuimos rótulos para cada serie podemos obter uma legenda gratuita
#loc = 9 significa "top center"
plt.legend(loc = 9)

plt.xlabel("Complexibilidade do modelo")

plt.title("Compromisso entre polarização e variancia")

plt.show()