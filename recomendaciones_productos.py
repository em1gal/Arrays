def crear_lista(tamanio: int, elemento_base: any = 0) -> list:
    return [elemento_base] * tamanio    

def cargar_lista(lista: list, oracion: str) -> None:

    for i in range(len(lista)):

        valor = input(oracion)

        lista[i] = valor

productos = crear_lista(5)

cargar_lista(productos, "ingrese un producto: ")

print(productos)

# 1

def productos_comun_lista(lista1:list, lista2:list)->list:
    interseccion = []

    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                interseccion.append(lista1[i])
        
    return interseccion

lista1 = [ "Mouse","Auriculares", "Monitor","Webcam"]

lista2 = [ "Televisor", "Auriculares", "Mouse", "celular"]

resultado = productos_comun_lista(lista1, lista2)

print(resultado)

# 2

def exclusivo_lista(lista1: list,lista2: list)->list:
    diferencia = lista1.copy()

    for i in range(len(lista2)):
        for j in range(len(diferencia)):
            if lista2[i] == diferencia[j]:
                diferencia.pop(j)
                break

    return diferencia


lista1 = [ "Mouse","Auriculares", "Monitor","Webcam"]

lista2 = [ "Televisor", "Auriculares", "Mouse", "celular"]

resultado = exclusivo_lista(lista1, lista2)

print(resultado)

# 3

def catalogo_lista(lista1:list, lista2:list)->list:
    union = []

    for i in range(len(lista1)):
        union.append(lista1[i])

    for j in range(len(lista2)):
        if lista2[j] not in union:
            union.append(lista2[j])
        
    return union

lista1 = [ "Mouse","Auriculares", "Monitor","Webcam"]

lista2 = [ "Televisor", "Auriculares", "Mouse", "celular"]

resultado = catalogo_lista(lista1, lista2)

print(resultado)

# 4


recomendacion1 = exclusivo_lista(lista2, lista1)

print("Recomendaciones usuario 1:", recomendacion1)

recomendacion2 = exclusivo_lista(lista1, lista2)

print("Recomendaciones usuario 2:", recomendacion2)