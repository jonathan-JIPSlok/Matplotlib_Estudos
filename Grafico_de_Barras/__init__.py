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

#nomeia o eixo x (>) com o nome dos filmes, 1 param: lista com os numeros de cada filme que tera, 2 param: lista com os nomes dos filmes
plt.xticks([num for num, _ in enumerate(movies)], movies)

#recebe uma lista com valores númericos, os 2 primeiros valores é o eixo x os 2 segundos é o eixo y
#plt.axis([eixo x menor, eixo x maior, eixo y menor, eixo y maior])
#Seja criterioso quando usar plt.axis(). Ao criar Graficos de barra, não começar o eixo y em 0 é considerado ruim, já que essa é uma maneira fácil de enganar as pessoas.

#renderiza o grafico
plt.show()