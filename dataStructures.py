from copy import copy
from enum import Enum
import methods as meth


BLACK_PLAYER = 1
WHITE_PLAYER = 2
##Lsta de listas mejo porque son mutables
Hnefatafl = [[0,0,0,1,1,1,1,1,0,0,0],
                 [0,0,0,0,0,1,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [1,0,0,0,0,2,0,0,0,0,1],
                 [1,0,0,0,2,2,2,0,0,0,1],
                 [1,1,0,2,2,3,2,2,0,1,1], ##Línea del medio
                 [1,0,0,0,2,2,2,0,0,0,1],
                 [1,0,0,0,0,2,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,1,0,0,0,0,0],
                 [0,0,0,1,1,1,1,1,0,0,0]]

Tablut = [[0,0,0,1,1,1,0,0,0],
              [0,0,0,0,1,0,0,0,0],
              [0,0,0,0,2,0,0,0,0],
              [1,0,0,0,2,0,0,0,1],
              [1,1,2,2,3,2,2,1,1], ##Línea del medio
              [1,0,0,0,2,0,0,0,1],
              [0,0,0,0,2,0,0,0,0],
              [0,0,0,0,1,0,0,0,0],
              [0,0,0,1,1,1,0,0,0]]

Ard_Ri = [[0,0,1,1,1,0,0],
              [0,0,0,1,0,0,0],
              [1,0,2,2,2,0,1],
              [1,1,2,3,2,1,1], ##Linea del medio
              [1,0,2,2,2,0,1],
              [0,0,0,1,0,0,0],
              [0,0,1,1,1,0,0]]

Brandubh = [[0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,2,0,0,0],
                [1,1,2,3,2,1,1], ##Linea del medio
                [0,0,0,2,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0]]

Tawlbwrdd = [[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 2, 2, 2, 0, 0, 1, 1],
                [1, 0, 1, 2, 2, 3, 2, 2, 1, 0, 1], ##Linea del medio
                [1, 1, 0, 0, 2, 2, 2, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]]

Alea_Evangelii = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0], ##Línea del medio
                      [0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                      [0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]]


def gui_boards(board):
    board_cp = copy(board)
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if(board[i][j] == 1):
                board_cp[i][j] = "bp"
            elif(board[i][j] == 2):
                board_cp[i][j] = "wp"
            elif(board[i][j] == 3):
                board_cp[i][j] = "wking"
    return board_cp

class nodo:

    def __init__(self):
        self.estado = None
        self.movimientos = []
        self.n = 0
        self.q = 0
        self.i = 0
        self.hijos = []
        self.padre = None
            