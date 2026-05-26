# 1

def crear_lista(tamanio: int, elemento_base: any = 0) -> list:
    return [elemento_base] * tamanio    

# 2

def cargar_lista(lista: list, oracion: str) -> None:

    for i in range(len(lista)):

        valor = int(input(oracion))

        lista[i] = valor

numeros = crear_lista(5)

cargar_lista(numeros, "ingrese un numero: ")

print(numeros)

# 3

def promedio_lista(lista:list)->float:
    suma = 0

    for i in lista:
        suma += i

    promedio = suma / len(lista)

    return promedio

lista = [1,2,3,4]

resultado = promedio_lista(lista)

print(resultado)

# 4

def promedio_lista(lista:list)->float:
    suma = 0
    contador = 0

    for i in lista:
        if i > 0:
            suma += i
            contador += 1

    promedio = suma / contador

    return promedio

lista = [0,2,-3,4]

resultado = promedio_lista(lista)

print(resultado)

# 5

def producto_lista(lista:list)->float:
    producto = 1

    for i in lista:
        producto *= i 
    return producto

lista = [1,2,3,4]

resultado = producto_lista(lista)

print(resultado)

# 6

def maximo_lista(lista:list)->int:
    maximo = lista[0]
    posicion = 0

    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posicion = i

    return posicion

lista = [6,10,5,8]

resultado = maximo_lista(lista)

print(resultado)

# 7

def posicion_lista(lista:list)->list:
    maximo = lista[0]
    posicion = []

    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]

    for i in range(len(lista)):
        if lista[i] == maximo:
             posicion.append(i)
    
    return posicion

lista = [6,10,5,12]

resultado = posicion_lista(lista)

print(resultado)

# 8

def reemplazar_nombres(lista_nombres:list, nombre_antiguo:str, nombre_nuevo:str)->int:
    contador = 0

    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            contador += 1

    return contador

lista = ["Emiliano", "Axel", "Martin", "Juan"]

resultado = reemplazar_nombres(lista,"Juan","Pepe")

print(lista)

print(resultado)

# 9

def interseccion_lista(lista1:list, lista2:list)->list:
    interseccion = []

    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                interseccion.append(lista1[i])
        
    return interseccion

lista1 = [6,10,5,12]
lista2 = [6,12,4,10]

resultado = interseccion_lista(lista1, lista2)

print(resultado)

# 10 

def union_lista(lista1:list, lista2:list)->list:
    union = []

    for i in range(len(lista1)):
        union.append(lista1[i])

    for j in range(len(lista2)):
        if lista2[j] not in union:
            union.append(lista2[j])
        
    return union

lista1 = [6,10,5,12]
lista2 = [6,12,4,10]

resultado = union_lista(lista1, lista2)

print(resultado)

# 11

def diferencia_lista(lista1: list,lista2: list)->list:
    diferencia = lista1.copy()

    for i in range(len(lista2)):
        for j in range(len(diferencia)):
            if lista2[i] == diferencia[j]:
                diferencia.pop(j)
                break

    return diferencia


lista1 = [6,10,5,12]
lista2 = [6,12,4,10]

resultado = diferencia_lista(lista1, lista2)

print(resultado)
