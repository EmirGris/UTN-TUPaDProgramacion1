print ("Hola Mundo!") #Ejercicio 1

Nombre = input("Ingrese su nombre ") #Ejercicio 2
print(f"Hola {Nombre}!")

Nombre =input("Ingrese su nombre ") #Ejercicio 3
Apellido =input("Ingrese su apellido ")
Edad =input("Ingrese su edad ")
Localidad =input("Ingrese su Localidad ")
print(f"Soy {Nombre} {Apellido},tengo {Edad} y vivo en {Localidad}")

import math #Ejercicio 4

radio =float(input("Ingrese el radio del circulo: "))
area=math.pi*radio**2
perimetro= 2*math.pi*radio

print("El valor del area es ",area)
print("El valor del perimetro es ",perimetro)

Segundos =int(input("Ingresa la cantidad de segundos ")) #Ejercicio 5
Horas =Segundos/3600
print(f"{Segundos} Equivale a {Horas} Horas ")

print ("Tablas de Multiplicar") #Ejercicio 6
Numero=int(input("Ingrese un numero "))
print(f"Tabla de multiplicar del {Numero}:")
for i in range(1, 11):
 resultado = Numero * i
 print(f"{Numero} x {i} = {resultado}")

Numero=int(input("Ingrese un numero entero (distinto del 0): ")) #Ejercicio 7
Numero2=int(input("Ingrese otro numero entero (distinto del 0): "))
if Numero == 0 or Numero2 == 0:
 print("Los numeros no pueden ser 0 ")
Suma = Numero + Numero2
Resta = Numero - Numero2
if Numero2 != 0:
 Division = Numero / Numero2
 Multiplicacion = Numero * Numero2 
print(f"Resultado de las operaciones con los numeros {Numero} y {Numero2}:")
print(f"{Numero} + {Numero2} = {Suma} ")
print(f"{Numero} - {Numero2} = {Resta} ")
print(f"{Numero} / {Numero2} = {Division} ")
print(f"{Numero} * {Numero2} = {Multiplicacion} ")

Altura=float(input("Ingrese su altura en metros: ")) #Ejercicio 8
Peso=float(input("Ingrese su peso en kg: "))
imc= Peso/(Altura)**2
print("Su indice de masa corporal es de: ",round (imc,2))

Grados_c=float(input("Ingrese la temperatura en celsius: ")) #Ejercicio 9
Grados_f=((9/5)*Grados_c) + 32

print(f"La temperatura {Grados_c} grados celsius quivales a: ",round (Grados_f,2),"Fahrenheit")

Numero=int(input("Ingrese el primer numero: ")) #Ejercicio 10
Numero2=int(input("Ingrese el segundo numero: "))
Numero3=int(input("Ingrese el tercer numero: "))

promedio=(Numero+Numero2+Numero3)/3

print("El promedio de los 3 numeros es de: ",promedio)