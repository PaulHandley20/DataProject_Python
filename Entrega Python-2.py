# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
#    de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_frecuencias_letras(cadena):
    frecuencias = {}
    for letra in cadena.replace(" ", ""):
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

print("1.", contar_frecuencias_letras("hola mundo"))


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def duplicar_valores(lista):
    return list(map(lambda x: x * 2, lista))

print("2.", duplicar_valores([1, 2, 3, 4, 5]))


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#    devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def palabras_con_palabra_objetivo(lista_palabras, palabra_objetivo):
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

print("3.", palabras_con_palabra_objetivo(["manzana", "banana", "cereza"], "an"))


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

print("4.", diferencia_listas([10, 5, 8], [1, 2, 3]))


# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#    defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#    que nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#    una tupla que contenga la media y el estado.
def promedio_y_estado(numeros, nota_aprobado=5):
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado

print("5.", promedio_y_estado([4, 5, 6]))


# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("6.", factorial(5))


# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: "".join(map(str, t)), lista_tuplas))

print("7.", tuplas_a_strings([(1, 2), ("a", "b")]))


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#    o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#    indicando si la división fue exitosa o no.
def dividir_dos_numeros():
    try:
        num1 = float(input("8. Ingresa el primer número: "))
        num2 = float(input("8. Ingresa el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("8. Error: Ingresa solo números.")
    except ZeroDivisionError:
        print("8. Error: No se puede dividir por cero.")
    else:
        print("8. El resultado es:", resultado)

dividir_dos_numeros()


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#    excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#    "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()
def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

print("9.", filtrar_mascotas(["Perro", "Tigre", "Gato", "Mapache", "Oso"]))


# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#     excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass

def promedio_con_excepcion(numeros):
    if not numeros:
        raise ListaVaciaError("La lista está vacía.")
    return sum(numeros) / len(numeros)

try:
    print("10.", promedio_con_excepcion([]))
except ListaVaciaError as e:
    print("10.", e)


# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
#     valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def solicitar_edad():
    try:
        edad = int(input("11. Ingresa tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
    except ValueError as e:
        print("11. Error:", e)
    else:
        print("11. Edad válida:", edad)

solicitar_edad()


# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitudes_frase(frase):
    return list(map(len, frase.split()))

print("12.", longitudes_frase("Python es divertido"))


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#     mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()
def letras_mayus_minus(caracteres):
    unicos = set(caracteres)
    return list(map(lambda c: (c.upper(), c.lower()), unicos))

print("13.", letras_mayus_minus("Python"))


# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def palabras_con_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))

print("14.", palabras_con_letra(["manzana", "mango", "pera"], "m"))


# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))
print("15.", sumar_tres([1, 2, 3]))


# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#     todas las palabras que sean más largas que n. Usa la función filter()
def palabras_mas_largas(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda p: len(p) > n, palabras))

print("16.", palabras_mas_largas("sol estrella luz", 3))


# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
#     corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce
def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

print("17.", lista_a_numero([5, 7, 2]))


# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#     (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificación": 92},
    {"nombre": "Luis", "edad": 22, "calificación": 85},
    {"nombre": "Carlos", "edad": 21, "calificación": 90}
]

def filtrar_estudiantes(estudiantes):
    return list(filter(lambda est: est["calificación"] >= 90, estudiantes))

print("18.", filtrar_estudiantes(estudiantes))


# 19. Crea una función lambda que filtre los números impares de una lista dada.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
print("19.", filtrar_impares([1, 2, 3, 4, 5]))


# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
def filtrar_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

print("20.", filtrar_enteros([1, "a", 3.5, 4]))


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda
cubo = lambda x: x ** 3
print("21.", cubo(3))


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().
def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

print("22.", producto_total([1, 2, 3, 4]))


# 23. Concatena una lista de palabras. Usa la función reduce().
def concatenar_palabras(lista):
    return reduce(lambda x, y: x + y, lista)

print("23.", concatenar_palabras(["Hola", " ", "mundo"]))


# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

print("24.", diferencia_total([10, 2, 3]))  # Ejemplo: 10 - 2 - 3 = 5


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    return len(cadena)

print("25.", contar_caracteres("Python"))


# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
resto = lambda a, b: a % b
print("26.", resto(10, 3))


# 27. Crea una función que calcule el promedio de una lista de números.
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

print("27.", promedio([1, 2, 3, 4, 5]))


# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set()
    for elem in lista:
        if elem in vistos:
            return elem
        vistos.add(elem)
    return None

print("28.", primer_duplicado([1, 2, 3, 2, 5]))


# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#     carácter '#', excepto los últimos cuatro.
def enmascarar_variable(var):
    s = str(var)
    if len(s) <= 4:
        return s
    return "#" * (len(s) - 4) + s[-4:]

print("29.", enmascarar_variable(123456789))


# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#     pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

print("30.", son_anagramas("amor", "roma"))


# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#     esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#     lanza una excepción.
def buscar_nombre():
    nombres = input("31. Ingresa una lista de nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    buscar = input("31. Ingresa el nombre a buscar: ").strip()
    if buscar in nombres:
        print(f"31. {buscar} fue encontrado en la lista.")
    else:
        raise Exception("31. Nombre no encontrado.")

try:
    buscar_nombre()
except Exception as e:
    print(e)


# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#     devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#     no trabaja aquí.
def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre_completo"] == nombre_completo:
            return empleado["puesto"]
    return "La persona no trabaja aquí."

empleados = [
    {"nombre_completo": "Juan Perez", "puesto": "Gerente"},
    {"nombre_completo": "Ana Gomez", "puesto": "Secretaria"}
]

print("32.", buscar_empleado("Ana Gomez", empleados))
print("32.", buscar_empleado("Carlos Ruiz", empleados))


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
sumar_elementos = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))
print("33.", sumar_elementos([1, 2, 3], [4, 5, 6]))


# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#     crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#     manipular la estructura del árbol.
#     Código a seguir:
#       1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#       2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#       3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#       4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#       5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#       6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
#     Caso de uso:
#       1. Crear un árbol.
#       2. Hacer crecer el tronco del árbol una unidad.
#       3. Añadir una nueva rama al árbol.
#       4. Hacer crecer todas las ramas del árbol una unidad.
#       5. Añadir dos nuevas ramas al árbol.
#       6. Retirar la rama situada en la posición 2.
#       7. Obtener información sobre el árbol.
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
            self.ramas.pop(posicion)
    def info_arbol(self):
        return {"longitud_tronco": self.tronco, "numero_ramas": len(self.ramas), "longitudes_ramas": self.ramas}

arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
print("34.", arbol.info_arbol())


# 36. Crea la clase UsuarioBanco , representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#     corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
#     agregar dinero al saldo.
#     Código a seguir:
#       1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
#       2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#       3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
#       4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#     Caso de uso:
#       1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#       2. Agregar 20 unidades de saldo de "Bob".
#       3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#       4. Retirar 50 unidades de saldo a "Alicia".
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise Exception("Saldo insuficiente.")
        self.saldo -= cantidad
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise Exception("El otro usuario no tiene saldo suficiente.")
        otro_usuario.retirar_dinero(cantidad)
        self.saldo += cantidad
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
bob.transferir_dinero(alicia, 80)
alicia.retirar_dinero(50)
print("36. Saldo de Alicia:", alicia.saldo)
print("36. Saldo de Bob:", bob.saldo)


# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
#     reemplazar_palabras , eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
#     de la función procesar_texto.
#     Código a seguir:
#       1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
#       2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el remplazo de palabras.
#       3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
#       4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
#     Caso de uso:
#       Comprueba el funcionamiento completo de la función procesar_texto.
def contar_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    return " ".join([p for p in texto.split() if p != palabra_a_eliminar])

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabra(texto, args[0])
    else:
        raise Exception("Opción o argumentos inválidos.")

print("37. (contar)", procesar_texto("el gato juega con el perro y el perro ladra", "contar"))
print("37. (reemplazar)", procesar_texto("el gato juega con el perro y el perro ladra", "reemplazar", "perro", "gato"))
print("37. (eliminar)", procesar_texto("el gato juega con el perro y el perro ladra", "eliminar", "gato"))


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def periodo_del_dia(hora):
    if 0 <= hora < 6 or hora >= 20:
        return "Es de noche"
    elif 6 <= hora < 12:
        return "Es de día"
    elif 12 <= hora < 20:
        return "Es la tarde"
    else:
        return "Hora no válida"

try:
    hora_usuario = int(input("38. Ingresa la hora (0-23): "))
    print("38.", periodo_del_dia(hora_usuario))
except ValueError:
    print("38. Error: Ingresa un número entero.")


# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#     Las reglas de calificación son:
#       - 0 - 69 insuficiente
#       - 70 - 79 bien
#       - 80 - 89 muy bien
#       - 90 - 100 excelente
def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Calificación no válida"

try:
    nota = int(input("39. Ingresa la calificación (0-100): "))
    print("39. La calificación es:", calificacion_texto(nota))
except ValueError:
    print("39. Error: Ingresa un número entero.")


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" )
#     y datos (una tupla con los datos necesarios para calcular el área de la figura).
def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        (radio,) = datos
        return 3.1416 * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return 0.5 * base * altura
    else:
        return "Figura no reconocida"

print("40. (rectángulo)", calcular_area("rectangulo", (5, 10)))
print("40. (círculo)", calcular_area("circulo", (7,)))
print("40. (triángulo)", calcular_area("triangulo", (6, 8)))


# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
#     monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
#       1. Solicita al usuario que ingrese el precio original de un artículo.
#       2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#       3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#       4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
#       5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#       6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.
def calcular_precio_final():
    try:
        precio_original = float(input("41. Ingresa el precio original del artículo: "))
        tiene_cupon = input("41. ¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
        if tiene_cupon in ["sí", "si"]:
            valor_cupon = float(input("41. Ingresa el valor del cupón de descuento: "))
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
            else:
                precio_final = precio_original
        else:
            precio_final = precio_original
        print(f"41. El precio final de la compra es: {precio_final:.2f}€")
    except ValueError:
        print("41. Error: Ingresa valores numéricos válidos.")

calcular_precio_final()
