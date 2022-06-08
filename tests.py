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