
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Error: división entre cero"

print("\nResultados:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

nombre = "maykel"
print("\nAutor del programa (mayúsculas):", nombre.upper())
print("Autor del programa (minúsculas):", nombre.lower())


language = "PYTHON"
print("\nCadena completa:", language)
primer_caracter = language[0]
antepenultimo_caracter = language[-3]
numero_caracteres = len(language)
print("Primer carácter:", primer_caracter)
print("Antepenúltimo carácter:", antepenultimo_caracter)
print("Número de caracteres:", numero_caracteres)

dispositivos = ["router", "cable", "mause", "teclado"]
lista_nombres = ["Carlos", "Ana", "Luis", "María"]
numeros = list(range(0, 11))  
tupla_dispositivos = tuple(dispositivos)


animales = {
    "perro": "Fiel",
    "gato": "Independiente",
    "loro": "Hablador"
}


while True:
    entrada_menu = input("\n¿Deseas entrar al menú de edición de listas, tuplas y diccionarios? (s/n): ").lower()
    if entrada_menu != 's':
        print("\nNo se modificará ninguna lista, tupla o diccionario. Continuando con el programa...")
        break

    print("\nElige el contenedor a modificar:")
    print("1 - Lista de dispositivos")
    print("2 - Lista de nombres")
    print("3 - Lista de números (0 al 10)")
    print("4 - Tupla de dispositivos")
    print("5 - Diccionario de animales")
    print("0 - Salir del menú")
    opcion = int(input("Opción: "))

    if opcion == 0:
        print("Saliendo del menú...")
        break

    es_diccionario = False
    es_tupla = False
    lista_seleccionada = None

    if opcion == 1:
        lista_seleccionada = dispositivos
        nombre_lista = "Lista de dispositivos"
    elif opcion == 2:
        lista_seleccionada = lista_nombres
        nombre_lista = "Lista de nombres"
    elif opcion == 3:
        lista_seleccionada = numeros
        nombre_lista = "Lista de números"
    elif opcion == 4:
        lista_seleccionada = list(tupla_dispositivos)
        nombre_lista = "Tupla de dispositivos"
        es_tupla = True
    elif opcion == 5:
        diccionario_seleccionado = animales
        nombre_lista = "Diccionario de animales"
        es_diccionario = True
    else:
        print("Opción inválida")
        continue


    if es_diccionario:
        print(f"\n{nombre_lista} actual:", diccionario_seleccionado)
        print("OK")
        print("Acciones disponibles: agregar (a), reemplazar (r), eliminar (e)")
        accion = input("Elige la acción: ").lower()
        if accion == "a":
            clave = input("Ingrese la nueva clave: ")
            valor = input("Ingrese el valor asociado: ")
            diccionario_seleccionado[clave] = valor
        elif accion == "r":
            clave = input("Ingrese la clave a reemplazar: ")
            if clave in diccionario_seleccionado:
                valor = input("Ingrese el nuevo valor: ")
                diccionario_seleccionado[clave] = valor
            else:
                print("Clave no encontrada")
        elif accion == "e":
            clave = input("Ingrese la clave a eliminar: ")
            if clave in diccionario_seleccionado:
                del diccionario_seleccionado[clave]
            else:
                print("Clave no encontrada")
        else:
            print("Acción inválida")
        print(f"\n{nombre_lista} actualizada:", diccionario_seleccionado)
        print("OK")

  
    elif lista_seleccionada is not None:
        print(f"\n{nombre_lista} actual:", lista_seleccionada)
        print("OK")

        if es_tupla:
            accion = input("¿Deseas reemplazar un elemento (r) o agregar uno nuevo (a)? ").lower()
            if accion == "r":
                indice = int(input("Ingrese el índice del elemento a modificar (empezando en 0): "))
                nuevo_valor = input("Ingrese el nuevo valor: ")
                lista_seleccionada[indice] = nuevo_valor
            elif accion == "a":
                nuevo_valor = input("Ingrese el nuevo valor a agregar: ")
                lista_seleccionada.append(nuevo_valor)
            else:
                print("Acción inválida")
            tupla_dispositivos = tuple(lista_seleccionada)
        else:
            indice = int(input("Ingrese el índice del elemento a modificar (empezando en 0): "))
            nuevo_valor = input("Ingrese el nuevo valor: ")
            if opcion == 3:
                lista_seleccionada[indice] = int(nuevo_valor)
            else:
                lista_seleccionada[indice] = nuevo_valor

        print(f"\n{nombre_lista} actualizada:", lista_seleccionada)
        print("OK")


print("\nÚltimos elementos y últimos tres números de las listas y tupla:")
print("Último elemento de dispositivos:", dispositivos[-1])
print("Último elemento de nombres:", lista_nombres[-1])
print("Últimos tres números de la lista de números:", numeros[-3:])
print("Último elemento de la tupla de dispositivos:", tupla_dispositivos[-1])
print("Diccionario de animales final:", animales)
print("OK")
