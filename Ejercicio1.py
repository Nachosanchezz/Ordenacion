# Leer el número de casos de prueba
t = int(input())

for _ in range(t):
    # Leer el número de alumnos y los identificadores
    n = int(input())
    identificadores = list(map(int, input().split()))

    # Algoritmo de ordenamiento de burbuja (ya proporcionado)

    # Contador de identificadores únicos
    unique_count = 0

    # Recorrer la lista de identificadores y contar los únicos
    for i in range(n):
        is_unique = True
        for j in range(i + 1, n):
            if identificadores[i] == identificadores[j]:
                is_unique = False
                break
        if is_unique:
            unique_count += 1

    # Imprimir el número de identificadores únicos
    print(unique_count)
