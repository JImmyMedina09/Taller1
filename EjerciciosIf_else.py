while True:
    print("\n--- Menú de Ejercicios ---")
    print("Presentado por: Jimmy Medina")
    print("1. Determinar si una letra está en las primeras o últimas del alfabeto")
    print("2. Determinar el cuadrante de un ángulo")
    print("3. Clasificar el rendimiento de un estudiante")
    print("4. Clasificar la temperatura")
    print("5. Verificar la palabra 'Jengibre'")
    print("6. Salir")
    
    
    opcion = input("Elige una opción (1-6): ")

    if opcion == '1':
        letra = input("ingresa una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("solo debes ingresar una sola letra.")
        elif 'a' <= letra <= 'm':
            print(f"La letra '{letra}' está en la primera parte del alfabeto (a - m).")
        else:
            print(f"La letra '{letra}' está en la última parte del alfabeto (n - z).")

    elif opcion == '2':
        angulo = float(input("ingresa el valor del ángulo en grados: "))
        
        if 0 < angulo < 90:
            print(f"El ángulo de {angulo} grados se encuentra en el primer cuadrante.")
        elif 90 < angulo < 180:
            print(f"El ángulo de {angulo} grados se encuentra en el segundo cuadrante.")
        elif 180 < angulo < 270:
            print(f"El ángulo de {angulo} grados se encuentra en el tercer cuadrante.")
        elif 270 < angulo < 360:
            print(f"El ángulo de {angulo} grados se encuentra en el cuarto cuadrante.")
        elif angulo == 0 or angulo == 360:
            print(f"El ángulo de {angulo} grados está en el eje positivo de X.")
        elif angulo == 90:
            print(f"El ángulo de {angulo} grados está en el eje positivo de Y.")
        elif angulo == 180:
            print(f"El ángulo de {angulo} grados está en el eje negativo de X.")
        elif angulo == 270:
            print(f"El ángulo de {angulo} grados está en el eje negativo de Y.")
        else:
            print("El ángulo ingresado no está dentro del rango de 0 a 360 grados.")

    elif opcion == '3':
        calificacion = float(input("Ingrese la calificación del estudiante (0 a 5): "))
        
        if calificacion > 4.5:
            print("Rendimiento: Excelente")
        elif 3.5 < calificacion <= 4.5:
            print("Rendimiento: Bueno")
        elif 3 <= calificacion <= 3.5:
            print("Rendimiento: Regular")
        elif 0 <= calificacion < 3:
            print("Rendimiento: Insuficiente")
        else:
            print("La calificación ingresada no es válida. Debe estar entre 0 y 5.")

    elif opcion == '4':
        temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
        
        if temperatura < 15:
            print("Clasificación: Frío")
        elif 15 <= temperatura <= 25:
            print("Clasificación: Templado")
        else:
            print("Clasificación: Cálido")

    elif opcion == '5':
        palabra = input("Por favor, ingrese la palabra 'Jengibre': ")
        
        if palabra == "Jengibre":
            print("Sí, ¡El Jengibre es la mejor planta de todos los tiempos!")
        elif palabra == "jengibre":
            print("No, ¡quiero un gran Jengibre!")
        else:
            print(f"¡Jengibre! No, la palabra ingresada fue '{palabra}'")

    elif opcion == '6':
        print("Saliendo del programa. ¡See You Later!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 6.")
