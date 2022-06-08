from dataStructures import game

def startGame():

    ##Aqui iria el input pa que el usuario seleccione el tipo de board
    bType = str(input("En qué tablero quiere jugar?"))
    selectBoard(g,bType)
    



def selectBoard(game,boardType):
    match boardType:
        case 'Hnefatafl':
            game.board = ((0,0,0,1,1,1,1,1,0,0,0),
                 (0,0,0,0,0,1,0,0,0,0,0),
                 (0,0,0,0,0,0,0,0,0,0,0),
                 (1,0,0,0,0,2,0,0,0,0,1),
                 (1,0,0,0,2,2,2,0,0,0,1),
                 (1,1,0,2,2,3,2,2,0,1,1), ##Línea del medio
                 (1,0,0,0,2,2,2,0,0,0,1),
                 (1,0,0,0,0,2,0,0,0,0,1),
                 (0,0,0,0,0,0,0,0,0,0,0),
                 (0,0,0,0,0,1,0,0,0,0,0),
                 (0,0,0,1,1,1,1,1,0,0,0))
            print("Hnefatafl")
        case 'Tablut':
            game.boardType = ((0,0,0,1,1,1,0,0,0),
              (0,0,0,0,1,0,0,0,0),
              (0,0,0,0,2,0,0,0,0),
              (1,0,0,0,2,0,0,0,1),
              (1,1,2,2,3,2,2,1,1), ##Línea del medio
              (1,0,0,0,2,0,0,0,1),
              (0,0,0,0,2,0,0,0,0),
              (0,0,0,0,1,0,0,0,0),
              (0,0,0,1,1,1,0,0,0))
            print("Tablut")
        case _:
            print("a")

startGame()