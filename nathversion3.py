print("******Calculadora******")
print("*Selecciona una operación *")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la opción: ").strip()

if opcion in ("1", "2", "3", "4"):
    try:
        num1 = float(input("Ingresa el primer número: ").strip())
        num2 = float(input("Ingresa el segundo número: ").strip())

        if opcion == "1":
            resultado = num1 + num2
            print("Resultado de la suma:", resultado)

        elif opcion == "2":
            resultado = num1 - num2
            print("Resultado de la resta:", resultado)

        elif opcion == "3":
            resultado = num1 * num2
            print("Resultado de la multiplicación:", resultado)

        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2

                if "." in str(resultado) and len(str(resultado).split(".")[1]) > 6:
                    resultado = round(resultado, 6)

                print("Resultado de la división:", resultado)
            else:
                print("Error: No se puede dividir para cero.")

    except ValueError:
        print("Error: Debes ingresar números válidos.")
    except OverflowError:
        print("Error: El número es demasiado grande para procesar.")
else:
    print("Opción no válida")
