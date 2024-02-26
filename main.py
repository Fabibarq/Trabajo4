# Función para saludar al usuario con su nombre
def saludar():
    nombre = input("Por favor, ingresa tu nombre: ")
    print("¡Hola,", nombre + "! Bienvenido al programa.")

# Función para contar hasta un número específico
def contar():
    numero = int(input("Ingresa un número entero para contar hasta él: "))
    print("Contando hasta", numero, ":")
    for i in range(1, numero + 1):
        print(i)

# Función para realizar operaciones aritméticas simples
def calcular():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación a realizar (suma, resta, multiplicación o división): ")

    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicación':
        resultado = num1 * num2
    elif operacion == 'división':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: No se puede dividir entre cero."
    else:
        resultado = "Operación no válida"

    print("El resultado de la", operacion, "es:", resultado)

# Función principal que ejecuta el programa
def main():
    print("Bienvenido al programa")
    print("1. Saludo Personalizado")
    print("2. Contador de Números")
    print("3. Calculadora Básica")
    opcion = int(input("Por favor, selecciona una opción (1, 2 o 3): "))

    if opcion == 1:
        saludar()
    elif opcion == 2:
        contar()
    elif opcion == 3:
        calcular()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
