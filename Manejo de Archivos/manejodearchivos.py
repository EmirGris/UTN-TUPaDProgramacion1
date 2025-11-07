#Ejercicio 1
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Regla,180,45\n")
    archivo.write("Cuaderno,200,25\n")

#Ejercicio 2 y 4
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)
        
#Ejercicio 3
while True:
    print("\nAgregar un nuevo producto:")
    nombre = input("Nombre del nuevo producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(nuevo_producto)

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    print("Producto agregado correctamente.")

    continuar = input("\n¿Desea agregar otro producto? (s/n): ")
    if continuar != "s":
        break

#Ejercicio 5
print("\nBuscar producto por nombre")
buscar = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for p in productos:
    if p["nombre"] == buscar:
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nEl producto no existe en la lista.")
    
#Ejercicio 6
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo 'productos.txt' actualizado correctamente.")
