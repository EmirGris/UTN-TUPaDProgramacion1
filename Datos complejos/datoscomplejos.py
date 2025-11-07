#Punto 1
precios_frutas = {"Banana":1200, "Anana":2500, "Melon":3000, "Uva":1450}
precios_frutas["Naranja"] =1200
precios_frutas["Manzana"] =1500
precios_frutas["Pera"] =2300
print(precios_frutas)

#Punto 2
precios_frutas["Banana"] =1330
precios_frutas["Manzana"] =1700
precios_frutas["Melon"] =2800
print(precios_frutas)

#Punto 3
frutas = list(precios_frutas.keys())
print(frutas)

#Punto 4
contactos = {}
for i in range(5):
    nombre = input("Introduce el nombre del contacto: ")
    numero = input(f"Introduce el numero de telefono de {nombre}: ")
    contactos[nombre] = numero
nombre_consulta = input("Introduce el nombre para consultar el numero: ")
if nombre_consulta in contactos:
    print(f"El numero de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print("El contacto no existe")

#Punto 5
frase = input("Introduce una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print("Palabras unicas:", palabras_unicas)
print("Recuento:", recuento)

#Punto 6
alumnos = {}
for i in range(3):
    nombre = input("Introduce el nombre del alumno: ")
    nota1 = float(input("Ingrese la primer nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercer nota: "))
    alumnos[nombre] = (nota1, nota2, nota3)
print("\nPromedio de cada alumno: ")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#Punto 7
parcial1 = {"Juan", "Ana", "Carlos", "Lucia", "Marta"}
parcial2 = {"Carlos", "Marta", "Luis", "Ana", "Pedro"}
aprobados_ambos = parcial1 & parcial2
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
aprobados_solo_uno = parcial1 ^ parcial2
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)
aprobaron_al_menos_uno = parcial1 | parcial2
print("Estudiantes que aprobaron al menos un parcial:", aprobaron_al_menos_uno)

#Punto 8
stock = {
    "manzanas": 50,
    "bananas": 30,
    "naranjas": 20
}
print("Stock actual:", stock)

producto = input("\nIngrese el nombre del producto que desea consultar: ")


if producto in stock:
    print(f"El stock actual de '{producto}' es: {stock[producto]} unidades.")
    
    agregar = input("¿Desea agregar unidades a este producto? (s/n): ")
    if agregar == "s":
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de '{producto}': {stock[producto]} unidades.")
    else:
        print("No se realizaron cambios.")
else:
   
    print(f"El producto '{producto}' no existe en el stock.")
    agregar_nuevo = input("¿Desea agregarlo? (s/n): ")
    if agregar_nuevo == "s":
        cantidad = int(input("Ingrese la cantidad inicial: "))
        stock[producto] = cantidad
        print(f"Se agregó '{producto}' con {cantidad} unidades al stock.")
    else:
        print("No se agregó ningún producto nuevo.")

print("\nStock actualizado:", stock)

#Punto 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Desayuno con amigos",
    ("jueves", "14:30"): "Cita médica",
}
dia = input("Ingrese el dia de la semana: ")
hora = input("Ingrese la hora (HH:MM): ")
clave = (dia, hora)
if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay ninguna actividad programada para ese dia y hora")

#Punto 10
original ={
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Peru": "Lima",
    "Colombia": "Bogota"
}
invertido = {capital: pais for pais, capital in original.items()}
print("Diccionario invertido:", invertido)