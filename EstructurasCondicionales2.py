#Ejercicio 1
#El programa define una contraseña fija, despues pide que el usuario ingrese una contraseña y verifica si esta bien o mal
#Que pasaria si el usuario ingresa la contraseña en mayuscula?
#La contraseña estaria mal y tendria que intentar una contraseña denuevo
#Como mejorarias el programa para dar mas intentos?
#Usar un bucle que permita mas intento al usuario, un bucle for que limite los intentos a 3

#Ejercicio 2

vocal = input("Ingrese una letra: ")
if vocal in "aeiouAEIOU":
    print("La letra ingresada es una vocal ")
else:
    print("La letra ingresada NO es una vocal")
#¿Cómo manejarías vocales acentuadas (á, é)?
#Las agregaria en la cadena de comparacion
#¿Qué estructura usarías para simplificar las comparaciones?
#Dejaria la estructura que utilice

#Ejercicio 3

numero = int(input("Ingrese un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")
#¿Qué ocurre si el usuario ingresa un texto?
#El programa lanzara un error porque intentara convertir el texto a entero
#¿Cómo adaptarías el código para números decimales?
#Cambiaria el int por float para permitir numero con decimales

#Ejercicio 4
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
if num1 > num2:
    print("El primer numero ingresado es mayor")
elif num1 < num2:
    print("El primer numero ingresado es menor")
else:
    print("Los numeros ingresados son iguales")

#¿Cómo modificarías el programa para comparar más de dos números?
#Usaria bucles para comparar elemento a elemento o encontrar igualdad
#¿Qué pasa si se ingresan valores no numéricos?
#Daria un error, porque intentaria convertir el texto a float

#Ejercicio 5
temperatura = float(input("Ingrese la temperatura actual en °C"))
if temperatura <= 10:
    print("Hace frio")
elif temperatura > 10 and temperatura <= 25:
    print("Esta templado")
else:
    print("Hace calor")

#¿Cómo adaptarías el programa para usar °F?
#Pedir la temperatura directamente en °F y ajustar los rangos segun la escala
#Convertir °F a °C utilizando la formula de conversion
#¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?
#Tendria en consideracion el bajo cero

#Ejercicio 6
año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Se ingreso un año bisiesto")
else:
    print("Se ingreso un año no bisiesto")

#¿Por qué el año 1900 no es bisiesto?
#Porque es divisible por 100 pero no por 400
#¿Cómo validarías que el año sea positivo?
#Agregaria una condicion para verificar que el año sea mayor que 0

#Ejercicio 7

frase = input("Ingrese una palabra o frase: ")
if frase [-1] != ".":
    print(frase+".")
else:
    print(frase)

#¿Cómo manejarías frases que terminan con espacios?
#Usaria strip() para eliminar los espacios al final
#¿Qué otros caracteres de puntuación podrías considerar?
#Signo de exlamacion, de pregunta,comas, puntos y comas, etc

#Ejercicio 8

contraseña = input("Crea una contraseña: ")
if len(contraseña) > 8 and len(contraseña) <= 20 and any(c.isupper()for c in contraseña) and any(c.isdigit() for c in contraseña):
    print("¡Felicitaciones! Creaste tu contraseña.")
else:
    print("La contraseña no es segura")

# ¿Cómo añadirías la regla de usar un carácter especial?
#Usaria la funcin any() junto con una lista de caracteres especiales
#¿Por qué es importante limitar la longitud máxima?
#Limitar la longitud maxima de una contraseña es importante para evitar que sea demasiado larga, lo que podria dificultar su manejo y almacenamiento

#Ejercicio 9
contraseña=input("Ingrese una contraseña: ")
if len(contraseña) <8:
    print("La contraseña no es segura.Debe tener al menos 8 caracteres")
elif len(contraseña) >20:
    print("La contraseña no es segura. Debe tener menos de 20 caracteres")
elif not any(c.isupper()for c in contraseña):
    print("La contraseña no es segura. Debe tener al menos una mayuscula")
elif not any(c.isdigit() for c in contraseña):
    print("La contraseña no es segura. Debe tener al menos un numero.")
else:
    print("Felicitaciones! Creaste tu contraseña")

#¿Cómo evitarías repetir código al verificar cada condición?
#Usaria una lista para almacenar los mensajes de error y luego imprimirlos todos juntos al final si hay errores
#¿Qué ventajas tiene este enfoque para el usuario?
#Este enfoque proporciona retroalimentacion especifica sobre que aspectos de la contraseña no cumplen con los requisitos

#Ejercicio 10
jugador1 = input("Jugador 1, ingrese su jugada(piedra,papel o tijera): ").lower()
jugador2 = input("Jugador 2, ingrese su jugada(piedra,papel o tijera): ").lower()

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra"):
    print("Jugador 1 gana")
elif jugador1 == jugador2:
    print("Empate")
else:
    print("Jugador 2 gana")

#¿Cómo manejarías entradas inválidas (ej: "piedra" mal escrito)?
#Si la entrada no es valida, mostraria un mensaje de error y pediria al usuario que ingrese nuevamente
#¿Qué estructura usarías para simplificar las comparaciones?
#Usaria un diccionario para mapear las jugadas y sus resultados
