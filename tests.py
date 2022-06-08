import dataStructures as ds
import methods as m


tupla = m.obtiene_estado_inicial(3)
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