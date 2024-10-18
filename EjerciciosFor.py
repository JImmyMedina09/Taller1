import random

while True:
    print("\n--- Menú de Ejercicios Ciclo For ---")
    print("Presentado por: Jimmy Medina")
    print("1. Sumar los cubos de los números del 1 al 50")
    print("2. Crear una pirámide de asteriscos")
    print("3. Simular un tablero de ajedrez")
    print("4. Invertir una cadena ingresada por el usuario")
    print("5. Buscar un elemento en una lista de caracteres")
    print("6. Salir")
   
    
    opcion = input("Elige una opción (1,2,3,4,5,6): ")

    if opcion == '1':
        suma_cubos = 0
        for numero in range(1, 51):
            suma_cubos += numero ** 3
        print(f"La suma de los cubos de los números del 1 al 50 es: {suma_cubos}")

    elif opcion == '2':
        niveles = 5
        print("Pirámide de asteriscos:")
        for i in range(1, niveles + 1):
            print('*' * i)

    elif opcion == '3':
        tamano = 8
        print("Tablero de ajedrez:")
        for fila in range(tamano):
            if fila % 2 == 0:
                print("* " * (tamano // 2))
            else:
                print(" *" * (tamano // 2))

    elif opcion == '4':
        cadena = input("Por favor, ingrese una cadena: ")
        cadena_invertida = ""
        for letra in cadena:
            cadena_invertida = letra + cadena_invertida
        print(f"La cadena invertida es: {cadena_invertida}")

    elif opcion == '5':
        lista = ["carro", "moto", "bicicleta", "patineta", "camion"]
        elemento = input("Ingrese el elemento que desea buscar: ")
        encontrado = False
        for item in lista:
            if item == elemento:
                encontrado = True
                break
        if encontrado:
            print(f"El elemento '{elemento}' se encuentra en la lista.")
        else:
            print(f"El elemento '{elemento}' no se encuentra en la lista.")

    elif opcion == '6':
        print("Saliendo del programa. ¡See You Later!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción entre 1,2,3,4,5,6.")