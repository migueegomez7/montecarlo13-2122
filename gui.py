import tkinter as tk
import dataStructures as ds

LADO_TABLERO = 8

class App():
    def __init__(self, L_CUADRADO):
        self.L_CUADRADO = L_CUADRADO
        self.imagenes = {}

        self.ventana = tk.Tk()
        self.ventana.title("Motor de ajedrez vikingo")
        self.ventana.iconbitmap("imagenes/logo.ico")
        self.ventana.geometry(f"{str(L_CUADRADO*LADO_TABLERO)}x{str(L_CUADRADO*LADO_TABLERO)}")
        self.ventana.resizable(0,0) #Esto hace que no se puede resizear

        self.interfaz  = tk.Canvas(self.ventana)
        self.interfaz.pack(fill = "both",expand=True)


    def __call__(self):
        self.ventana.mainloop()

    def dibujar_tablero(self,lado_tablero):
        global LADO_TABLERO
        LADO_TABLERO = lado_tablero
        self.ventana.geometry(f"{str(self.L_CUADRADO*LADO_TABLERO)}x{str(self.L_CUADRADO*LADO_TABLERO)}")
        for i in range(lado_tablero):
            for j in range(lado_tablero):
                self.interfaz.create_rectangle(i*self.L_CUADRADO,j*self.L_CUADRADO,(i+1)*self.L_CUADRADO,(j+1)*self.L_CUADRADO,fill="#ffdd99")

    def cargar_imagenes(self):
        piezas = ["bp","wp","wking"]
        for pieza in piezas:
            self.imagenes[pieza] = tk.PhotoImage(file="./imagenes/" + pieza + ".png").subsample(11)
            

    def mostrar_piezas(self):
        for indice_i, i in enumerate(ds.gui_boards(ds.Hnefatafl)):
            for indice_j,j in enumerate(i):
                if j != 0:
                    self.interfaz.create_image(indice_j*self.L_CUADRADO,indice_i*self.L_CUADRADO,image=self.imagenes[j], anchor="nw")

MotorDeAjedrezVikingo = App(70)
MotorDeAjedrezVikingo.dibujar_tablero(len(ds.Hnefatafl[0]))
MotorDeAjedrezVikingo.cargar_imagenes()
MotorDeAjedrezVikingo.mostrar_piezas()
MotorDeAjedrezVikingo()