print("******Calculadora******")
print("*Selecciona una operación*")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la opción: ")

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    if opcion == "1":
        print("Resultado de la suma:", num1 + num2)

    elif opcion == "2":
        print("Resultado de la resta:", num1 - num2)

    elif opcion == "3":
        print("Resultado de la multiplicación:", num1 * num2)

    elif opcion == "4":
        try:
            print("Resultado de la división:", num1 / num2)
        except ZeroDivisionError:
            print("No se puede dividir entre cero.")

    else:
        print("Opción no válida.")

except ValueError:
    print("Ingresa un dato permitido (solo números).")
