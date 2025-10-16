import numpy as np  

print('=================================================================================')
print("CREACIÓN DE MATRICES ALEATORIAS")
print('=================================================================================')

# Generar matrices aleatorias 3x3
m1 = np.random.randint(1, 10, (3, 3))
m2 = np.random.randint(1, 10, (3, 3))

print("Matriz 1:\n", m1)
print("\nMatriz 2:\n", m2)
print("-------------------------------------------------------------")

# -------------------------------------------------------------
# Operaciones básicas entre matrices
# -------------------------------------------------------------
suma = m1 + m2
resta = m1 - m2
multiplicacion = m1 * m2
division = m1 / m2 
producto_matricial = np.dot(m1, m2)  

print("Suma de matrices:\n", suma)
print("\nResta de matrices:\n", resta)
print("\nMultiplicación elemento a elemento:\n", multiplicacion)
print("\nDivisión elemento a elemento:\n", np.round(division, 2))
print("\nProducto matricial (dot product):\n", producto_matricial)
print("-------------------------------------------------------------")

# -------------------------------------------------------------
# Sumas por filas, columnas y total
# -------------------------------------------------------------
suma_filas = np.sum(m1, axis=1)
suma_columnas = np.sum(m1, axis=0)
suma_total = np.sum(m1)

print("Suma por filas de la Matriz 1:", suma_filas)
print("Suma por columnas de la Matriz 1:", suma_columnas)
print("Suma total de todos los elementos de la Matriz 1:", suma_total)
print("-------------------------------------------------------------")

# -------------------------------------------------------------
# Máscara booleana y filtrado
# -------------------------------------------------------------
filtro = m1 > 5
print("Máscara booleana (m1 > 5):\n", filtro)
print("Valores filtrados mayores a 5 en m1:", m1[filtro])
print("-------------------------------------------------------------")

# -------------------------------------------------------------
# Manipulación de filas y columnas (tipo “píxeles”)
# -------------------------------------------------------------
print("Matriz original para manipulación de filas y columnas:\n", m1)

# Intercambiar fila 0 con fila 2
m1[[0, 2]] = m1[[2, 0]]
print("\nDespués de intercambiar fila 0 con fila 2:\n", m1)

# Intercambiar columna 0 con columna 2
m1[:, [0, 2]] = m1[:, [2, 0]]
print("\nDespués de intercambiar columna 0 con columna 2:\n", m1)

# Transponer la matriz
m_transpuesta = m1.T
print("\nMatriz transpuesta (filas ↔ columnas):\n", m_transpuesta)

# Mezclar filas aleatoriamente
np.random.shuffle(m1)
print("\nMatriz después de mezclar filas aleatoriamente:\n", m1)

# Mezclar columnas aleatoriamente
m1 = m1[:, np.random.permutation(m1.shape[1])]
print("\nMatriz después de mezclar columnas aleatoriamente:\n", m1)

# -------------------------------------------------------------
# Concatenación de matrices (horizontal y vertical)
# -------------------------------------------------------------
print('\n=================================================================================')
print("CONCATENACIÓN DE MATRICES")
print('=================================================================================')

# Crear dos matrices aleatorias 3x3 (simulando imágenes)
img1 = np.random.randint(0, 256, (3, 3))
img2 = np.random.randint(0, 256, (3, 3))

print("Matriz img1:\n", img1)
print("\nMatriz img2:\n", img2)

# Concatenación horizontal
conc_horizontal = np.hstack((img1, img2))
print("\nConcatenación horizontal (lado a lado):\n", conc_horizontal)

# Concatenación vertical
conc_vertical = np.vstack((img1, img2))
print("\nConcatenación vertical (una debajo de otra):\n", conc_vertical)

# Usando np.concatenate con axis
conc_h_axis = np.concatenate((img1, img2), axis=1)
conc_v_axis = np.concatenate((img1, img2), axis=0)

print("\nConcatenación horizontal usando np.concatenate:\n", conc_h_axis)
print("\nConcatenación vertical usando np.concatenate:\n", conc_v_axis)

print('=================================================================================')
print("FIN DEL PROGRAMA")
print('=================================================================================')
