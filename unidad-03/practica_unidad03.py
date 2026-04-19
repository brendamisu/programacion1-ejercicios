
# 1. Solicita al usuario que ingrese su nombre y su edad. Luego, imprime un mensaje que diga "¡Hola, [nombre]! Tienes [edad] años".

nombre_usuario = input("Ingrese su nombre: ")
edad_usuario = input("Ingrese su edad: ")
print(f"¡Hola, {nombre_usuario}! Tienes {edad_usuario} años")


"""
2. Imprima en pantalla las siguientes figuras geometricas (utilizar concatenación y replicación de strings)

+***************+
*               *
*               *
*               *
+***************+

+---+
|   |
|   |
|   |
+---+

###################################
###################################
##                               ##
##                               ##
##                               ##
###################################
###################################

"""

# Primera figura
linea1 = "+" + ("*" * 15) + "+\n"
linea2 = "*" + (" " * 15) + "*\n"
print(linea1 + linea2*3 + linea1)

# Segunda figura
linea3 = "+" + ("-" * 3) + "+\n"
linea4 = "|" + (" " * 3) + "|\n"
print(linea3 + linea4*3 + linea3)

# Tercera figura
linea5 = ("#" * 35) + "\n"
linea6 = ("#" * 2) + (" " * 31) + ("#" * 2) + "\n"
print(linea5*2 + linea6*3 + linea5*2)


# 3. Solicita al usuario que ingrese dos números enteros. Luego, convierte estos números a float, realiza la división de ambos y muestra el resultado.

numero_1 = input("Ingrese un número entero: ")
numero_2 = input("Ingrese otro número entero: ")
division = float(numero_1) / float(numero_2)
print(f"La división de ambos números es igual a: {division}")


# 4. Pide al usuario que ingrese una cadena que represente un número entero. Convierte esta cadena a un entero usando la función int() y luego suma 10. Imprime el resultado.

cadena = input("Ingrese un número entero: ")
resultado = int(cadena) + 10
print(resultado)


# 5. Pregunta al usuario que ingrese un número. Si el número es mayor que 10, imprime "El número es mayor que 10". Si es igual a 10, imprime "El número es igual a 10". De lo contrario, imprime "El número es menor que 10".

numero = int(input("Ingrese un número: "))

if numero > 10:
    print("El número es mayor que 10")
elif numero == 10:
    print("El número es igual a 10")
else:
    print("El número es menor que 10")


# 6. Solicita al usuario que ingrese dos números y compara si son iguales. Si lo son, imprime "Los números son iguales". De lo contrario, imprime "Los números son diferentes".

primer_num = int(input("Ingrese un número: "))
segundo_num = int(input("Ingrese otro número: "))

if primer_num == segundo_num:
    print("Los números son iguales")
else:
    print("Los números son diferentes")


# 7. Pregunta al usuario que ingrese su edad. Si la edad es mayor o igual a 18, imprime "Eres mayor de edad". De lo contrario, imprime "Eres menor de edad".

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# 8. Pide al usuario que ingrese una temperatura en Celsius. Si la temperatura es mayor o igual a 100, imprime "El agua está hirviendo". Si es menor o igual a 0, imprime "El agua está congelada". De lo contrario, imprime "El agua está en estado líquido".

temperatura = float(input("Ingrese una temperatura en Celsius: "))

if temperatura >= 100:
    print("El agua está hirviendo")
elif temperatura <= 0:
    print("El agua está congelada")
else:
    print("El agua está en estado líquido")


# 9. Pregunta al usuario que ingrese un número. Si es positivo, imprime "El número es positivo". Si es negativo, imprime "El número es negativo". Si es cero, imprime "El número es cero".

num = int(input("Ingrese un número: "))

if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")


# 10. Solicita al usuario que ingrese un número del 1 al 7. Luego, imprime el día de la semana correspondiente (1 para Lunes, 2 para Martes, etc.). Si ingresa un número fuera de ese rango, imprime "Número de día no válido".

numero_dia = int(input("Ingrese un número del 1 al 7: "))

if numero_dia == 1:
    print("Lunes")
elif numero_dia == 2:
    print("Martes")
elif numero_dia == 3:
    print("Miércoles")
elif numero_dia == 4:
    print("Jueves")
elif numero_dia == 5:
    print("Viernes")
elif numero_dia == 6:
    print("Sábado")
elif numero_dia == 7:
    print("Domingo")
else:
    print("Número de día no válido")


# 11. Calculadora básica
# Crea un programa que tome dos números como entrada y luego imprima la suma, resta, multiplicación y división de esos dos números. Usa operadores aritméticos y asegúrate de manejar casos donde el divisor sea cero.

num_1 = float(input("Ingrese el primer número: "))
num_2 = float(input("Ingrese el segundo número: "))

suma = num_1 + num_2
print(f"El resultado de la suma es {suma}")

resta = num_1 - num_2
print(f"El resultado de la resta es {resta}")

multiplicacion = num_1 * num_2
print(f"El resultado de la multiplicación es {multiplicacion}")

if num_2 == 0:
    print("El resultado de la división es indefinido")
else:
    division = num_1 / num_2
    print(f"El resultado de la división es {division}")


# 12. Calculador de IMC
# Crea un programa que calcule el Índice de Masa Corporal (IMC) de una persona. Pide al usuario su peso en kilogramos y su altura en metros. Luego, calcula el IMC usando la fórmula `IMC = peso / altura**2` y muestra el resultado con un mensaje que indique si el IMC está en el rango normal, bajo peso, sobrepeso, etc.

peso_kg = float(input("Ingrese su peso en kilogramos: "))
altura_m = float(input("Ingrese su altura en metros: "))
imc = peso_kg / altura_m**2

if imc < 18.5:
    res = "bajo peso"
elif imc < 25:
    res = "peso normal"
elif imc < 30:
    res = "sobrepeso"
elif imc < 35:
    res = "obesidad grado I"
elif imc < 40:
    res = "obesidad grado II"
else:
    res = "obesidad grado III"

print(f"Su IMC es {imc}. Resultado: {res}")


# 13. Conversión de unidades
# Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit. La fórmula de conversión es `F = C * 9/5 + 32`. Pide al usuario que ingrese una temperatura en Celsius y muestra el resultado en Fahrenheit.

Celsius = float(input("Ingrese una temperatura en Celsius: "))
Fahrenheit = Celsius * 9/5 + 32
print(f"La temperatura en Fahrenheit es: {Fahrenheit}")


# 14. Juego de adivinanza
# Crea un programa que pida al usuario que adivine un número entre 1 y 10. El programa debe comparar el número ingresado con uno predefinido (por ejemplo, 7) y decir si es correcto o no. Si es incorrecto, debe dar una pista si el número es mayor o menor.

numero_predefinido = 8
numero_usuario = int(input("Adivina un número entre 1 y 10: "))

if numero_usuario == numero_predefinido:
    print("¡Felicidades! El número es correcto.")
else:
    print("El número es incorrecto.")
    if numero_predefinido > numero_usuario:
        print("Pista: el número correcto es mayor.")
    else:
        print("Pista: el número correcto es menor.")


"""
15. Identificación del tipo de dato
Escribe un programa que tome una entrada del usuario usando input() y determine qué tipo de dato representa la cadena ingresada. 
Ten en cuenta que input() siempre devuelve una cadena de texto (string), pero el usuario puede haber ingresado algo que representa un número.

Tu programa debe analizar la entrada y determinar si representa:

    Un número entero (positivo o negativo)
    Un número flotante (positivo o negativo)
    Una cadena de texto

Requisitos específicos:

    Usa el método isdigit() para verificar si todos los caracteres son dígitos
    Para números negativos, verifica si el primer carácter es un guión (-) usando indexación
    Para números flotantes, verifica si contiene exactamente un punto decimal
    Imprime un mensaje claro indicando qué tipo de dato representa la entrada

Ejemplo de salidas esperadas:

Entrada: "123" → "El dato representa un número entero"
Entrada: "-45" → "El dato representa un número entero negativo"
Entrada: "3.14" → "El dato representa un número flotante"
Entrada: "-2.5" → "El dato representa un número flotante negativo"
Entrada: "hola" → "El dato representa una cadena de texto"

"""

entrada = input("Ingrese un dato: ")
if entrada.isdigit():
    print("El dato representa un número entero")
else:
    print("El dato no representa un número entero")


# 16. Calculador de calificaciones
# Crea un programa que pida al usuario que ingrese sus calificaciones en tres materias. Luego, calcula el promedio de esas calificaciones e imprime un mensaje que indique si el alumno aprobó (promedio ≥ 6) o no.

calificacion_matematica = float(input("Ingrese su calificación en Matemática: "))
calificacion_arte = float(input("Ingrese su calificación en Arte: "))
calificacion_historia = float(input("Ingrese su calificación en Historia: "))
promedio_calificaciones = (calificacion_matematica + calificacion_arte + calificacion_historia) / 3

if promedio_calificaciones >= 6:
    print("El alumno aprobó")
else:
    print("El alumno desaprobó")


# 17. Concatenación de strings
# Escribe un programa que pida al usuario su nombre y su color favorito. Luego, concatena estos datos en una sola oración que diga "Hola [nombre], tu color favorito es [color]" y la imprima.

nombre = input("Ingrese su nombre: ")
color_favorito = input("Ingrese su color favorito: ")
print("Hola " + nombre + ", tu color favorito es " + color_favorito)
