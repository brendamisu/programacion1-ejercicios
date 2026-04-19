
# 1. Calcula el área de un rectángulo con base 5 y altura 3. Imprime el resultado.
base = 5
altura = 3
area_rectangulo = base*altura
print("El área del rectángulo es:", area_rectangulo)

# 2. Convierte la temperatura de Celsius a Fahrenheit. Pide al usuario ingresar la temperatura en Celsius y luego imprime la temperatura equivalente en Fahrenheit.
Celsius = float(input("Ingrese la temperatura en Celsius: "))
Fahrenheit = (Celsius*1.8) + 32
print("La temperatura en Fahrenheit es:", Fahrenheit)

# 3. Concatena tu nombre y tu edad como strings y guárdalos en una variable. Luego imprime el tipo de dato de esa variable.
nombre_edad = "Brenda" + "20"
print(type(nombre_edad))
# El tipo de dato de la variable es un string.

# 4. Calcula el área de un círculo con radio 4. Imprime el resultado.
radio = 4
area_circulo = 3.14*(radio**2)
print("El área del círculo es:", area_circulo)

# 5. Pide al usuario que ingrese dos números y muestra la suma, resta, multiplicación y división de esos números.
num_1 = int(input("Ingrese un número: "))
num_2 = int(input("Ingrese otro número: "))
print("La suma da:", num_1+num_2, "\nLa resta da:", num_1-num_2, "\nLa multiplicación da:", num_1*num_2, "\nLa división da:", num_1/num_2)

# 6. Almacena el resultado de una operación aritmética compleja en una variable y luego imprime tanto el resultado como el tipo de dato de esa variable.
resultado = 200 + 10**2 - 50 * 3 + 600 / 4
print("Resultado de la operación:", resultado, "\nTipo de dato:", type(resultado))
# El tipo de dato de la variable es un float.

# 7. Crea una variable booleana que represente si un alumno ha aprobado o no un examen y luego imprime su estado.
aprobado = True
print(aprobado)

# 8. Calcula el perímetro de un triángulo equilátero con lados de longitud 6. Imprime el resultado.
longitud_lados = 6
perimetro_triangulo = longitud_lados*3
print("El perímetro del triángulo es:", perimetro_triangulo)

# 9. Pide al usuario que ingrese su nombre, edad y ciudad de residencia y luego imprime cada uno de esos datos con su respectivo tipo de dato.
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad de residencia: ")
print(nombre, type(nombre))
print(edad, type(edad))
print(ciudad, type(ciudad))
# En este caso, todos los datos son strings porque la función input siempre devuelve un string.

# 10. Realiza una operación matemática que involucre paréntesis, multiplicación, suma y resta. Guarda el resultado en una variable y luego imprímela junto con su tipo de dato.
operacion = 450 - (20*5) + 25
print("Resultado de la operación con paréntesis:", operacion, "\nTipo de dato:", type(operacion))
# A diferencia del ejercicio 6, el tipo de dato es un int en vez de un float.
