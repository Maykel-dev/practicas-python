import random  

def mostrar_diccionario():
    mydictionary = dict()
    mydictionary['human'] = 2
    mydictionary['mouse'] = 4
    mydictionary['spider'] = 8

    for animal in mydictionary:
        data = mydictionary[animal]
        print(f'The {animal} has {data} legs')


def contar_con_while():
    counter = 0
    while counter < 10:
        print(counter)
        counter += 1


def pares_con_for():
    mylist = []
    for i in range(100):
        if i % 2 == 0:
            mylist.append(i)
    print(mylist)


def pares_comprension():
    mylist = [i for i in range(10) if i % 2 == 0]
    print(mylist)


def lista_doble():
    mylist = [i + i for i in range(100)]
    print(mylist)


def greetings():
    return f'Hello my friend...'



def numeros_maximos():
   
    lista = [i**2 if i <= 3 else i for i in range(1, 101)]
    print("Lista generada (primeros 20 elementos):", lista[:20], "...")

   
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
            print(f"Nuevo máximo encontrado: {maximo}")

    print("El número máximo de la lista es:", maximo)


while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Mostrar diccionario")
    print("2. Contar con while (0 al 9)")
    print("3. Números pares (0-99) con for")
    print("4. Números pares (0-9) con comprensión")
    print("5. Lista con el doble de cada número (0-198)")
    print("6. Saludo con función")
    print("7. Lista 1-100 (3 primeros al cuadrado) y máximo")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_diccionario()
    elif opcion == "2":
        contar_con_while()
    elif opcion == "3":
        pares_con_for()
    elif opcion == "4":
        pares_comprension()
    elif opcion == "5":
        lista_doble()
    elif opcion == "6":
        print(greetings())
    elif opcion == "7":
        numeros_maximos()
    elif opcion == "0":
        print("Saliendo... ")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
