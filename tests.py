from copy import copy
import dataStructures as ds
import methods as m


tupla = m.obtiene_estado_inicial(1)
def print_estado_inicial(tupla):
    for i in range(len(tupla[0])):
        print(tupla[0][i])
    print(tupla[1])


print("---------------Estado inicial------------------")
print_estado_inicial(tupla)

print("----------------Movimientos desde estado inicial--------------------")
print(m.obtiene_movimientos(tupla))

print("--------------Negras han ganado-----------------")
#tupla[0][3][3] = 0
print(m.ganan_negras(tupla,0))

print("--------------Blancas han ganado-----------------")
#tupla[0][0][0] = 3
print(m.ganan_blancas(tupla,0))

print("--------------Es estado Final-----------------")
#tupla[0][0][0] = 3
print(m.es_estado_final(tupla,0))

print("---------------Aplica movimiento-----------------")
tupla[0][4][3] = 1
tupla[0][0][3] = 0
tupla_nueva = (tupla[0],2)
print(m.aplica_movimiento(tupla_nueva,(3,5,3,3)))

print("------------Aplica movimiento elimina 2 piezas------------------")
lista = [   [0,0,0,1,1,1,1,1,0,0,0],
            [0,0,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [1,2,0,0,0,0,0,0,0,0,1],
            [1,0,2,0,0,2,2,0,0,0,1],
            [1,0,1,2,2,3,2,2,0,1,1], ##Línea del medio
            [1,0,0,0,2,2,2,0,0,0,1],
            [1,0,0,0,0,2,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,1,1,1,1,1,0,0,0]]

tp_ls = (lista,1)
print(m.aplica_movimiento(tp_ls,(1,2,3,2)))

print("---------------------Imprime estado-----------------------")
m.imprime_estado(tupla,0)
print("---------------------Entender Tablero-----------------------")
m.entender_tablero(tupla)