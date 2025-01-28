
.1
"**Enunciado**: Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena."
"Los espacios no deben ser considerados."

def contar_frecuencias_letras(cadena):
    frecuencias = {}
    for letra in cadena.replace(" ", ""):
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

texto = "hola mundo"
resultado = contar_frecuencias_letras(texto)
print(resultado)

"**Explicación**: La función `contar_frecuencias_letras` recorre cada letra de la cadena después de eliminar los espacios con `replace(" ", "")`."
"Luego, usa `frecuencias.get(letra, 0) + 1` para actualizar la cuenta de cada letra en un diccionario."



.2
"**Enunciado**: Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función `map()`."

def duplicar_valores(lista):
    return list(map(lambda x: x * 2, lista))

numeros = [1, 2, 3, 4, 5]
resultado = duplicar_valores(numeros)
print(resultado)

"**Explicación**: La función `duplicar_valores` utiliza `map()` para duplicar cada elemento de la lista mediante una expresión lambda."



.3
"**Enunciado**: Crea una función que tome una lista de palabras y una subcadena como entrada y devuelva las palabras que contengan dicha subcadena."

def palabras_con_subcadena(lista_palabras, subcadena):
    return [palabra for palabra in lista_palabras if subcadena in palabra]

lista = ["manzana", "banana", "cereza"]
subcadena = "an"
resultado = palabras_con_subcadena(lista, subcadena)
print(resultado)

"**Explicación**: La función `palabras_con_subcadena` utiliza una comprensión de listas para filtrar las palabras que contienen la subcadena especificada."



.4
"**Enunciado**: Implementa una función que tome dos listas de números y devuelva una nueva lista con la diferencia entre los elementos correspondientes."

def diferencia_elementos(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

resultado = diferencia_elementos([10, 5, 8], [1, 2, 3])
print(resultado)

"**Explicación**: Se usa `map()` con una lambda que resta los valores correspondientes de las dos listas para producir una nueva lista con las diferencias."



.5
"**Enunciado**: Calcula la media de una lista de números y determina si la media es mayor o igual a un valor de aprobación. Devuelve la media y el estado aprobado o suspenso."

def calcular_media_estado(notas, aprobado=5):
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= aprobado else "suspenso"
    return media, estado

print(calcular_media_estado([4, 5, 6]))

"**Explicación**: Calcula la media con `sum` y `len`, y usa una expresión condicional para determinar si se alcanza el valor de aprobación."



.6
"**Enunciado**: Implementa una función que calcule el factorial de un número utilizando recursión."

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

numero = 5
resultado = factorial(numero)
print(resultado)

"**Explicación**: La función `factorial` llama a sí misma hasta alcanzar el caso base `n == 0`, donde devuelve 1. Multiplica sucesivamente los valores decrecientes para obtener el resultado."



.7
"**Enunciado**: Convierte una lista de tuplas en una lista de cadenas concatenando los elementos de cada tupla."

def tuplas_a_cadenas(lista_tuplas):
    return list(map(lambda t: ''.join(map(str, t)), lista_tuplas))

resultado = tuplas_a_cadenas([(1, 2), ('a', 'b')])
print(resultado)

"**Explicación**: Usa `map()` para convertir las tuplas en cadenas concatenadas, utilizando `str()` para asegurar la conversión a texto."



.8
"**Enunciado**: Escribe una función que divida dos números ingresados por el usuario, manejando excepciones para división por cero y errores de entrada."

def dividir_numeros():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        return "Error: Por favor ingresa solo números."
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    else:
        return f"El resultado es {resultado}"

print(dividir_numeros())

"**Explicación**: La función solicita números del usuario, maneja excepciones para errores de tipo y división por cero, y devuelve el resultado o un mensaje de error."



.9
"**Enunciado**: Crea una función que reciba una lista de nombres de mascotas y excluya aquellas que pertenezcan a una lista de mascotas prohibidas."

def excluir_mascotas(lista_mascotas):
    prohibidas = ["Tigre", "Mapache", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

mascotas = ["Perro", "Tigre", "Gato", "Mapache"]
print(excluir_mascotas(mascotas))

"**Explicación**: Usa `filter()` para remover las mascotas prohibidas de la lista proporcionada, devolviendo solo las permitidas."



.10
"**Enunciado**: Implementa una función que calcule el promedio de una lista y levante una excepción personalizada si la lista está vacía."

class ListaVaciaError(Exception):
    pass

def promedio(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía.")
    return sum(lista) / len(lista)

try:
    numeros = []
    print(promedio(numeros))
except ListaVaciaError as e:
    print(e)

"**Explicación**: La función levanta una excepción si la lista está vacía, usando una clase de error personalizada."



.11
"**Enunciado**: Solicita al usuario una edad y verifica que sea un valor entre 0 y 120." 
"Maneja excepciones para entradas no numéricas."

def solicitar_edad():
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")
    except ValueError as e:
        return f"Error: {e}"
    else:
        return f"Edad válida: {edad}"

print(solicitar_edad())

"**Explicación**: La función maneja excepciones para valores fuera de rango y no numéricos."



.12
"**Enunciado**: Devuelve la longitud de cada palabra en una frase usando `map()`."

def longitudes_palabras(frase):
    return list(map(len, frase.split()))

frase = "Python es divertido"
print(longitudes_palabras(frase))

"**Explicación**: Se usa `map(len, frase.split())` para obtener la longitud de cada palabra."



.13
"**Enunciado**: Crea una función que devuelva pares (mayúscula, minúscula) únicos de caracteres de una cadena."

def mayus_minus_unicas(cadena):
    unicos = set(cadena)
    return [(letra.upper(), letra.lower()) for letra in unicos]

resultado = mayus_minus_unicas("Python")
print(resultado)

"**Explicación**: Se usan conjuntos para eliminar duplicados y comprensión de listas para devolver pares."



.14
"**Enunciado**: Devuelve palabras que comienzan con una letra específica usando `filter()`."

def palabras_con_letra(lista_palabras, letra):
    return list(filter(lambda p: p.startswith(letra), lista_palabras))

palabras = ["manzana", "mango", "pera"]
resultado = palabras_con_letra(palabras, "m")
print(resultado)

"**Explicación**: Usa `filter()` con `startswith()` para encontrar palabras que comienzan con la letra dada."



.15
"**Enunciado**: Usa una lambda para sumar 3 a cada número en una lista."

def sumar_tres(lista):
    return list(map(lambda x: x + 3, lista))

print(sumar_tres([1, 2, 3]))

"**Explicación**: Aplica `map()` con una lambda para sumar 3 a cada elemento de la lista."



.16
"**Enunciado**: Filtra palabras de más de n letras de una lista."

def palabras_mas_largas(lista, n):
    return list(filter(lambda p: len(p) > n, lista))

print(palabras_mas_largas(["sol", "estrella", "luz"], 3))

"**Explicación**: Usa `filter()` con `len()` para seleccionar palabras más largas que `n`."



.17
"**Enunciado**: Convierte una lista de dígitos en un número entero usando `reduce()`."

from functools import reduce

def lista_a_numero(lista_digitos):
    return reduce(lambda x, y: x * 10 + y, lista_digitos)

print(lista_a_numero([1, 2, 3, 4]))

"**Explicación**: `reduce()` combina los dígitos en un único valor entero, multiplicando por 10 y sumando."



.18
"**Enunciado**: Filtra una lista de estudiantes, devolviendo solo aquellos con una calificación mayor o igual a 90."

def filtrar_estudiantes(estudiantes):
    return list(filter(lambda est: est['calificación'] >= 90, estudiantes))

alumnos = [{'nombre': 'Ana', 'calificación': 92}, {'nombre': 'Luis', 'calificación': 85}]
print(filtrar_estudiantes(alumnos))

"**Explicación**: Usa `filter()` para devolver solo los estudiantes cuya calificación es 90 o superior."



.19
"**Enunciado**: Filtra números impares de una lista usando una lambda."

def filtrar_impares(lista):
    return list(filter(lambda x: x % 2 != 0, lista))

print(filtrar_impares([1, 2, 3, 4, 5]))

"**Explicación**: `filter()` con una lambda selecciona solo los números impares."



.20
"**Enunciado**: Filtra valores enteros de una lista usando `filter()`."

def filtrar_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

print(filtrar_enteros([1, 'a', 3.5, 4]))

"**Explicación**: `filter()` selecciona elementos que son enteros utilizando `isinstance`."



.21
"**Enunciado**: Calcula el cubo de un número usando una expresión lambda."


cubo = lambda x: x ** 3
print(cubo(3))

"**Explicación**: La lambda eleva `x` al cubo y devuelve el resultado."



.22
"**Enunciado**: Encuentra la suma de los cuadrados de una lista de números usando `map()` y `sum()`."

def suma_cuadrados(lista):
    return sum(map(lambda x: x ** 2, lista))

print(suma_cuadrados([1, 2, 3, 4]))

"**Explicación**: Usa `map()` para elevar al cuadrado cada número y `sum()` para sumar los resultados."



.23
"**Enunciado**: Encuentra el producto de todos los elementos de una lista usando `reduce()`."

from functools import reduce

def producto_lista(lista):
    return reduce(lambda x, y: x * y, lista)

print(producto_lista([1, 2, 3, 4]))

"**Explicación**: `reduce()` multiplica secuencialmente los elementos para obtener el producto total."



.24
"**Enunciado**: Ordena una lista de tuplas por el segundo elemento usando `sorted()`."

def ordenar_por_segundo(lista):
    return sorted(lista, key=lambda x: x[1])

print(ordenar_por_segundo([(1, 3), (4, 1), (2, 2)]))

"**Explicación**: Usa `sorted()` con una lambda que toma el segundo elemento como clave."



.25
"**Enunciado**: Filtra números negativos de una lista."

def filtrar_negativos(lista):
    return list(filter(lambda x: x < 0, lista))

print(filtrar_negativos([-5, 3, -1, 7]))

"**Explicación**: Usa `filter()` con una lambda para seleccionar números menores que 0."



.26
"**Enunciado**: Calcula la suma acumulativa de una lista."

from itertools import accumulate

def suma_acumulativa(lista):
    return list(accumulate(lista))

print(suma_acumulativa([1, 2, 3, 4]))

"**Explicación**: `accumulate()` devuelve la suma parcial acumulada de la lista."



.27
"**Enunciado**: Cuenta la cantidad de palabras en una frase que comienzan con una letra específica."

def contar_palabras_con_letra(frase, letra):
    palabras = frase.split()
    return len([palabra for palabra in palabras if palabra.startswith(letra)])

print(contar_palabras_con_letra("hola hombre hada", "h"))

"**Explicación**: Usa comprensión de listas para filtrar palabras y `len()` para contar."



.28
"**Enunciado**: Convierte una lista de booleanos en un único valor usando `reduce()` con `and`."

from functools import reduce

def todos_verdaderos(lista):
    return reduce(lambda x, y: x and y, lista)

print(todos_verdaderos([True, True, False]))

"**Explicación**: `reduce()` devuelve `True` solo si todos los valores son verdaderos."



.29
"**Enunciado**: Devuelve la intersección de dos listas como conjunto."

def interseccion_listas(lista1, lista2):
    return set(lista1) & set(lista2)

print(interseccion_listas([1, 2, 3], [2, 3, 4]))

"**Explicación**: Usa operadores de conjuntos para encontrar elementos comunes."



.30
"**Enunciado**: Encuentra el valor máximo en una lista de diccionarios por una clave específica."

def max_por_clave(lista_diccionarios, clave):
    return max(lista_diccionarios, key=lambda d: d[clave])

print(max_por_clave([{ "a": 5 }, { "a": 10 }], "a"))

"**Explicación**: Usa `max()` con una lambda para seleccionar el valor máximo según una clave."



.31
"**Enunciado**: Elimina duplicados de una lista manteniendo el orden original."

def eliminar_duplicados(lista):
    vista = set()
    return [x for x in lista if not (x in vista or vista.add(x))]

print(eliminar_duplicados([1, 2, 2, 3, 4, 4]))

"**Explicación**: Usa un conjunto para realizar un seguimiento de los elementos únicos."



.32
"**Enunciado**: Devuelve una lista de los n elementos más grandes de una lista usando `heapq.nlargest()`."

import heapq

def n_mas_grandes(lista, n):
    return heapq.nlargest(n, lista)

print(n_mas_grandes([1, 3, 2, 4, 5], 3))

"**Explicación**: `heapq.nlargest()` devuelve los `n` elementos más grandes de una lista."


.33
"**Enunciado**: Suma los elementos correspondientes de dos listas usando `map()`."

def sumar_listas(lista1, lista2):
    return list(map(lambda x, y: x + y, lista1, lista2))

print(sumar_listas([1, 2, 3], [4, 5, 6]))

"**Explicación**: Usa `map()` para sumar los elementos correspondientes de ambas listas."



34.
"**Enunciado**: Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:"
"crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para"
"manipular la estructura del árbol."
"Código a seguir:"
"1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas."
"2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad."
"3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas."
"4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes."
"5. Implementar el método quitar_rama para eliminar una rama en una posición específica."
"6. Implementar el método"
"info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las"
"mismas."
"Caso de uso:"
"1. Crear un árbol."
"2. Hacer crecer el tronco del árbol una unidad."
"3. Añadir una nueva rama al árbol."
"4. Hacer crecer todas las ramas del árbol una unidad."
"5. Añadir dos nuevas ramas al árbol."
"6. Retirar la rama situada en la posición 2."
"7. Obtener información sobre el árbol"

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]

    def info_arbol(self):
        return {
            'longitud_tronco': self.tronco,
            'numero_ramas': len(self.ramas),
            'longitudes_ramas': self.ramas
        }

# Caso de uso
arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
info = arbol.info_arbol()
print(info)

"**Explicacion**: La clase arbol define un tronco con longitud inicial de 1 y una lista de ramas vacia."
"Los métodos permiten manipular el árbol:" 
"aumentar la longitud del tronco, agregar ramas," 
"hacer crecer todas las ramas, eliminar una rama en una posición específica, y devolver la información del árbol."



.35
"**Enunciado**: Crea la clase UsuarioBanco que representa a un usuario de un banco con nombre, saldo, y si tiene cuenta corriente." 
"Implementa métodos para retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo."

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para retirar.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError("El usuario no tiene saldo suficiente para la transferencia.")
        otro_usuario.retirar_dinero(cantidad)
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# Caso de uso
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)
bob.transferir_dinero(alicia, 80)
alicia.retirar_dinero(50)

print(f"Saldo de Alicia: {alicia.saldo}")
print(f"Saldo de Bob: {bob.saldo}")

"**xplicación: La clase UsuarioBanco tiene atributos para el nombre, el saldo y la cuenta corriente."
"Los métodos implementan las operaciones básicas: retirar_dinero reduce el saldo, transferir_dinero transfiere fondos de otro usuario, y agregar_dinero incrementa el saldo."
"Los errores se manejan lanzando excepciones."



.37
"**Enunciado:** Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra."
"Define primero estas funciones y llámalas dentro de procesar_texto."

def contar_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    resultado = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return ' '.join(resultado)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida o argumentos incorrectos.")

# Caso de uso
texto = "el gato juega con el perro y el perro ladra"
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "perro", "gato"))
print(procesar_texto(texto, "eliminar", "gato"))

"**Explicación:** Se definen las funciones para contar, reemplazar y eliminar palabras."
"La función procesar_texto acepta una opción y llama a la función correspondiente, manejando diferentes números de argumentos según la operación seleccionada."



.38
"**Enunciado:** Genera un programa que determine si es de noche, de día o tarde según la hora proporcionada por el usuario."

def determinar_periodo_del_dia(hora):
    if 0 <= hora < 6 or hora == 24:
        return "Es de noche"
    elif 6 <= hora < 12:
        return "Es de día"
    elif 12 <= hora < 18:
        return "Es la tarde"
    elif 18 <= hora < 24:
        return "Es de noche"
    else:
        return "Hora no válida"

# Caso de uso
try:
    hora = int(input("Introduce la hora (0-23): "))
    resultado = determinar_periodo_del_dia(hora)
    print(resultado)
except ValueError:
    print("Error: Por favor, introduce un número entero.")

"**Explicación:** La función determinar_periodo_del_dia clasifica la hora según los rangos establecidos para noche, día y tarde."
"Se maneja la entrada del usuario con un bloque try-except para validar que sea un número entero."

.39
"**Enunciado:** Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica."
"Las reglas de calificación son:"
"0 a 69: insuficiente"
"70 a 79: bien"
"80 a 89: muy bien"
"90 a 100: excelente"

def determinar_calificacion(calificacion):
    if 0 <= calificacion <= 69:
        return "insuficiente"
    elif 70 <= calificacion <= 79:
        return "bien"
    elif 80 <= calificacion <= 89:
        return "muy bien"
    elif 90 <= calificacion <= 100:
        return "excelente"
    else:
        return "Calificación no válida"

# Caso de uso
try:
    calificacion = int(input("Introduce la calificación (0-100): "))
    resultado = determinar_calificacion(calificacion)
    print(f"La calificación es: {resultado}")
except ValueError:
    print("Error: Por favor, introduce un número entero.")

"**Explicación:** La función determinar_calificacion evalúa la calificación ingresada dentro de los rangos definidos para devolver una descripción textual." 
"Un bloque try-except maneja errores de entrada no numérica."

.40
"**Enunciado:** Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo")" 
"y datos (una tupla con los datos necesarios para calcular el área de la figura)."

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio, = datos
        return 3.1416 * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return 0.5 * base * altura
    else:
        return "Figura no reconocida"

# Casos de uso
print(calcular_area("rectangulo", (5, 10)))  # Área del rectángulo
print(calcular_area("circulo", (7,)))        # Área del círculo
print(calcular_area("triangulo", (6, 8)))    # Área del triángulo

"**Explicación: La función calcular_area toma el nombre de la figura y sus dimensiones dentro de una tupla."
"Dependiendo de la figura, calcula el área correspondiente. Usa el valor de π aproximado a 3.1416 para el área del círculo."



.41
"**Enunciado:** Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento."

def calcular_precio_final():
    try:
        precio_original = float(input("Ingresa el precio original del artículo: "))
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(input("Ingresa el valor del cupón de descuento: "))
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
                print(f"El precio final con descuento es: {precio_final:.2f}€")
            else:
                print(f"Valor del cupón no válido. El precio final es: {precio_original:.2f}€")
        else:
            print(f"No se aplicó descuento. El precio final es: {precio_original:.2f}€")
    except ValueError:
        print("Error: Por favor, introduce valores numéricos válidos.")

# Caso de uso
calcular_precio_final()

"**Explicación:** Se solicitan datos del usuario para calcular el precio final aplicando descuentos. Se valida la entrada numérica y el uso correcto de cupones."
