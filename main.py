import stats_data as sd

lista = []
while True:
    numbers = input("Introduce cualquier numero: ")
    if numbers == "fin":
        break
    numbers = float(numbers)
    lista.append(numbers)
calculo_stats = sd.StatsData(lista)

print("Lista de numbers: ", calculo_stats.l_data)
print("Media: ", calculo_stats.mean)
print("Mediana: ", calculo_stats.median)
print("Varianza: ", calculo_stats.variance)