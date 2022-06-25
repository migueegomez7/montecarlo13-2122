from cmath import log, sqrt
from operator import truediv
import dataStructures as ds
import random as r
import copy as c
import time

def obtiene_estado_inicial(variante):
    match variante:
        case 1:
            return (ds.Hnefatafl,ds.BLACK_PLAYER)
        case 2:
            return (ds.Tablut, ds.BLACK_PLAYER)
        case 3:
            return (ds.Ard_Ri, ds.BLACK_PLAYER)
        case 4:
            return (ds.Brandubh, ds.BLACK_PLAYER)
        case 5:
            return (ds.Tawlbwrdd, ds.BLACK_PLAYER)
        case 6:
            return (ds.Alea_Evangelii, ds.BLACK_PLAYER)

def obtiene_movimientos(estado):
    lista_movimientos = []
    for i in range(len(estado[0])):
        for j in range(len(estado[0][i])):
            if(estado[0][i][j] == estado[1]):
                lista_movimientos.extend(obtiene_movimientos_desde_casilla(estado,(i,j)))
    r.shuffle(lista_movimientos)
    return lista_movimientos
                

## Recibe el estado actual del tablero y una casilla con una pieza del jugador con turno activo. Devuelve los movimientos disponibles a realizar.
def obtiene_movimientos_desde_casilla(estado,casilla):
    ##Y  LAS ESQUINAS QUÉ??!!!
    ##Y  LAS ESQUINAS QUÉ??!!!
    ##Y  LAS ESQUINAS QUÉ??!!!
    ##Y  LAS ESQUINAS QUÉ??!!!
    ##Casillas libres a la izq
    lista_movimientos = []
    fila = casilla[0]
    print(fila)
    columna = casilla[1]
    print(columna)
    for i in range (columna-1,-1,-1):
        if(estado[0][fila][i] == 0):
            lista_movimientos.append((fila,columna,fila,i))
        else:
            break
    ##Casillas libres a la dcha
    for i in range(columna+1,len(estado[0][0]),1):
        if(estado[0][fila][i] == 0):
            lista_movimientos.append((fila,columna,fila,i))
        else:
            break
    ##Casillas libes arriba
    for i in range(fila-1,-1,-1):
        if(estado[0][i][columna] == 0):
            lista_movimientos.append((fila,columna,i,columna))
        else:
            break
    ##Casillas libres abajo
    for i in range(fila+1,len(estado[0][0]),1):
        if(estado[0][i][columna] == 0):
            lista_movimientos.append((fila,columna,i,columna))
        else:
            break
    return lista_movimientos



def ganan_negras(estado,numero_movimientos):
    b = True
    if(estado[1] == 2 and numero_movimientos == 0):
        return b
    else:
        for i in estado[0]:
            for j in i:
                if(j == 3):
                    b = False
                    break
        return b

def ganan_blancas(estado,numero_movimientos):
    b = False
    if(estado[1] == 1 and numero_movimientos == 0):
        b = True
    elif(estado[0][0][0] == 3 
    or estado[0][0][len(estado[0][0])-1] == 3 
    or estado[0][len(estado[0][0])-1][0] == 3
    or estado[0][len(estado[0][0])-1][len(estado[0][0])-1] == 3):
        b = True

    return b

def es_estado_final(estado, numero_movimientos):
    b = False
    if(ganan_blancas(estado,numero_movimientos) or ganan_negras(estado,numero_movimientos)):
        b = True
    return b

#En algun lao habrá que checkear que el movimiento que entra aqui sea valido
def aplica_movimiento(estado,movimiento):
    estado_nuevo = c.copy(estado)
    estado_nuevo[0][movimiento[2]][movimiento[3]] = estado_nuevo[0][movimiento[0]][movimiento[1]]
    estado_nuevo[0][movimiento[0]][movimiento[1]] = 0
    elimina_piezas_capturadas(estado_nuevo,movimiento)
    aux = cambia_estado(estado_nuevo[1])
    estado_tupla_nueva = (estado_nuevo[0],aux)
    return estado_tupla_nueva


def elimina_piezas_capturadas(estado_nuevo,movimiento):
    i = movimiento[2]
    j = movimiento[3]
    last_index = len(estado_nuevo[0][0])-1
    estado_opuesto = cambia_estado(estado_nuevo[1])
    elimIzq = False
    elimArriba = False
    elimDcha = False
    elimAbajo = False
    #Izq
    if(j>0):
        if(estado_nuevo[0][i][j-1] == estado_opuesto):
            if((j-1 == 0 and i == 0) or (j-1 == 0 and i == last_index)): ##Comprueba si es una esquina
                elimIzq = True
            elif(j-2 >= 0 and estado_nuevo[0][i][j-2] == estado_nuevo[1]):
                elimIzq = True
    #Ariba
    if(i>0):
        if(estado_nuevo[0][i-1][j] == estado_opuesto):
            if((i-1 == 0 and j == 0) or (i-1 == 0 and j == last_index)):
                elimArriba = True
            elif(i-2 >= 0 and estado_nuevo[0][i-2][j] == estado_nuevo[1]):
                elimArriba = True
    #Dcha
    if(j<last_index):
        if(estado_nuevo[0][i][j+1] == estado_opuesto):
            if((j+1 == 0 and i == 0) or (j+1 == 0 and i == last_index)): ##Comprueba si es una esquina
                elimDcha = True
            elif(j+2 <= last_index and estado_nuevo[0][i][j+2] == estado_nuevo[1]):
                elimDcha = True
    #Abajo
    if(i<last_index):
        if(estado_nuevo[0][i+1][j] == estado_opuesto):
            if((i+1 == 0 and j == 0) or (i+1 == 0 and j == last_index)):
                elimAbajo = True
            elif(i+2 >= 0 and estado_nuevo[0][i+2][j] == estado_nuevo[1]):
                elimAbajo = True
    if(elimIzq == True):
        estado_nuevo[0][i][j-1] = 0
    if(elimArriba == True):
        estado_nuevo[0][i-1][j] = 0
    if(elimDcha == True):
        estado_nuevo[0][i][j+1] = 0
    if(elimAbajo == True):
        estado_nuevo[0][i+1][j] = 0
    return estado_nuevo

def cambia_estado(num):
    if(num == 1):
        return 2
    else:
        return 1
    
def imprime_estado(estado, numero_movimientos):
    entender_tablero(estado)
    print("\nPosibles movimientos: " + str(numero_movimientos))
    if(es_estado_final(estado, numero_movimientos)):
        if(ganan_blancas(estado,numero_movimientos)):
            print("Ganan blancas")
        elif(ganan_negras(estado,numero_movimientos)):
            print("Ganan negras")
        else:
            print("Tablas")
    elif(estado[1]==2 and numero_movimientos>0):
        return print("Juegan blancas")
    elif(estado[1]==1 and numero_movimientos>0):
        return print("Juegan negras")
    

def entender_tablero(estado):
    a=len(estado[0])
    b=len(estado[0][0])
    print("     ", end="")
    for i in range(1,(b+1)):
        if (i<9):
            print(str(i), end="  ")
        else:
            print(str(i), end=" ")
           
        
        
    print("")
    print("   ", end="")
    
    # for i in range(1,(b+1)):
    #     if(i<=9):
    #         print("---", end="")
    #     else:
    #         print("--", end="")
    
    print("")
    

    
    for e in range(0,(a)):
        c=estado[0][e]
        if (e<9):
            print(str(e+1), end="    ")
        else:
            print(str(e+1), end="   ")
            
        print(*c, sep="  ")
    




   
def busca_solucion(estado,tiempo):
    v0 = crea_nodo(estado,None)
    timeout = time.time() + tiempo
    while time.time() < timeout: #Mientras que el tiempo actual sea menor que el tiempo dentro de +tiempo segundos
        v1 = tree_policy(v0)
        delta = default_policy(v1)
        backup(v1,delta)
    return v0.movimientos[best_child(v0,0)]

def crea_nodo(estado,padre):
    v = ds.nodo()
    v.estado = estado
    v.movimientos = obtiene_movimientos(estado)
    v.n = 0
    v.q = 0
    v.i = 0
    v.hijos = []
    v.padre = padre
    return v

def tree_policy(nodo):
    while not es_estado_final(nodo.estado,nodo.movimientos):
        if(nodo.i < len(nodo.movimientos)):
            return expand(nodo)
        else:
            nodo = nodo.hijos[best_child(nodo, 1/sqrt(2))]
    

def expand(nodo):
    estado = aplica_movimiento(nodo.estado, nodo.movimientos[nodo.i])
    nodo.i = nodo.i +1
    hijo = crea_nodo(estado, nodo)
    nodo.hijos.append(hijo)
    return hijo


def best_child(nodo,c):
    nodo_aux = ds.nodo()
    for i in range(0,len(nodo.hijos)):
        nodo_value = (nodo.hijos[i].q / nodo.hijos[i].n) + c * sqrt(2*log(nodo.n,10)/nodo.hijos[i].n)
        nodo_aux_value = (nodo_aux.hijos[i].q / nodo_aux.hijos[i].n) + c * sqrt(2*log(nodo_aux.n,10)/nodo_aux.hijos[i].n)
        if(nodo_value > nodo_aux_value):
            nodo_aux = nodo
    return nodo_aux

def default_policy(nodo):
    estado = nodo.estado
    movs = nodo.movimientos
    jugador = nodo.padre.estado[1]
    while not es_estado_final(estado,movs):
        a = r.randint(0,len(movs)-1)
        estado = aplica_movimiento(estado, movs[a])
    if(ganan_blancas(estado,movs) and jugador == 2):
        return 1
    elif(ganan_negras(estado,movs) and jugador == 1):
        return 1
    else:
        return -1
    
def backup(nodo,delta):
    while nodo != None:
        nodo.n = nodo.n+1
        nodo.q = nodo.q + delta
        delta = -delta
        nodo = nodo.padre


