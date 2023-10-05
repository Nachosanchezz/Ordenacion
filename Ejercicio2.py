# Leer el peso máximo por góndola y el número de niños
peso_maximo = int(input("Escriba el peso maximo por gondola: "))
n = int(input("Escriba el numero de niños: "))

# Leer los pesos de los niños y ordenarlos de menor a mayor
niños = list(map(int, input("Escribe el peso de los niños: ").split()))
niños.sort()

# Inicializar variables para contar el número de góndolas y para llevar un índice de inicio
num_góndolas = 0
inicio = 0

# Usar dos punteros para encontrar los pares de niños que quepan en una góndola
while inicio < n:
    fin = n - 1
    while inicio < fin:
        if niños[inicio] + niños[fin] <= peso_maximo:
            inicio += 1
        fin -= 1
    num_góndolas += 1

    # Si solo queda un niño sin pareja, colocarlo en su propia góndola
    if inicio == fin:
        num_góndolas += 1

print(num_góndolas)
