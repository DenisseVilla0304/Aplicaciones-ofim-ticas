print("******Calculadora******")
print("*Selecciona una opción*")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la opción: ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

resp1 = num1 + num2
resp2 = num1 - num2
resp3 = num1 * num2

if opcion == "1":
    print("Resultado:", resp1)

elif opcion == "2":
    print("Resultado:", resp2)

elif opcion == "3":
    print("Resultado:", resp3)

elif opcion == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: No se puede dividir para cero.")

else:
    print("Opción no válida")
