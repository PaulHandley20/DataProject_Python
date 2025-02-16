# DataProject_Python - Entrega Python-2

## 🐍 Proyecto de Lógica: Katas de Python

Este repositorio contiene la solución de **41 ejercicios de lógica en Python**, resueltos fielmente siguiendo los enunciados originales del documento *enunciadodataprojectpython.pdf*. La solución completa se encuentra en este archivo, que integra tanto la documentación como la implementación de cada ejercicio.

---

## 📋 Tabla de Contenidos
- [📖 Descripción del Proyecto](#-descripción-del-proyecto)
- [📂 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️ Instalación y Requisitos](#-instalación-y-requisitos)
- [🚀 Uso y Ejemplos](#-uso-y-ejemplos)
- [✒️ Autores y Agradecimientos](#-autores-y-agradecimientos)

---

## 📖 Descripción del Proyecto

Este proyecto aborda **41 ejercicios** de Python que ponen a prueba conceptos fundamentales del lenguaje:
- 🔠 **Procesamiento de cadenas:** Análisis, enmascarado y manipulación de texto.
- 📋 **Operaciones sobre listas:** Duplicación de valores, filtrado, reducción y concatenación.
- 🔄 **Funciones Lambda y funciones integradas:** Uso intensivo de `map()`, `filter()` y `reduce()`.
- 🎯 **Recursión y manejo de excepciones:** Ejercicios que refuerzan la robustez del código.
- 🏛 **Programación Orientada a Objetos:** Creación de clases para modelar problemas reales (por ejemplo, `Arbol` y `UsuarioBanco`).

Cada ejercicio se ha desarrollado siguiendo exactamente el enunciado original del archivo *enunciadodataprojectpython.pdf*, asegurando fidelidad y precisión en las soluciones.

---

## 📂 Estructura del Proyecto

El repositorio contiene:
📂 **Entrega Python-2.py** → Archivo único con la solución completa de los **41 ejercicios**.
📄 **README.md** → Documentación del proyecto.
📑 **enunciadodataprojectpython.pdf** → Enunciado original de los ejercicios.

---

## ⚙️ Instalación y Requisitos

### 🔹 Requisitos:
- **Python 3.8 o superior.**

### 🔹 Ejecución:
1. **Clona el repositorio:**
   git clone https://github.com/PaulHandley20/DataProject_Python.git
   
2. **Navega al directorio del proyecto:**
   cd DataProject_Python
   
3. **Ejecuta este archivo:**
  python "Entrega Python-2.py"

---

## 🚀 Uso y Ejemplos

### 🔹 **Frecuencia de Letras:**

texto = "hola mundo"
resultado = contar_frecuencias_letras(texto)
print(resultado)
# Salida: {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}


```

### 🔹 **Uso de Clases:**

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
bob.transferir_dinero(alicia, 80)
alicia.retirar_dinero(50)
print("Saldo de Alicia:", alicia.saldo)
print("Saldo de Bob:", bob.saldo)


Consulta el código completo para ver la solución de cada ejercicio.

---

## ✒️ Autores y Agradecimientos

👤 **Autor:** Paul Handley  
📧 **Contacto:** [paulhandley2001@gmail.com](mailto:paulhandley2001@gmail.com)  
🐙 **GitHub:** [@PaulHandley20](https://github.com/PaulHandley20)

Agradezco a los creadores de los enunciados por proporcionar un material tan completo y retador. 🙌


