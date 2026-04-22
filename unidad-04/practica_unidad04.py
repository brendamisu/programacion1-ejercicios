"""
EJERCICIO 1:

Crear una variable con valor 20 que va a ser como referencia el mínimo.
Crear otra variable con valor 500 que va a ser como referencia el máximo.
Luego preguntar al usuario por un valor, almacenarlo en una variable y forzar a que ponga un número.
Si no pone un número, preguntar repetidamente.
Transformar ese número en integer.

Ahora imprimir en pantalla:
Si el número que puso el usuario es menor que el valor mínimo definido, mostrar el texto VALOR BAJO.
Si el número que puso el usuario es mayor que el valor máximo definido, mostrar el texto VALOR ALTO.
Si el número que puso el usuario está entre el valor mínimo y el valor máximo, mostrar el texto VALOR MEDIO.

"""

minimo = 20
maximo = 500
valor = input("Ingrese un número: ")

while not valor.isdigit():
    print("El valor ingresado no es un número")
    valor = input("Por favor, ingrese un número: ")

valor = int(valor)
if valor < minimo:
    print("VALOR BAJO")
elif valor > maximo:
    print("VALOR ALTO")
else:
    print("VALOR MEDIO")


"""
EJERCICIO 2:

Escribir un programa que pida un año y diga si es bisiesto o no.
Recordar que los años bisiestos son múltiplos de 4, pero que los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
"""

# En este ejercicio hice dos versiones distintas del mismo programa
year = int(input("Ingrese un año: "))

# Primera versión (con condicionales anidados)
if year % 4 == 0:
    if year % 100 != 0:
        print("El año es bisiesto")
    else:
        if year % 400 == 0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
else:
    print("El año no es bisiesto")

# Segunda versión (con operadores lógicos)
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")


"""
EJERCICIO 3:

Pedir al usuario que ingrese un número de inicio del bucle.
Pedir al usuario que ingrese un número de fin del bucle.
Validar que el número de inicio sea menor al número de fin, si no es así volver a pedir los dos números, hasta que ésto sea correcto
Luego de que el usuario ingrese los dos números, mostrar en pantalla todos los números que hay entre el número de inicio y el número de fin
De la siguiente manera:
Este es el bucle número 1
Este es el bucle número 2
Este es el bucle número 3
---
Fin del programa.

"""

numero_inicio = int(input("Ingrese un número de inicio del bucle: "))
numero_fin = int(input("Ingrese un número de fin del bucle: "))

while not numero_inicio < numero_fin:
    print("El número de inicio debe ser menor al número de fin")
    numero_inicio = int(input("Ingrese un número de inicio del bucle: "))
    numero_fin = int(input("Ingrese un número de fin del bucle: "))

contador = 1
while numero_inicio + 1 < numero_fin:
    print(f"Este es el bucle número {contador}")
    contador += 1
    numero_inicio += 1
print("---" + "\nFin del programa.")


"""
EJERCICIO 4:

Vamos a realizar un programa que nos va a decir la nota promedio de un alumno en todo el cuatrimestre.
Dentro del cuatrimestre son 4 examenes y luego un examen final.
La aprobación del cuatrimestre es con nota 6 o mayor de promedio.
Y si el alumno tiene aprobada la cursada (es decir, obtuvo seis o más de 6 de promedio en sus 4 examenes, rinde el examen final)
Si el alumno tiene aprobada la cursada y el examen final, entonces el alumno aprobó la materia.

Entonces el programa debe preguntar por la nota de cada examen.
En función de las respuestas, primero debe avisar el promedio de las 4 notas de los examenes.
En caso de que el promedio sea mayor o igual a 6, debe avisar que el alumno tiene aprobada la cursada.
En caso de que el promedio sea menor a 6, debe avisar que el alumno no tiene aprobada la cursada.
Luego preguntar por nota del final (en caso de que haya aprobado la cursada), si es mayor o igual a 6, debe avisar que el alumno aprobó la materia.
En caso de que sea menor a 6, debe avisar que el alumno no aprobó el final de la materia, y puede rendir recuperatorio.

"""

nota1 = float(input("Ingrese la nota del primer examen: "))
nota2 = float(input("Ingrese la nota del segundo examen: "))
nota3 = float(input("Ingrese la nota del tercer examen: "))
nota4 = float(input("Ingrese la nota del cuarto examen: "))

promedio_notas = (nota1 + nota2 + nota3 + nota4) / 4
print(f"El promedio de las cuatro notas es {promedio_notas}")

if promedio_notas >= 6:
    print("El alumno aprobó la cursada")
    nota_final = float(input("Ingrese la nota del examen final: "))
    if nota_final >= 6:
        print("El alumno aprobó la materia")
    else:
        print("El alumno no aprobó el examen final y debe rendir un recuperatorio")
else:
    print("El alumno no aprobó la cursada")


"""
EJERCICIO 5:

Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a
Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones):

ECUACIÓN A X + B = 0
Escriba el valor del coeficiente a: 0
Escriba el valor del coeficiente b: 3
La ecuación no tiene solución.

ECUACIÓN A X + B = 0
Escriba el valor del coeficiente a: 4.2
Escriba el valor del coeficiente b: 21
La ecuación tiene una solución: -5.0

ECUACIÓN A X + B = 0
Escriba el valor del coeficiente a: 0
Escriba el valor del coeficiente b: 0
Todos los números son solución.

"""

a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))

if a == 0 and b != 0:
    print("La ecuación no tiene solución.")
elif a == 0 and b == 0:
    print("Todos los números son solución.")
else:
    x = -b / a
    print(f"La ecuación tiene una solución: {x}")


"""
EJERCICIO 6:

Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.

Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que todos los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)

Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones).

a	b	c	Solución
1	-2	2	Sin solución real
2	-7	3	Dos soluciones: 0.5 y 3.0
1	2	1	Una solución: -1.0
0	0	5	Sin solución
0	0	0	Todos los números son solución
0	3	2	Una solución: -0.666...

"""

a = float(input("Ingrese el valor del coeficiente a: "))
b = float(input("Ingrese el valor del coeficiente b: "))
c = float(input("Ingrese el valor del coeficiente c: "))

if a == 0 and b == 0 and c == 0:
    print("Todos los números son solución")
elif a == 0 and b == 0 and c != 0:
    print("Sin solución")
elif a == 0 and b != 0:
    x = -c / b
    print(f"Una solución: {x}")
elif (b**2 - 4 * a * c) == 0:
    # Si el discriminante es igual a cero existe una solución
    x = (-b) / (2 * a)
    print(f"Una solución: {x}")
elif (b**2 - 4 * a * c) > 0:
    # Si el discriminante es mayor a cero existen dos soluciones
    x1 = ((-b) + (b**2 - 4 * a * c)**0.5) / (2 * a)
    x2 = ((-b) - (b**2 - 4 * a * c)**0.5) / (2 * a)
    print(f"Dos soluciones: {x1} y {x2}")
else:
    # Si el discriminante es menor a cero no existe solución real
    print("Sin solución real")


"""
EJERCICIO 7:

Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.

Nota: Utilice como valor de pi el valor 3.141592.

"""

respuesta = input("¿Desea calcular el área de un triángulo (T/t) o de un círculo (C/c)?: ")

while not (respuesta == "T" or respuesta == "t" or respuesta == "C" or respuesta == "c"):
    respuesta = input("Opción inválida. Ingrese T/t para triángulo o C/c para círculo: ")

if respuesta == "T" or respuesta == "t":
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area_triangulo = base * altura / 2
    print(f"El área del triángulo es {area_triangulo}")
elif respuesta == "C" or respuesta == "c":
    radio = float(input("Ingrese el radio: "))
    area_circulo = 3.141592 * radio**2
    print(f"El área del círculo es {area_circulo}")


"""
EJERCICIO 8:

Escriba un programa que pida tres números y diga si el tercero está más cerca del primero o del segundo.
"""

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Calculo la distancia entre el tercer y primer número. En caso de ser negativa la convierto a positiva
distancia31 = numero3 - numero1
if distancia31 < 0:
    distancia31 = -distancia31

# Calculo la distancia entre el tercer y segundo número. En caso de ser negativa la convierto a positiva
distancia32 = numero3 - numero2
if distancia32 < 0:
    distancia32 = -distancia32

# Comparo las distancias
if distancia31 == distancia32:
    print("El tercer número está a la misma distancia de ambos")
elif distancia31 < distancia32:
    print("El tercer número está más cerca del primero")
else:
    print("El tercer número está más cerca del segundo")
