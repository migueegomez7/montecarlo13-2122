import dataStructures as ds

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




 ##Función que recibe un estado y devuelve una lista
 ##   con todos los posibles movimientos del jugador activo. Esta lista deberá devolverse
  ## ”barajada” tras aplicar la función random.shuffle.