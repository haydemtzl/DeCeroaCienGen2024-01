# Ejercicios Tareas clase 3

'''Escribe una función que tome una lista de números y devuelva la suma acumulada, 
    es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es 
    la suma del primero con el segundo, el tercer elemento es la suma del resultado anterior 
    con el siguiente elemento y así sucesivamente. 
    Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].'''

def sumaacum(lista):
    temp = 0
    for x in range(len(lista)):
        temp += lista[x] # Es igual que si usara temp = temp + lista[x]
        lista[x] = temp
    return lista


'''Escribe una función "ordenada" que tome una lista como parámetro y devuelva True 
    si la lista está ordenada en orden ascendente y devuelva False en caso contrario.
    Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False.
'''

def ordenada(lista):
    lista2 = lista
    if lista2 == lista.sort():
        return True
    else:
        return False


'''Escribir una función que reciba una tupla con n cantidad de nombres, y para cada nombre 
    imprima el mensaje Estimado,*inserte nombre aquí* vote por mí.'''

def vote(tupla):
    for nombre in tupla:
        print("Estimado, ", nombre, " vote por mi")

'''Escribir una función que indique si dos fichas de dominó encajan o no. 
    Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4). 
    Las fichas de domino encajan cuando ambas tienen un número igual. 
    Por ejemplo las de arriba si encajan pero (2,1) y (3,6) no encajan.'''

def domino(ficha1, ficha2):
    if ficha1[0] in ficha2 or ficha1[1] in ficha2:
        print("Si encajan")
    else:
        print("No encajan")


# Ejecución

lista_ord = [1,2,3,4,5]
lista_dord = [4,9,1,0,5]
ficha1 = (3,5)
ficha2 = (5,4)
ficha3 = (2,6)

print(sumaacum(lista_ord))
print(ordenada(lista_dord))
print(ordenada(["hola", "adios", "buenas tardes"]))
print(ordenada(lista_ord))
vote(("Hayde", "Marco", "Cristian", "Adriana"))
domino(ficha1, ficha2)
domino(ficha1, ficha3)