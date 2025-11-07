#Ejercicio 1
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


n = int(input("Ingrese un número entero: "))
print("Factoriales del 1 al",n,"son:")
for i in range(1, n + 1):
    print(f"El factorial de {i} es {factorial(i)}")

#Ejercicio 2
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {n}:")
for i in range(n):
    print(fibonacci(i))

#Ejercicio 3
def potencia(base, exponente):
    
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)

print(f"{base} elevado a la {exponente} es igual a {resultado}")

#Ejercicio 4
def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num // 2) + str(num % 2)
    
n = int(input("Ingrese un número entero positivo en base decimal: "))
binario = decimal_a_binario(n)
if binario == "":
    binario = "0"
print(f"La representación binaria de {n} es: {binario}")

#Ejercicio 5
def es_palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    elif palabra[0] != palabra[-1]:
        return False 
    else:
        
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo")
else:
    print(f"'{texto}' no es un palíndromo")

#Ejercicio 6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10) 

numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1) 
    
niveles = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
total_bloques = contar_bloques(niveles)
print(f"El total de bloques necesarios para construir la pirámide es: {total_bloques}")

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        contador = 1 if numero % 10 == digito else 0
        return contador + contar_digito(numero // 10, digito)
input_numero = int(input("Ingrese un número entero positivo: "))
input_digito = int(input("Ingrese un dígito (entre 0 y 9): "))
resultado = contar_digito(input_numero, input_digito)
print(f"El dígito {input_digito} aparece {resultado} veces en el número {input_numero}.")