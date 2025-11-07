#Punto 1
def imprimir_hola_mundo():
    print("Hola Mundo")
imprimir_hola_mundo

#Punto 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre_usuario = input("¿Como te llamas? ")
print(saludar_usuario(nombre_usuario))

#Punto 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Punto 4
import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio = float(input("Ingresa el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Area del circulo: {area:.2f}")
print(f"Perimetro del circulo: {perimetro:.2f}")

#Punto 5
def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    return horas,minutos
segundos = int(input("Ingresa la cantidad de segundos: "))
horas, minutos = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} y {minutos} minutos")

#Punto 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingresa un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Punto 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")

#Punto 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en m: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

#Punto 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit:2.f} grados Fahrenheit")

#Punto 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
c = float(input("Ingresa el tercer numero: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de los numeros es: {promedio:.2f}")