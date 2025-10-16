
usuario_correcto = "maykel"
contrasena_correcta = "1234"

usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("¡Login exitoso!\n")
    
    
    number = int(input("Enter a number, please: "))
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

    
    lista_1_100 = list(range(1, 101))
    print("\nLista automática del 1 al 100 creada.")
    suma_1_100 = sum(lista_1_100)
    print(f"Suma de la lista del 1 al 100: {suma_1_100}")

   
    print("\nAhora puedes crear tu propia lista de números para sumar (máximo 100).")
    entrada = input("Ingresa los números separados por comas, ej: 10,3,8,25\nTus números: ")

    lista_usuario = [int(x.strip()) for x in entrada.split(",")]

    if len(lista_usuario) > 100:
        print("¡Has ingresado más de 100 números! Solo se tomarán los primeros 100.")
        lista_usuario = lista_usuario[:100]

    suma_usuario = sum(lista_usuario)
    print(f"\nHas ingresado {len(lista_usuario)} números.")
    print(f"La suma de tus números es: {suma_usuario}")

else:
    print("Usuario o contraseña incorrectos. Acceso denegado.")
