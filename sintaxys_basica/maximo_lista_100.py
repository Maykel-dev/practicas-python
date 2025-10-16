import random

def maximo_lista():
  
    lista = [random.randint(1, 20) for _ in range(10)]
    print("Lista generada:", lista)

    
    maximo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
            print(f"Nuevo máximo encontrado: {maximo}")  

    print("El número máximo de la lista es:", maximo)
