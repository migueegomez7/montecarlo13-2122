from xml.etree.ElementTree import TreeBuilder
import dataStructures as ds
from methods import es_estado_final, ganan_blancas, imprime_estado, obtiene_estado_inicial, obtiene_movimientos

def main():
    variante = choose_board()
    estado_inicial = obtiene_estado_inicial(variante)
    chosen_side = choose_side()
    num_movs_estado_inicial = len(obtiene_movimientos(estado_inicial))
    imprime_estado(estado_inicial,num_movs_estado_inicial)
    start_game(estado_inicial)
    


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
def start_game(estado,num_movs,chosen_side,play_human):
    while(not es_estado_final(estado,num_movs)):
        if(chosen_side == 1):
            player_turn(chosen_side)
            machine_turn(chosen_side)
        if(chosen_side == 2):
            machine_turn(chosen_side)
            player_turn(chosen_side)
main()