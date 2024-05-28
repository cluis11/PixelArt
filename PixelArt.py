from tkinter import *

class editor:
    def __init__(self):
        self.matriz = [
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    ]
        self.creador = ""
        self.estado = "Creado"
        self.color = 9
        self.color_fill = "black"
        self.SIZE = 20
        self.x = 0
        self.y = 0
        self.cont = 1
        self.cuadros_cambiados = set()
        
        self.window = Tk()
        self.pantalla = Canvas(self.window,width=800, height=600)
        self.lienzo = Canvas(self.pantalla,width=430, height=430)


    def get_creador(self):
        return self.creador
    
    def get_color(self):
        return self.color
    
    def get_colorfill(self):
        return self.color_fill
    
    def get_estado(self):
        return self.estado
    
    def set_creador(self, creador):
        self.creador = creador
    
    def set_color(self, color):
        self.color = color
        
    def set_colorfill(self, color):
        self.color_fill = color
        
    def set_estado(self, estado):
        self.estado = estado
        
    def set_matriz(self, i, j):
        self.matriz[i][j] = self.get_color()
        
    def actualiza_lienzo(self):
        cont = 1
        for fila in self.matriz:
            for j in fila:
                self.actualiza_color(j)
                self.lienzo.itemconfig(f"pixel{cont}", fill = self.get_colorfill())
                cont += 1
        self.actualiza_color(self.get_color())

    def mostrar_interfaz(self):
        for fila in self.matriz:
            for columna in fila:
                self.lienzo.create_rectangle(self.x, self.y, self.x + self.SIZE, self.y + self.SIZE, fill = "white", tag = f"pixel{self.cont}")
                self.cont+=1
                self.x += self.SIZE + 1
            self.x = 0
            self.y+= self.SIZE + 1
            
        self.pantalla.create_oval(620, 100, 620+50, 100+50, fill="white", tag="color")
        self.pantalla.create_oval(680, 100, 680+50, 100+50, fill="black", tag="color")
        self.pantalla.create_oval(620, 160, 620+50, 160+50, fill="pink", tag="color")
        self.pantalla.create_oval(680, 160, 680+50, 160+50, fill="brown", tag="color")
        self.pantalla.create_oval(620, 220, 620+50, 220+50, fill="blue", tag="color")
        self.pantalla.create_oval(680, 220, 680+50, 220+50, fill="orange", tag="color")
        self.pantalla.create_oval(620, 280, 620+50, 280+50, fill="purple", tag="color")
        self.pantalla.create_oval(680, 280, 680+50, 280+50, fill="yellow", tag="color")
        self.pantalla.create_oval(620, 340, 620+50, 340+50, fill="red", tag="color")
        self.pantalla.create_oval(680, 340, 680+50, 340+50, fill="green", tag="color")
        
        self.pantalla.tag_bind("color", "<Button-1>", self.asignar_color)

        self.pantalla.pack()
        self.lienzo.place(x=400,y=300, anchor="center")
        self.lienzo.bind("<Button-1>", self.on_canvas_click)
        self.lienzo.bind("<B1-Motion>", self.on_canvas_motion)
        
        self.window.mainloop()
        
    def asignar_color(self, event):
        color_id = event.widget.find_withtag(CURRENT)[0]
        fill_color = event.widget.itemcget(color_id, "fill")
        if fill_color == "black":
            self.set_color(9)
            self.set_colorfill(fill_color)
        elif fill_color == "purple":
            self.set_color(7)
            self.set_colorfill(fill_color)
        elif fill_color == "brown":
            self.set_color(8)
            self.set_colorfill(fill_color)
        elif fill_color == "orange":
            self.set_color(3)
            self.set_colorfill(fill_color)
        elif fill_color == "yellow":
            self.set_color(2)
            self.set_colorfill(fill_color)
        elif fill_color == "green":
            self.set_color(4)
            self.set_colorfill(fill_color)
        elif fill_color == "red":
            self.set_color(5)
            self.set_colorfill(fill_color)
        elif fill_color == "blue":
            self.set_color(6)
            self.set_colorfill(fill_color)
        elif fill_color == "pink":
            self.set_color(1)
            self.set_colorfill(fill_color)
        elif fill_color == "white":
            self.set_color(0)
            self.set_colorfill(fill_color)
            
    def actualiza_color(self, num):
        if num == 0:
            self.set_colorfill("white")
        elif num == 1:
            self.set_colorfill("pink")
        elif num == 2:
            self.set_colorfill("yellow")
        elif num == 3:
            self.set_colorfill("orange")
        elif num == 4:
            self.set_colorfill("green")
        elif num == 5:
            self.set_colorfill("red")
        elif num == 6:
            self.set_colorfill("blue")
        elif num == 7:
            self.set_colorfill("purple")
        elif num == 8:
            self.set_colorfill("brown")
        elif num == 9:
            self.set_colorfill("black")
        
    def on_canvas_click(self,event):
        self.cuadros_cambiados.clear()
        x, y = event.x, event.y
        cuadro = self.lienzo.find_overlapping(x, y, x, y)
        if cuadro not in self.cuadros_cambiados:
            self.lienzo.itemconfig(cuadro, fill=self.get_colorfill())
            self.cuadros_cambiados.add(cuadro)
            j = x // (self.SIZE + 1)
            i = y // (self.SIZE + 1)
            print("\n")
            print(x, y)
            print (j, i)
            self.set_matriz(i,j)            

    def on_canvas_motion(self,event):
        x, y = event.x, event.y
        cuadro = self.lienzo.find_overlapping(x, y, x, y)
        for item in cuadro:
            if item not in self.cuadros_cambiados:
                self.lienzo.itemconfig(item, fill=self.get_colorfill())
                self.cuadros_cambiados.add(item)
                j = x // (self.SIZE + 1)
                i = y // (self.SIZE + 1)
                print("\n")
                print(x, y)
                print (j, i)
                self.matriz[i][j] = self.get_color()


objeto = editor()
objeto.mostrar_interfaz()