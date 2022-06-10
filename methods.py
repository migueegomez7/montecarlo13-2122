from operator import truediv
import dataStructures as ds
import random as r
import copy as c

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
    if(es_estado_final(estado, numero_movimientos)):
        if(ganan_blancas(estado,numero_movimientos)):
            print("\nGanan blancas")
        elif(ganan_negras(estado,numero_movimientos)):
            print("\nGanan negras")
        else:
            print("\nTablas")
    elif(estado[1]==2 and numero_movimientos>0):
        return print("\nJuegan blancas")
    elif(estado[1]==1 and numero_movimientos>0):
        return print("\nJuegan negras")
    print("Posibles movimientos: " + str(numero_movimientos))
    

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
    
   
  
              
    
       
            
