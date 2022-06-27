from xml.etree.ElementTree import TreeBuilder
import dataStructures as ds
from methods import aplica_movimiento, busca_solucion, es_estado_final, ganan_blancas, imprime_estado, obtiene_estado_inicial, obtiene_movimientos

def main():
    # lista = [[0,0,0,1,1,1,1,1,0,0,0],
    #         [0,0,1,0,0,0,0,0,0,0,0],
    #         [0,1,3,1,0,0,0,0,0,0,0],
    #         [1,2,0,0,0,0,0,0,0,0,1],
    #         [1,0,0,0,0,0,2,0,0,0,1],
    #         [1,0,1,2,1,0,1,2,0,1,1], ##Línea del medio
    #         [1,0,0,0,2,0,2,0,0,0,1],
    #         [1,0,0,0,0,2,0,0,0,0,1],
    #         [0,0,0,0,0,0,0,0,0,0,0],
    #         [0,0,0,0,0,1,0,0,0,0,0],
    #         [0,0,0,1,1,1,1,1,0,0,0]]
    # tupla = (lista,1)

    # lista2 = [[0,3,0,1,1,1,1,1,0,0,0],
    #          [0,0,1,0,0,0,0,0,0,0,0],
    #          [0,1,0,1,0,0,0,0,0,0,0],
    #          [1,2,0,0,0,0,0,0,0,0,1],
    #          [1,0,0,0,0,0,2,0,0,0,1],
    #          [1,0,1,2,1,0,1,2,0,1,1], ##Línea del medio
    #          [1,0,0,0,2,0,2,0,0,0,1],
    #          [1,0,0,0,0,2,0,0,0,0,1],
    #          [0,0,0,0,0,0,0,0,0,0,0],
    #          [0,0,0,0,0,1,0,0,0,0,0],
    #          [0,0,0,1,1,1,1,1,0,0,0]]
    # tupla2 = (lista2,1)
    tiempo = 0
    variante = choose_board()
    estado_inicial = obtiene_estado_inicial(variante)
    chosen_side = choose_side()
    num_movs_estado_inicial = len(obtiene_movimientos(estado_inicial))
    play_human = choose_oponent()
    if not play_human:
        tiempo = int(input("Elija el tiempo que tendra la IA para pensar las jugadas."))
    imprime_estado(estado_inicial,num_movs_estado_inicial)
    start_game(estado_inicial,num_movs_estado_inicial,chosen_side,play_human,tiempo)
    


def choose_board():
    choose = True
    print("Escribe el numero del tablero en el que deseas jugar:")
    print("1. Hnefatafl\n2. Tablut\n3. Ard_Ri\n4. Brandubh\n5. Tawlbwrdd\n6. Alea_Evangelii")
    while choose:
        bType = int(input("En qué tablero quiere jugar?"))
        if(bType >= 1 and bType <= 6):
            print("Ha seleccionado el tablero " + str(bType) + ".\n")
            break
        print("El numero que ha introducido no se corresponde con ningún tablero. Por favor introduzca un numero entre el 1 y el 6.")    
    return bType

def choose_side():
    choose = True
    while choose:
        side = int(input("Elija con qué piezas quiere jugar:\n1. Negras\n2. Blancas"))
        if(side == 1):
            print("Ha seleccionado las piezas negras.\n")
            break
        elif(side == 2):
            print("Ha seleccionado las piezas negras.\n")
            break
        print("Escriba un número entre 1 o 2 para seleccionar las piezas negras o blancas respectivamente.")
    return side

def choose_oponent():
    choose = True
    while choose:
        human = int(input("Elija si quiere jugar contra otra persona o contra la IA:\n1. Persona\n2. IA"))
        if(human == 1):
            print("Ha decidido jugar contra un humano.\n")
            return True
        elif(human == 2):
            print("Ha decidido jugar contra la IA.\n")
            return False
        print("Escriba 1 o 2")


def start_game(estado,num_movs,chosen_side,play_human,tiempo):
    aux = estado
    if play_human:
        while not es_estado_final(aux,num_movs):
            estado_nuevo = player_turn(aux,1)
            if(not es_estado_final(estado_nuevo,len(obtiene_movimientos(estado_nuevo)))):
                aux = player_turn(estado_nuevo,2)
                if(es_estado_final(aux,len(obtiene_movimientos(aux)))):
                    imprime_estado(aux,len(obtiene_movimientos(aux)))
                    print("\n----------------------------------\n|                                |\n|Gracias. La partida ha terminado|\n|                                |\n----------------------------------")
                    break
            else:
                imprime_estado(estado_nuevo,len(obtiene_movimientos(estado_nuevo)))
                print("\n----------------------------------\n|                                |\n|Gracias. La partida ha terminado|\n|                                |\n----------------------------------")
                break
    elif(chosen_side == 1):
        while(not es_estado_final(aux,num_movs)):
            estado_nuevo = player_turn(aux,1)
            if(not es_estado_final(estado_nuevo,len(obtiene_movimientos(estado_nuevo)))):
                aux = machine_turn(estado_nuevo,2,tiempo)
            else:
                imprime_estado(estado_nuevo,len(obtiene_movimientos(estado_nuevo)))
                print("\n----------------------------------\n|                                |\n|Gracias. La partida ha terminado|\n|                                |\n----------------------------------")
                break
    elif(chosen_side == 2):
        while(not es_estado_final(aux,num_movs)):
            estado_nuevo = machine_turn(aux,1,tiempo)
            if(not es_estado_final(estado_nuevo,len(obtiene_movimientos(estado_nuevo)))):
                aux = player_turn(estado_nuevo,2)
            else:
                imprime_estado(estado_nuevo,len(obtiene_movimientos(estado_nuevo)))
                print("\n----------------------------------\n|                                |\n|Gracias. La partida ha terminado!|\n|                                |\n----------------------------------")
                break

def player_turn(estado,color):
    print("-----------------------------------------\n")
    imprime_estado(estado,len(obtiene_movimientos(estado)))
    print("\n---------------------------------------------------")
    choose = True
    while choose:
        movimiento = str(input("Introduzca el movimiento que quiere hacer:\nFormato: (x from, y from, x to, y to). IMPORTANTE LOS ESPACIOS!"))
        for cad in obtiene_movimientos(estado):
            if str(cad) == movimiento:
                return aplica_movimiento(estado,cad)
        print("El movimiento introducido no es posible\n.")


def machine_turn(estado,color,tiempo):
    print("-----------------------------------------\n")
    imprime_estado(estado,len(obtiene_movimientos(estado)))
    print("\n---------------------------------------------------")
    movimiento = busca_solucion(estado,tiempo)
    return aplica_movimiento(estado,movimiento)

main()