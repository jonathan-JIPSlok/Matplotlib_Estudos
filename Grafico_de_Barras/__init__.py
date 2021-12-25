from matplotlib import pyplot as plt

#Filmes
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Est Side Story"]

#Número de Oscars
num_oscars = [5, 11, 3, 8]

#define o grafico com barras eixo x (>) eixo y(^)
plt.bar(movies, num_oscars)

#Titulo do grafico
plt.title("Meus filmes favoritos")

#Selo eixo y
plt.ylabel("Número de Oscars")

#renderiza o grafico
plt.show()