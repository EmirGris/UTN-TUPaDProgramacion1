#Punto 1
#Solicita la edad del usuario
edad = int(input("Ingrese su edad: "))
#Verificamos si es mayor de edad
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#Punto 2
#Soliticamos la nota al usuario
nota = int(input("Ingrese su nota: "))
#Pedimos que muestre si esta aprobado o desaprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Punto 3
#Pedimos que ingrese un numero
numero = int(input("Ingrese un numero: "))
#Usamos el operador % para verificar si es par
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Punto 4
#Pedimos al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))
#Verificamos si es niño, adolescente, joven adulto o adulto
if edad <= 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Punto 5
#Pedimos que ingrese una contraseña
Contraseña = input("Ingrese su contraseña: ")
#Usamos el len para obtener la cantidad de elementos en un iterable
if 8 <= len(Contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor,ingrese una contraseña de entre 8 a 14 caracteres")

#Punto 6
import statistics
import random
numeros_aleatorios = [random.randint(1, 100)for i in range (50)]
#Calcular el mode, median y mean
moda = statistics.mode(numeros_aleatorios)
moda = -1
print("Nota: No se pudo calcular la moda de forma unica")
mediana = statistics.mode(numeros_aleatorios)
media = statistics.mode(numeros_aleatorios)
print(f"Lista de numeros aleatorios:{numeros_aleatorios}...")
print(f"Mode: {moda}")
print(f"Median: {mediana}")
print(f"Mean: {media}")
#Determinar el sesgo
if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")
else:
    print("El sesgo de la distribucion es indefinido o no se ajusta a las categorias dadas")

#Punto 7
frase = input("Ingrese una frase o palabra: ")
if frase[-1] in "aeiouAEIOU":
    print(frase + "!")
else:
    print(frase)

#Punto 8
Nombre = input("Ingrese su nombre: ")
Opcion = int(input("Ingrese 1, 2 o 3 dependiendo la opcion que desee: 1.Mayuscula, 2.Minusculas, 3. Primera letra mayuscula:"))
if Opcion == 1:
    print(Nombre.upper())
elif Opcion == 2:
    print(Nombre.lower())
elif Opcion == 3:
    print(Nombre.title())
else:
    print("Opcion no valida")

#Punto 9
Magnitud = float(input("Ingrese la magnitud del terreno: "))
if Magnitud < 3:
    print("Muy leve (imperceptible)")
elif Magnitud >= 3 and Magnitud <4:
    print("Leve (Ligeramente imperceptible)")
elif Magnitud >= 4 and Magnitud <5:
    print("Moderado (Sentido por personas, pero generalmente no causa daños)")
elif Magnitud >= 5 and Magnitud <6:
    print("Fuerte (Puede causar daños en estructuras debiles)")
elif Magnitud >= 6 and Magnitud <7:
    print("Muy fuerte (Puede causar daños significativos)")
elif Magnitud >= 7:
    print("Extremo (Puede causar graves daños a gran escala)")
else:
    print("Valor no valido")

#Punto 10
Hemisferio = input("Ingrese el hemisferio (N para norte, S para sur):").upper()
Mes = int(input("Ingrese el numero del mes (1-12):"))
Dia = int(input("Ingrese el dia del mes (1-31):"))
if Hemisferio == "N":
    if (Mes == 12 and Dia >= 21) or Mes in [1,2] or (Mes == 3 and Dia <= 20):
        Estacion = "Invierno"
    elif(Mes == 3 and Dia >= 21) or Mes in [4,5] or (Mes == 6 and Dia <= 20):
        Estacion = "Primavera"
    elif (Mes == 6 and Dia >= 21) or Mes in [7,8] or (Mes == 9 and Dia <= 20):
        Estacion = "Verano"
    elif (Mes == 9 and Dia >= 21) or Mes in [10,11] or (Mes == 12 and Dia <= 20):
        Estacion = "Otoño"
    else:
        Estacion = "Dato Invalido"
elif Hemisferio == "S":
    if (Mes == 12 and Dia >= 21) or Mes in [1, 2] or (Mes == 3 and Dia <= 20):
        estacion = "Verano"
    elif (Mes == 3 and Dia >= 21) or Mes in [4, 5] or (Mes == 6 and Dia <= 20):
        estacion = "Otoño"
    elif (Mes == 6 and Dia >= 21) or Mes in [7, 8] or (Mes == 9 and Dia <= 20):
        estacion = "Invierno"
    elif (Mes == 9 and Dia >= 21) or Mes in [10, 11] or (Mes == 12 and Dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Dato inválido"
else:
    estacion = "Hemisferio no válido" 
print("La estacion es:", Estacion)