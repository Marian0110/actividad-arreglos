"""3 UNIDAD PROGRAMACION DE ALGORITMOS: en esta unidad se ven: listas, arreglos, funciones"""

"""Arreglos unidimensionales"""

#Ejercicio 1: Crear un arreglo unidimensional de tamaño 10, con elementos aleatorios de números enteros del 0 al 100, para ello deberá investigar
#la función que permita crear números aleatorios.

#funcion que permite crear numeros aleatorios = random (import random) random.randint genera numeros entre el rango que se especifique

import numpy as np
import random

arreglo = []
for i in range(10):
    aleatorios = random.randint(0, 100)
    arreglo.append(aleatorios)
print(arreglo)


# #Ejercicio 2: Crear una copia del arreglo y muestre: Elemento mayor, Elemento menor, Suma de los elementos, Promedio de los elementos.
# # Mostrar todos los elementos
copia_arreglo = arreglo.copy()
elementoMayor = max(copia_arreglo)
elementoMenor = min(copia_arreglo)
suma = sum(copia_arreglo)
promedio = np.mean(copia_arreglo)  

print(f"El elemento mayor de este arreglo es: {elementoMayor}")
print(f"El elemento menor de este arreglo es: {elementoMenor}")
print(f"La suma de este arreglo es: {suma}")
print(f"El promedio de este arreglo es: {promedio}")

print(" ")

"""Arreglos bidimensionales"""
#Ejercicio 1: Crear un arreglo de dos dimensiones de tamaño 3 x 3, con elementos aleatorios de números enteros del 0 al 100.
arreglo2 = np.zeros((3, 3), dtype=int)
for i in range(3):
        for x in range(3):
              arreglo2[i][x] = random.randint(0, 100)
print(arreglo2)

#Ejercicio 2: Utilice las siguientes funciones en el arreglo creado en el punto 1:Promedio de los elementos,Suma de los elementos,
# Mostrar el elemento mayor,Mostrar el elemento menor,Mostrar sólo los elementos de la diagonal principal.

print("el promedio de este arreglo bidimensional es:", round(arreglo2.mean()))
print(f"la suma de este arreglo bidimensional es: {arreglo2.sum()}")
print(f"el numero mayor de este arreglo bidimensional es: {arreglo2.max()}")
print(f"el numero menor de este arreglo bidimensional es: {arreglo2.min()}")
print(f"elementos diagonales:{np.diag(arreglo2)}")

#Ejercicio 3: Crear un arreglo de dos dimensiones de 3 x 3 con números ceros, excepto la diagonal principal que debe contener en el mismo orden
# los siguientes elementos: 1, 2 y 3

arreglo3 = np.diag([1, 2, 3])
print(arreglo3)

print(" ")

"""4_1_2 ACT ARREGLOS"""
#Ejercicio 1: Se requiere crear un vector de tamaño 100, completar los valores del vector aleatoriamente con números enteros del 0 al 10

vector = []
for i in range(100):
      ale = random.randint(0, 10)
      vector.append(ale)
# Mostrar por pantalla sólo los valores que se encuentren en los índices pares
indicesPares = vector[2:100:2]
print(f"los valores de los indices pares en este vector son:",indicesPares)

# Mostrar el elemento mayor, sólo 1 en caso de repetirse.
print("El elemento mayor de este vector es:", max(vector))

# Mostrar el índice (posición) del elemento mayor
mayor = max(indicesPares)
indiceMayor = [i for i, poscicion in enumerate(indicesPares) if poscicion == mayor]

print("Los indices del numero mayor son:", indiceMayor)

#Mostrar el numero menor
print(f"El numero menor de este vector es: {min(indicesPares)}")

#Mostrar el indice del numero menor
menor = min(indicesPares)
indiceMenor = [i for i, indice in enumerate(indicesPares) if indice == menor]
print("Los indices del numero menor son:", indiceMenor)

#Crear un Vector de tamaño 10 que almacene nombres de personas.
#Crear un menú con las opciones: 1) Agregar persona 2)Ver Persona.
#Donde 1) agregar permita ingresar el nombre de una persona por pantalla mientras el vector no esté completo.
#2) Ver persona permite ver el nombre del índice ingresado por pantalla.

vector2 = []

personas = True
while personas:
    try:
        print("MENU: \n1)Agregar persona\n2)ver nombre de persona agregada\n")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            if len(vector2) >= 10:
                print("El vector esta completo, no puede agregar a mas personas")
            else:
                nombre = input("Ingrese el nombre de la persona: ")
                vector2.append(nombre)
                back = input("se agrego una persona exitosamente, desea volver al menu? (si/no): ")
                if back.lower() != "si":
                    print("Hasta Logo")
                    personas = False
        if op == 2:
            ver = int(input("Ingrese el numero de la persona que desea ver (1-10): "))
            nombre = vector2[ver]
            print(f"El nombre de la persona {ver} es {nombre}")
            back2 = input("desea volver al menu? (si/no): ")
            if back2 != str and back2 != "si":
                print("Saldras del programa")
    except ValueError:
        print("Solo se permiten numeros")
    else:
        print("ingreso invalido, (1-2)")