from operator import truediv
import dataStructures as ds
import random as r

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