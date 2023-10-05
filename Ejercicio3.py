t = int(input())

for _ in range(t):
    n = int(input())
    horarios = [tuple(map(int, input().split())) for _ in range(n)]
    horarios.sort(key=lambda x: x[1])
    
    # Inicializar el número de películas que puedes ver como máximo
    peliculas_vistas = 0
    
    # Inicializar el tiempo actual como el inicio de la primera película
    tiempo_actual = horarios[0][0]
    
    # Iterar a través de los horarios de las películas
    for i in range(n):
        inicio, fin = horarios[i]
        if inicio >= tiempo_actual:
            # Si el inicio de la película es igual o después del tiempo actual,
            # puedes verla, así que la sumamos a las películas vistas y actualizamos el tiempo actual.
            peliculas_vistas += 1
            tiempo_actual = fin
    
    # Imprimir el número máximo de películas que puedes ver
    print(peliculas_vistas)
