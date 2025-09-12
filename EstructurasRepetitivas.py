#Ejercicio 1
for i in range ("0,101"):
    print(i)

#Ejercicio 2
numero =int(input("Ingresa un numero entero: "))
contador = 0
while numero != 0:
    numero=numero//10
    contador+=1
print("La cantidad de digitos es de: ",contador)

#Ejercicio 3
inicio = int(input("Ingrese el primer valor: "))
fin= int(input("Ingrese el segundo valor: "))
if inicio > fin:
    inicio, fin = fin, inicio 
suma = 0
for i in range (inicio+1,fin):
    suma += 1
print("La suma de los numeros entre", inicio, "y", fin, "es:",suma)

#Ejercicio 4
suma = 0
while True:
    numero = int(input("Ingrese un numero entero (0 para terminar): "))

    if numero == 0:
        break

    suma += numero

print("La suma total es:", suma)

#Ejercicio 5
import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinanza = -1
numero = int(input("Adivina el numero aleatorio entre 0 y 9: "))
while adivinanza != numero_secreto:
    try:
        adivinanza = int(input("Ingresa tu numero: "))
        intentos += 1
    except ValueError:
        print("Por favor, ingresa un numero valido")
        continue

print(f"Felicidades, adivinaste el numero {numero_secreto} en {intentos} intentos")

#Ejercicio 6
for i in range (100,-1,-1):
    if i % 2 == 0:
        print(i)

#Ejercicio 7
num = int(input("Ingrese un numero entero positivo: "))
if num < 0:
    print("El numero tiene que ser positivo")
else:
    suma = 0
    for i in range (0,num + 1):
     suma += i
print("La suma de los numeros comprendidos entre 0 y",num,"es de:",suma)

#Ejercicio 8
contador_num = 0
cont_positivos = 0
cont_negativos = 0
cont_pares = 0
cont_impares = 0
while contador_num < 100:
    num=int(input("Ingrese un numero entero: "))
    if num > 0 and num % 2 == 0:
        cont_positivos += 1
        cont_pares += 1
    elif num < 0 and num % 2 == 0:
        cont_negativos += 1
        cont_pares += 1
    elif num % 2 != 0 and num < 0:
        cont_impares += 1
        cont_negativos += 1
    elif num % 2 != 0 and num > 0:
        cont_impares += 1
        cont_positivos += 1
    else:
        print("El numero ingresado es 0 o no es entero")

print("El total de numeros pares es de:",cont_pares)
print("El total de numeros impares es de:",cont_impares)
print("El total de numeros negativos es de",cont_negativos)
print("El total de numeros positivos es de:",cont_positivos)

#Ejercicio 9
suma=0
contador=0
while contador<100:
    num=int(input("Ingrese un numero entero: "))
    suma += num
    contador +=1
media=suma/100
print("LA media de la suma de los numeros enteros es de: ",media)

#Ejercicio 10
numero = input("Ingresa un numero entero: ")
if numero.startswith("-"):
    numero_invertido = "-" + numero[:0:-1]
else:
    numero_invertido = numero[::-1]
print("Numero invertido:", numero_invertido)