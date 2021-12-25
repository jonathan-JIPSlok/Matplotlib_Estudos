from matplotlib import pyplot as plt

#Anos
years = [1995, 2000, 2005, 2010, 2015, 2020]

#Total de Usuarios por anos
Users_Tot = [10567489.50, 30789426.89, 50721567.40, 25578514.56, 30524618.45, 90547156.58]

#Cria um grafuco de linhas com years no eixo x (>) e Users_Tot no eixo y (^), a cor das linhas red, marcador de linha como (•), e estilo de linha solida..
plt.plot(years, Users_Tot, color = "red", marker = "o", linestyle = "solid")

#Adiciona um titulo ao grafico
plt.title("Google Users in years")

#Adiciona um selo no lado y(^)
plt.ylabel("Total de Usuarios")

#renderiza o grafico
plt.show()