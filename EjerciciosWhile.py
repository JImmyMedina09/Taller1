import random

while True:
    print("\n--- Menú de Ejercicios ---")
    print("Presentado por: Jimmy Medina")
    print("1. Imprimir números del 1 al 20 de manera inversa")
    print("2. Imprimir números de 2 en 2 hasta el 50")
    print("3. Contar el número de vocales en una cadena")
    print("4. Simular tirar un dado hasta obtener un 6")
    print("5. Sumar los dígitos de un número")
    print("6. Salir")
    
    
    opcion = input("Elige una opción (1-6): ")

    if opcion == '1':
        numero = 20
        while numero >= 1:
            print(numero, end=" ")
            numero -= 1

    elif opcion == '2':
        numero = 0
        while numero <= 50:
            print(numero, end=" ")
            numero += 2

    elif opcion == '3':
        cadena = input("Por favor, ingrese una cadena de texto: ")
        vocales = "aeiouAEIOU"
        contador = 0
        indice = 0

        while indice < len(cadena):
            if cadena[indice] in vocales:
                contador += 1
            indice += 1

        print(f"Número de vocales en la cadena: {contador}")

    elif opcion == '4':
        tiradas = 0
        while True:
            tirada = random.randint(1, 6)
            tiradas += 1
            print(f"Tirada {tiradas}: {tirada}")
            if tirada == 6:
                print(f"¡Obtuviste un 6 después de {tiradas} tiradas!")
                break

    elif opcion == '5':
        numero = input("Por favor, ingresa un número: ")
        suma = 0
        indice = 0
        
        while indice < len(numero):
            if numero[indice].isdigit():
                suma += int(numero[indice])
            indice += 1

        print(f"La suma de los dígitos del número es: {suma}")

    elif opcion == '6':
        print("Saliendo del programa. ¡See You Later!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 6.")
