def suma_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")

    resultado = []  # Este debe estar dentro de la función
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)  # Esta línea estaba mal indentada
        resultado.append(fila)  # También debe estar dentro del bucle principal
    return resultado  # Este debe estar al nivel de la función, no dentro del for

# Ejemplo de uso
matriz_a = [
    [1, 2],
    [3, 4]
]

matriz_b = [
    [5, 6],
    [7, 8]
]

resultado_suma = suma_matrices(matriz_a, matriz_b)
print("Matriz resultante de la suma:")
for fila in resultado_suma:
    print(fila)
    


