#Trabajo Practico - Listas
#Punto 1
multiplos = list(range(4, 101, 4))
print(multiplos)

#Punto 2
elementos = ["auto","camioneta","bicicleta","moto","patineta"]
print(elementos[-2])

#Punto 3
lista = []
lista.append("nariz")
lista.append("boca")
lista.append("ojos")
print(lista)

#Punto 4
animales = ["jirafa","oso","tigre","puma"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Punto 5
numero = [8, 15, 3, 22, 7]
numero.remove(max(numero))
print(numero)
#Elimina el numero mas grande de la lista de "numero"

#Punto 6
numero = list(range(10, 31, 5))
print(numero[:2])

#Punto 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["ford", "chevrolet"]
print(autos)

#Punto 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Punto 9
compras = [["pan","leche"], ["arroz","fideos","salsa"],
["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Punto 10
lista_vacia = []
lista_vacia.append(15)
lista_vacia.append(True)
lista_vacia.append([25.5, 57.9, 30,6])
lista_vacia.append(False)
print(lista_vacia)