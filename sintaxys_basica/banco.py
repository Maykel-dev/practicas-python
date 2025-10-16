"""
# --- Banco.py ---
# Login fijo: usuario y contraseña
usuario_correcto = "maykel"
contrasena_correcta = "1234"

# Pedir usuario y contraseña al inicio
usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Verificar si el login es correcto
if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Exito\n")  # Mensaje de login exitoso

    saldo = 0  # Inicializamos el saldo en 0

    # Menú principal, se repite hasta que el usuario elija salir
    while True:
        print("\n MENU BANCO ")
        print("1. Ingresar dinero")
        print("2. Sacar dinero")
        print("3. Ver saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")  # Leer opción del usuario

        # Opción 1: Ingresar dinero
        if opcion == "1":
            ingreso = float(input("Ingrese a cantidad que desea depositar : "))
            saldo += ingreso  # Sumar el dinero ingresado al saldo
            print(f"Se han ingresado ${ingreso:.2f}. Su Saldo Actual es: ${saldo:.2f}")
        
        # Opción 2: Retirar dinero
        elif opcion == "2":
            retiro = float(input("Ingrese la cantidad que desea retirar : "))
            if retiro > saldo:
                print("No tienes saldo suficiente.")  # Verificar si hay suficiente dinero
            else:
                saldo -= retiro  # Restar dinero del saldo
                print(f"Se han retirado ${retiro:.2f}. Saldo actual: ${saldo:.2f}")
        
        # Opción 3: Ver saldo
        elif opcion == "3":
            print(f"Su saldo actual es: ${saldo:.2f}")
        
        # Opción 4: Salir del programa
        elif opcion == "4":
            print("Gracias por usar el banco de Michi Feliz XD XD XD XD ")
            break  # Rompe el bucle y termina el programa
        
        # Opción no válida
        else:
            print("Opcion no valida . Por favor Intente nuevamente.")

# Si el login es incorrecto
else:
    print("Usuario o contraseña incorrectos. Acceso denegado.")
"""
"""
# Clase Cliente
class Cliente:
    def __init__(self, nombre, saldo_inicial=1000):
        self.nombre = nombre
        self.saldo = saldo_inicial
        print(f"Cliente {self.nombre} registrado con saldo inicial de ${self.saldo:.2f}.")

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han ingresado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No tienes saldo suficiente.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.nombre}: ${self.saldo:.2f}")
"""









class Cliente:
    def __init__(self, usuario, contrasena, saldo_inicial=1000):
        self.usuario = usuario
        self.contrasena = contrasena
        self.saldo = saldo_inicial
        print(f"Cliente '{self.usuario}' registrado con saldo inicial de ${self.saldo:.2f}.")

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han ingresado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No tienes saldo suficiente.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}")

    def mostrar_saldo(self):
        print(f"Saldo actual de '{self.usuario}': ${self.saldo:.2f}")


usuario = input("Crea tu usuario: ")
contrasena = input("Crea tu contraseña: ")


cliente = Cliente(usuario, contrasena)


print("\nAhora inicia sesión")
usuario_login = input("Usuario: ")
contrasena_login = input("Contraseña: ")

if usuario_login == cliente.usuario and contrasena_login == cliente.contrasena:
    print("¡Login exitoso!\n")

    while True:
        print("\n--- MENÚ BANCO ---")
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Ver saldo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)

        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)

        elif opcion == "3":
            cliente.mostrar_saldo()

        elif opcion == "4":
            print("Gracias por usar el banco. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor intente nuevamente.")

else:
    print("Usuario o contraseña incorrectos. Acceso denegado.")
