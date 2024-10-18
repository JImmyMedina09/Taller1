while True:
    print("\n--- Menú de Ejercicios Funciones Lambda ---")
    print("Presentado por: Jimmy Medina")
    print("1. Sumar dos números usando una función lambda")
    print("2. Verificar si un número es par usando una función lambda")
    print("3. Ordenar una lista de tuplas según el segundo elemento")
    print("4. Filtrar números mayores a 10 de una lista usando lambda y filter")
    print("5. Elevar cada número al cuadrado usando lambda y map")
    print("6. Salir")
    
    
    opcion = input("Elige una opción (1-6): ")

    if opcion == '1':
        sumar = lambda x, y: x + y
        x = float(input("Ingresa el primer número: "))
        y = float(input("Ingresa el segundo número: "))
        print(f"La suma de {x} y {y} es: {sumar(x, y)}")

    elif opcion == '2':
        es_par = lambda num: num % 2 == 0
        numero = int(input("Ingresa un número para verificar si es par: "))
        if es_par(numero):
            print(f"El número {numero} es par.")
        else:
            print(f"El número {numero} no es par.")

    elif opcion == '3':
        lista_tuplas = [(1, 3), (4, 2), (2, 5), (3, 1)]
        print(f"Lista original: {lista_tuplas}")
        lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])
        print(f"Lista ordenada por el segundo elemento de cada tupla: {lista_ordenada}")

    elif opcion == '4':
        lista_numeros = [5, 15, 3, 10, 25, 8, 13]
        print(f"Lista original: {lista_numeros}")
        mayores_a_10 = list(filter(lambda x: x > 10, lista_numeros))
        print(f"Números mayores a 10: {mayores_a_10}")

    elif opcion == '5':
        lista_numeros = [2, 3, 4, 5, 6]
        print(f"Lista original: {lista_numeros}")
        cuadrados = list(map(lambda x: x ** 2, lista_numeros))
        print(f"Lista con los números elevados al cuadrado: {cuadrados}")

    elif opcion == '6':
        print("Saliendo del programa. ¡See You Later!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 6.")
