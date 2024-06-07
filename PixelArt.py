
from tkinter import *
from tkinter import filedialog
import json
from tkinter import messagebox

class editor:
    #Funcion para inicializar los objetos, todos los atributos se asignan manualmente
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
        self.creador = "" #Dueño de la imagen
        self.estado = "Creado" #Creado, Terminado, En Proceso
        self.color = 9 #valor que indica que se va a guardar en la matriz
        self.color_fill = "black" #Valor para poder pintar el rectangulo
        self.SIZE = 20 #Tamaño de los rectangulos
        self.x = 0 #coordenada x para dibujar en lienzo
        self.y = 0 #coordenada x para dibujar en lienzo
        self.cont = 1 #contador para asignar tag a los elementos del canvas
        self.cuadros_cambiados = set() #lista que almacena los cuadros que se han pintado al arrastrar el mouse
        #atributos de interfaz
        self.window = Tk() 
        self.pantalla = Canvas(self.window,width=800, height=600) #pantalla principal de la aplicacion
        self.lienzo = Canvas(self.pantalla,width=430, height=430) #lienzo donde se dibuja
        self.lienzo.start_x = None #posicion de inicio cuando se da click
        self.lienzo.start_y = None #posicion de fin cuando se da click
        self.lienzo.end_x = None #posicion de inicio cuando se suelta el click
        self.lienzo.end_y = None #posicion de fin cuando se suelta el click
        self.lienzo.zoom = None #
        self.isZoom = False #bandera para determinar si el editor esta en modo zoom
        self.isNum = False #bandera para determinar si el editor esta en modo mostrar numeros de la matriz
        self.isFill = False #
        self.color_to_paint = None #
        self.isCircle = None #bandera para determinar si la opcion del circulo esta seleccionada
        self.radius = None #radio del circulo
        self.isSquare = None 
        self.matriz_zoomed = None #Matriz del area seleccionada para el zoom
        self.zoomed_SIZEx = None #
        self.zoomed_SIZEy = None #
        self.isAscii = False #bandera para determinar si el editor esta en modo mostrar ascii
        self.islock = False
        self.estados = ["Creado","En Proceso","Completado"]
        self.pantalla.creadortxt = NONE
        self.pantalla.estadoimg = NONE
        self.pantalla.variable = NONE
        
#Funciones get de la clase
    def get_creador(self):
        return self.creador
    
    def get_color(self):
        return self.color
    
    def get_colorfill(self):
        return self.color_fill
    
    def get_estado(self):
        return self.estado
    
    def get_matriz(self):
        return self.matriz
    
    def get_cont(self):
        return self.cont
    
    def get_isNum(self):
        return self.isNum
    
    def get_isZoom(self):
        return self.isZoom
    
    def get_isFill(self):
        return self.isFill
    
    def get_color_to_paint(self):
        return self.color_to_paint

    def get_isCircle(self):
        return self.isCircle
    
    def get_radius(self):
        return self.radius
    
    def get_isSquare(self):
        return self.isSquare

    def get_matriz_zoomed(self):
        return self.matriz_zoomed
    
    def get_estados(self):
        return self.estados
    
#Funciones set de la clase
    def set_creador(self, creador):
        self.creador = creador
    
    def set_color(self, color):
        self.color = color
        
    def set_colorfill(self, color):
        self.color_fill = color
        
    def set_estado(self, estado):
        self.estado = estado
        
    def set_matriz(self, matriz):
        self.matriz = matriz
        
    def set_matriz_pos(self, i, j):
        self.matriz[i][j] = self.get_color()
        
    def set_cont(self, cont):
        self.cont = cont
        
    def set_isZoom(self):
        if self.isZoom():
            self.isZoom = False
        else:
            self.isZoom = True
    
    def set_isFill(self):
        if self.isFill:
            self.isFill = False
        else:
            self.isFill = True
    
    def set_isCircle(self):
        if self.isCircle:
            self.isCircle = False
        else:
            self.isCircle = True
    
    def set_isSquare(self):
        if self.isSquare:
            self.isSquare = False
        else:
            self.isSquare = True

    def set_isNum(self):
        if self.isNum():
            self.isNum = False
        else:
            self.isNum = True
      
    #Funcion que actualiza los colores de los cuadros en lienzo a los valores mas recientes de la matriz  
    def actualiza_lienzo(self):
        cont = 1
        for fila in self.matriz:
            for j in fila:
                self.actualiza_color(j)
                self.lienzo.itemconfig(f"pixel{cont}", fill = self.get_colorfill())
                cont += 1
        self.actualiza_color(self.get_color())
    
    #
    def reflejo_horizontal(self):
        nueva_matriz = []
        n = len(self.matriz[0])-1 #Tamaño de matriz (n+1)x(n+1)
        for fila in range (n+1):
            nueva_matriz.append([]) #Crea n filas de la nueva matriz
        
        for columna in range(n+1): #repite el ciclo por cada fila
            fila = 0
            original = n #fila original
            for i in range (n+1): 
                nueva_matriz[fila].append(self.matriz[original][columna])
                original = original - 1
                fila = fila + 1
        self.matriz = nueva_matriz
        self.actualiza_lienzo()
     
     #   
    def reflejo_vertical(self):
        nueva_matriz = []
        n = len(self.matriz[0]) - 1  # Tamaño de matriz (n+1)x(n+1)
        for fila in range(n + 1):  # Crea (n+1) filas de la nueva matriz
            nueva_matriz.append([])
        for fila in range(n + 1):  # repite el ciclo por cada fila
            original = n
            for _ in range(n + 1):
                nueva_matriz[fila].append(self.matriz[fila][original])
                original -= 1
        self.matriz = nueva_matriz
        self.actualiza_lienzo()
    
    #
    def rotar_derecha(self):
        nueva_matriz = []
        n = len(self.matriz[0])-1 #Tamaño de matriz (n+1)x(n+1)
        for fila in range (n+1):
            nueva_matriz.append([]) #Crea n filas de la nueva matriz
        for fila in nueva_matriz:
            for columna in range (n+1):
                fila.append('')
        columna_nueva_matriz = n
        for fila in self.matriz:
            fila_nueva_matriz = 0
            for elemento in fila:
                nueva_matriz[fila_nueva_matriz][columna_nueva_matriz] = elemento
                fila_nueva_matriz += 1
            columna_nueva_matriz -= 1
        self.matriz = nueva_matriz
        self.actualiza_lienzo()
    
    #
    def rotar_izquierda(self):
        nueva_matriz = []
        n = len(self.matriz[0])-1 #Tamaño de matriz (n+1)x(n+1)
        for fila in range (n+1):
            nueva_matriz.append([]) #Crea n filas de la nueva matriz
        for fila in nueva_matriz:
            for columna in range (n+1):
                fila.append('')
        columna_nueva_matriz = 0
        for fila in self.matriz:
            fila_nueva_matriz = n
            for elemento in fila:
                nueva_matriz[fila_nueva_matriz][columna_nueva_matriz] = elemento
                fila_nueva_matriz -= 1
            columna_nueva_matriz += 1
        self.matriz = nueva_matriz
        self.actualiza_lienzo()

    #Funcion que convierte todos los valores de la matriz en 0 y actualiza el lienzo
    def clear_matriz(self):
        cleared_matriz = []
        n = (len(self.matriz))
        for i in range (n):
            cleared_matriz.append([])
            for j in range(n):
                cleared_matriz[i].append(0)
        self.matriz = cleared_matriz
        self.actualiza_lienzo()
        
    #Funcion que invierte los valores de la matriz y actualiza el lienzo
    def negativo(self):
        valores_negativos = [9,8,7,6,5,4,3,2,1,0]
        n = (len(self.matriz))
        for i in range (n):
            for j in range(n):
                self.matriz[i][j] = valores_negativos[self.matriz[i][j]]
        self.actualiza_lienzo()  
    
    #
    def alto_contraste(self):
        nueva_matriz = self.matriz
        index_fila = 0
        for fila in self.matriz:
            index_columna = 0
            for elemento in fila:
                if elemento <= 4:
                    nueva_matriz [index_fila][index_columna] = 0
                else: 
                    nueva_matriz[index_fila][index_columna] = 9
                index_columna += 1
            index_fila += 1
        self.matriz = nueva_matriz
        self.actualiza_lienzo()
   
   #Funcion que se encarga de dibujar el lienzo en la interzas
    def dibujar_lienzo(self,matriz):
        for fila in matriz:
            for columna in fila:
                self.lienzo.create_rectangle(self.x, self.y, self.x + self.SIZE, self.y + self.SIZE, fill = "white", tag = f"pixel{self.cont}")
                self.lienzo.create_text(self.x + (self.SIZE/2), self.y + (self.SIZE/2), text="", fill="black", anchor="center", tag= f"cuadro{self.cont}")
                self.cont+=1
                self.x += self.SIZE + 1
            self.x = 0
            self.y+= self.SIZE + 1

    #Funcion que se encarga de crear la interfaz con todos sus elementos
    def mostrar_interfaz(self):
        self.dibujar_lienzo(self.get_matriz()) #Dibuja el lienzo
        #Dibuja los colores 
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
        
        self.pantalla.tag_bind("color", "<Button-1>", self.asignar_color) #permite cambiar de color al precionarlos

        self.pantalla.pack()
        self.lienzo.place(x=400,y=300, anchor="center")
        #Bindings para dibujar
        self.lienzo.bind("<Button-1>", self.on_canvas_click)
        self.lienzo.bind("<B1-Motion>", self.on_canvas_motion)
        
        #estado y creador
        options = self.get_estados()
        self.pantalla.variable = StringVar(self.pantalla)
        self.pantalla.variable.set(options[0])  
        self.pantalla.estadoimg = OptionMenu(self.pantalla, self.pantalla.variable, *options)
        self.pantalla.estadoimg.place(x=350, y=35)
        self.pantalla.create_text(310, 55, text="Estado", font = ("Stencil", 12))
        
        self.pantalla.create_text(310, 20, text="Creador", font = ("Stencil", 12))
        self.pantalla.creadortxt = Entry(self.pantalla, width=25)
        self.pantalla.creadortxt.place(x=350, y = 10)

        #Botones para interactuar con la matriz y lienzo
        self.vertical = Button(self.pantalla, width = 15, height = 1, text = 'Reflex Vertical', command = self.reflejo_vertical, relief="ridge", font = "Stencil",activebackground="lightgray")
        self.vertical.place(x=5, y=100)

        self.horizontal = Button(self.pantalla, width = 15, height = 1, text = 'Reflex Horizontal', command = self.reflejo_horizontal, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.horizontal.place(x=5, y=175)

        self.derecha = Button(self.pantalla, width = 15, height = 1, text = 'Rotate Right', command = self.rotar_derecha, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.derecha.place(x=5, y=250)

        self.izquierda = Button(self.pantalla, width = 15, height = 1, text = 'Rotate Left', command = self.rotar_izquierda, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.izquierda.place(x=5, y=325)

        self.clear_all = Button(self.pantalla, width = 15, height = 1, text = 'Clear All', command = self.clear_matriz, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.clear_all.place(x=5, y=400)

        self.contraste = Button(self.pantalla, width = 15, height = 1, text = 'High Contrast', command = self.alto_contraste, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.contraste.place(x=5, y=525)

        self.rellenar = Button(self.pantalla, width = 10, height = 1, text = 'Fill', command = self.Fill, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.rellenar.place(x=620, y=425)

        self.circulo = Button(self.pantalla, width = 10, height = 1, text = 'Circle', command = self.circle, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.circulo.place(x=620, y=475)

        self.cuadrado = Button(self.pantalla, width = 10, height = 1, text = 'Square', command = self.square, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.cuadrado.place(x=620, y=525)
        
        self.negate = Button(self.pantalla, width = 15, height = 1, text = 'Negativo', command = self.negativo, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.negate.place(x=5, y=460)
        
        self.abrir_img = Button(self.pantalla, width = 7, height = 1, text = 'Abrir', command = self.abrir_json, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.abrir_img.place(x=620, y=15)
        
        self.guardar_img = Button(self.pantalla, width = 7, height = 1, text = 'Guardar', command = self.guardar_json, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.guardar_img.place(x=710, y=15)
        
        self.zoom_button = Button(self.pantalla, width = 10, height = 1, text = 'Zoom In', command = self.zoom, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.zoom_button.place(x=30, y=15)
        
        self.muestra_num = Button(self.pantalla, width = 15, height = 1, text = 'Mostrar Num', command = self.mostrar_matriz_num, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.muestra_num.place(x=215, y=525)
        
        self.muestra_acsii = Button(self.pantalla, width = 15, height = 1, text = 'Mostrar Acsii', command = self.mostrar_matriz_acsii, relief="ridge", font = "Stencil", activebackground="lightgray")
        self.muestra_acsii.place(x=400, y=525)
        
        self.window.mainloop()
    
    #Funcion que oculta los botones al entrar en modo zoom
    def ocultar_botones(self):
        self.vertical.place_forget()
        self.horizontal.place_forget()
        self.derecha.place_forget()
        self.izquierda.place_forget()
        self.clear_all.place_forget()
        self.contraste.place_forget()
        self.negate.place_forget()
        self.abrir_img.place_forget()
        self.guardar_img.place_forget()
        self.circulo.place_forget()
        self.cuadrado.place_forget()
        self.rellenar.place_forget()
        self.muestra_acsii.place_forget()
        self.muestra_num.place_forget()
    
    #Funcion que muestra los botones tras salir de modo zoom
    def mostrar_botones(self):
        self.vertical.place(x=5, y=100)
        self.horizontal.place(x=5, y=175)
        self.derecha.place(x=5, y=250)
        self.izquierda.place(x=5, y=325)
        self.clear_all.place(x=5, y=400)
        self.contraste.place(x=5, y=525)
        self.negate.place(x=5, y=460)
        self.abrir_img.place(x=620, y=15)
        self.guardar_img.place(x=710, y=15)
        self.circulo.place(x=620, y=475)
        self.cuadrado.place(x=620, y=525)
        self.rellenar.place(x=620, y=425)
        self.muestra_num.place(x=215, y=525)
        self.muestra_acsii.place(x=400, y=525)
        
    #Funcion que asigna el valor a guardar en la matriz y el color que corresponde a este al presionar un color en la interfaz
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
    
    #Funcion que permite recordar que color se tenia seleccionado tras actuaizar el lienzo
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
            
    #Funcion que asigna todos los cuadros blancos y representa la matriz como un numero en el centro de cada cuadro
    def mostrar_matriz_num(self):
        self.set_cont(1)
        matriz = self.get_matriz()
        if self.isNum:
            self.isNum = False
            for fila in matriz:
                for columna in fila:
                    self.lienzo.itemconfig(f"cuadro{self.cont}", text=f"", fill = "black")
                    self.set_cont(self.get_cont()+1)
            self.actualiza_lienzo()
            self.islock=False
            self.lienzo.bind("<Button-1>", self.on_canvas_click)
            self.lienzo.bind("<B1-Motion>", self.on_canvas_motion)
        else:
            self.islock=True
            self.lienzo.unbind("<Button-1>")
            self.lienzo.unbind("<B1-Motion>")
            self.isNum = True
            for fila in matriz:
                for columna in fila:
                    self.lienzo.itemconfig(f"pixel{self.cont}", fill = "white")
                    self.lienzo.itemconfig(f"cuadro{self.cont}", text=f"{columna}", fill = "black")
                    self.set_cont(self.get_cont()+1)
            
    #Funcion que asigna cada cuadro blanco y representa el valor de la matriz con su valor ascii        
    def mostrar_matriz_acsii(self):
        self.set_cont(1)
        matriz = self.get_matriz()
        if self.isAscii:
            self.isAscii = False
            for fila in matriz:
                for columna in fila:
                    self.lienzo.itemconfig(f"cuadro{self.cont}", text=f"", fill = "black")
                    self.set_cont(self.get_cont()+1)
            self.actualiza_lienzo()
            self.islock=False
            self.lienzo.bind("<Button-1>", self.on_canvas_click)
            self.lienzo.bind("<B1-Motion>", self.on_canvas_motion)
        else:
            self.islock=True
            self.lienzo.unbind("<Button-1>")
            self.lienzo.unbind("<B1-Motion>")
            ascii_index = [' ','.',':','-','=','¡','&','$','%','@']
            self.isAscii = True
            for fila in matriz:
                for columna in fila:
                    self.lienzo.itemconfig(f"pixel{self.cont}", fill = "white")
                    self.lienzo.itemconfig(f"cuadro{self.cont}", text=f"{ascii_index[columna]}", fill = "black")
                    self.set_cont(self.get_cont()+1)

    def hide_matriz(self):
        for i in range(self.cont):
            self.lienzo.itemconfig(f"pixel{i}", state='hidden')
            self.lienzo.itemconfig(f"cuadro{i}", state='hidden')
    
    def mostrar_matriz(self):
        for i in range(self.cont):
            self.lienzo.itemconfig(f"pixel{i}", state='normal')
            self.lienzo.itemconfig(f"cuadro{i}", state='normal')

    def mostrar_matriz_zoomed(self):
        self.hide_matriz()
        self.ocultar_botones()

        for i in range(self.cont):
            self.lienzo.delete(f"zoomed_pixel{i}")


        n = abs((self.lienzo.start_x // (self.SIZE)) - (self.lienzo.end_x // (self.SIZE))) + 1
        m = abs((self.lienzo.start_y // (self.SIZE)) - (self.lienzo.end_y // (self.SIZE))) + 1
        self.x = 0
        self.y = 0
        if n >= m:
            self.zoomed_SIZEx = 430 // n
            self.zoomed_SIZEy = 430 // n
            self.y = 215 - (self.zoomed_SIZEy * m)/2
            
            

        else:
            self.zoomed_SIZEx = 430 // m
            self.zoomed_SIZEy = 430 // m
            self.x = 215 - (self.zoomed_SIZEx * n)/2
            

        initial_x = self.x


        if self.isZoom:

            for fila in self.matriz_zoomed:
                for num in fila:
                    if num == 0:
                        color = ("white")
                    elif num == 1:
                        color =("pink")
                    elif num == 2:
                        color =("yellow")
                    elif num == 3:
                        color =("orange")
                    elif num == 4:
                        color =("green")
                    elif num == 5:
                        color =("red")
                    elif num == 6:
                        color =("blue")
                    elif num == 7:
                        color =("purple")
                    elif num == 8:
                        color =("brown")
                    elif num == 9:
                        color =("black")
                    self.lienzo.create_rectangle(self.x, self.y, self.x + self.zoomed_SIZEx, self.y + self.zoomed_SIZEy, fill = color , tag = f"zoomed_pixel{self.cont}")
                    self.cont+=1
                    self.x += self.zoomed_SIZEx + 1
                
                self.x = initial_x
                self.y+= self.zoomed_SIZEy + 1

    def zoom_out(self):
        self.y = 0
        self.x = 0
        for i in range(self.cont):
            self.lienzo.delete(f"zoomed_pixel{i}")
        self.mostrar_matriz()
        self.isZoom = False
        self.zoom = False
        self.matriz_zoomed = None
        self.zoom_button.config(text='Zoom In')
        self.mostrar_botones()
    
    def rellenar_color(self, event):
        x, y = event.x, event.y
        m = x // (self.SIZE+1)
        n = y // (self.SIZE+1)
        matriz = self.matriz
        color = self.get_color()
        self.color_to_paint = matriz[n][m]
        if color != self.color_to_paint:
            self.rellenar_color_aux(matriz, n, m, color)
        self.actualiza_lienzo() 
    
    def rellenar_color_aux(self, matriz, n, m, color):
        if 0 <= n < len(matriz) and 0 <= m < len(matriz[0]):
            if matriz[n][m] == self.color_to_paint:
                matriz[n][m] = color
                if n + 1 < len(matriz) and matriz[n+1][m] == self.color_to_paint:
                    self.rellenar_color_aux(matriz, n+1, m, color)
                if n - 1 >= 0 and matriz[n-1][m] == self.color_to_paint:
                    self.rellenar_color_aux(matriz, n-1, m, color)
                if m + 1 < len(matriz[0]) and matriz[n][m+1] == self.color_to_paint:
                    self.rellenar_color_aux(matriz, n, m+1, color)
                if m - 1 >= 0 and matriz[n][m-1] == self.color_to_paint:
                    self.rellenar_color_aux(matriz, n, m-1, color)
    


    def create_circle3(self,event):
        x, y = event.x, event.y
        n = x // (self.SIZE+1)
        m = y // (self.SIZE+1)
        c = self.get_color()
        self.radius = 3
        circle_matriz = [['x','x',c,c,c,'x','x'],
                        ['x',c,'x','x','x',c,'x'],
                        [c,'x','x','x','x','x',c],
                        [c,'x','x','x','x','x',c],
                        [c,'x','x','x','x','x',c],
                        ['x',c,'x','x','x',c,'x'],
                        ['x','x',c,c,c,'x','x'] ]
        initial_x = m - 3
        index_fila = 0
        for fila in circle_matriz:
            if initial_x < 0:
                    index_fila +=1
                    initial_x += 1
            else:
                index_columna = 0
                initial_y = n - 3 
                for columna in fila:
                    if initial_y < 0:
                            index_columna +=1
                            initial_y += 1
                    else:
                        if circle_matriz[index_fila][index_columna] == c:
                            self.matriz[initial_x][initial_y] = circle_matriz[index_fila][index_columna]
                        index_columna +=1
                        initial_y += 1
                        if initial_y > 19:
                            break
                initial_x += 1
                index_fila += 1
                if initial_x > 19:
                    break
        self.actualiza_lienzo() 

    
    def create_square(self,event):
        x, y = event.x, event.y
        n = x // (self.SIZE+1)
        m = y // (self.SIZE+1)
        c = self.get_color()
        square_matriz = [['x',c,c,c,c,c,'x'],
                        ['x',c,'x','x','x',c,'x'],
                        ['x',c,'x','x','x',c,'x'],
                        ['x',c,'x','x','x',c,'x'],
                        ['x',c,c,c,c,c,'x'] ]
        initial_x = m - 2
        index_fila = 0
        for fila in square_matriz:
            if initial_x < 0:
                    index_fila +=1
                    initial_x += 1
            else:
                index_columna = 0
                initial_y = n - 3
                for columna in fila:
                    if initial_y < 0:
                            index_columna +=1
                            initial_y += 1
                    else:
                        if square_matriz[index_fila][index_columna] == c:
                            self.matriz[initial_x][initial_y] = square_matriz[index_fila][index_columna]
                        index_columna +=1
                        initial_y += 1
                        if initial_y > 19:
                            break
                initial_x += 1
                index_fila += 1
                if initial_x > 19:
                    break
        self.actualiza_lienzo() 
                 
            
    #Funcion que pinta los cuadro cuando se le da click
    def on_canvas_click(self,event):
        self.cuadros_cambiados.clear()
        x, y = event.x, event.y
        cuadro = self.lienzo.find_overlapping(x, y, x, y)
        if cuadro not in self.cuadros_cambiados:
            self.lienzo.itemconfig(cuadro, fill=self.get_colorfill())
            self.cuadros_cambiados.add(cuadro)
            j = x // (self.SIZE + 1)
            i = y // (self.SIZE + 1)
            self.set_matriz_pos(i,j)            

    #funcion que pinta los cuadros conforme el mouse se mueve mientras esta presionado
    def on_canvas_motion(self,event):
        x, y = event.x, event.y
        cuadro = self.lienzo.find_overlapping(x, y, x, y)
        for item in cuadro:
            if item not in self.cuadros_cambiados:
                self.lienzo.itemconfig(item, fill=self.get_colorfill())
                self.cuadros_cambiados.add(item)
                j = x // (self.SIZE + 1)
                i = y // (self.SIZE + 1)
                #print("\n")
                #print(x, y)
                #print (j, i)
                self.matriz[i][j] = self.get_color()
                
    def zoom(self):
        if self.isZoom:
            self.zoom = False
            self.lienzo.bind("<Button-1>", self.on_canvas_click)
            self.lienzo.bind("<B1-Motion>", self.on_canvas_motion)
            self.lienzo.unbind("<ButtonRelease-1>")
            self.zoom_out()
        else:
            self.zoom = True
            self.zoom_button.config(bg="lightgray")
            self.lienzo.bind("<Button-1>", self.inicio_zoom)
            self.lienzo.bind("<B1-Motion>", self.select_zoom)
            self.lienzo.bind("<ButtonRelease-1>", self.fin_zoom)
    
    def Fill(self):
        if self.isFill:
            self.isFill = False
            self.rellenar.config(bg = 'SystemButtonFace')
            self.lienzo.bind("<Button-1>", self.on_canvas_click)
            self.lienzo.bind("<B1-Motion>", self.on_canvas_motion)
            self.lienzo.unbind("<ButtonRelease-1>")

        else:
            self.isFill = True
            self.rellenar.config(bg="lightgray")
            self.lienzo.bind("<Button-1>", self.rellenar_color)
            self.lienzo.unbind("<B1-Motion>")
            self.lienzo.unbind("<ButtonRelease-1>")
    
    def circle(self):
        if self.isCircle:
            self.isCircle = False
            self.circulo.config(bg = 'SystemButtonFace')
            self.lienzo.bind("<Button-1>", self.on_canvas_click)
            self.lienzo.bind("<B1-Motion>", self.on_canvas_motion)
            self.lienzo.unbind("<ButtonRelease-1>")

        else:
            self.isCircle = True
            self.circulo.config(bg="lightgray")
            self.lienzo.bind("<Button-1>", self.create_circle3)
            self.lienzo.unbind("<B1-Motion>")
            self.lienzo.unbind("<ButtonRelease-1>")
    
    def square(self):
        if self.isSquare:
            self.isSquare = False
            self.cuadrado.config(bg = 'SystemButtonFace')
            self.lienzo.bind("<Button-1>", self.on_canvas_click)
            self.lienzo.bind("<B1-Motion>", self.on_canvas_motion)
            self.lienzo.unbind("<ButtonRelease-1>")

        else:
            self.isSquare = True
            self.cuadrado.config(bg="lightgray")
            self.lienzo.bind("<Button-1>", self.create_square)
            self.lienzo.unbind("<B1-Motion>")
            self.lienzo.unbind("<ButtonRelease-1>")
    

    
    #funcion guarda las coordenadas al momento que se da click para seleccionar un area para el zoom
    def inicio_zoom(self, event):
        if self.matriz_zoomed == None:
            self.matriz_zoomed = None
            self.lienzo.start_x = event.x
            self.lienzo.start_y = event.y
    
    #Funcion que actualiza el rectangulo que representa el area seleccionada para el zoom mientras se mueve el mouse presionado
    def select_zoom(self, event):
        if self.matriz_zoomed == None:
            if self.lienzo.zoom:
                self.lienzo.delete(self.lienzo.zoom)
            x0, y0 = (self.lienzo.start_x, self.lienzo.start_y)
            x1, y1 = (event.x, event.y)
            self.lienzo.zoom = self.lienzo.create_rectangle(x0, y0, x1, y1, outline="black", width=3)
            #print(x0// (self.SIZE) ,y0// (self.SIZE) ,x1// (self.SIZE) ,y1// (self.SIZE))
        
    #Funcion que guarda las coordenas cuando se suelta el click mientras se hacia zoom
    def fin_zoom(self, event):
        if self.matriz_zoomed == None:
            self.lienzo.end_x = event.x
            self.lienzo.end_y = event.y 
            self.lienzo.delete(self.lienzo.zoom)
            self.lienzo.zoom = None
            self.zoom_button.config(text='Zoom Out')
            self.zoom_button.config(bg = 'SystemButtonFace')
            self.zoom_in()
        
    
    def zoom_in(self): #inicial donde se hace click y final donde se suelta
        fila_inicial = self.lienzo.start_y // (self.SIZE+1)
        fila_final = self.lienzo.end_y // (self.SIZE+1)
        columna_inicial = self.lienzo.start_x // (self.SIZE+1)
        columna_final = self.lienzo.end_x // (self.SIZE+1)

        if fila_inicial > 19:
            fila_inicial = 19
        if fila_final > 19:
            fila_final = 19
        if columna_inicial > 19:
            columna_inicial = 19
        if columna_final > 19:
            columna_final = 19

        if fila_inicial < 0:
            fila_inicial = 0
        if fila_final < 0:
            fila_final = 0
        if columna_inicial < 0:
            columna_inicial = 0
        if columna_final < 0:
            columna_final = 0

        matriz = self.matriz

        filas_nueva_matriz = abs(fila_inicial-fila_final) + 1
        columnas_nueva_matriz = abs(columna_inicial - columna_final) + 1

        #print('size nueva matriz es {}x{}'.format(filas_nueva_matriz,columnas_nueva_matriz))
        
        nueva_matriz = []

        if fila_inicial < fila_final and columna_inicial < columna_final: #EL PUNTO INICIAL ES LA ESQUINA SUP IZQ
            
            index_fila = fila_inicial
            for fila in range (filas_nueva_matriz):
                nueva_matriz.append([])
                index_columna = columna_inicial
                for columna in range (columnas_nueva_matriz):
                    nueva_matriz[fila].append(matriz[index_fila][index_columna])
                    index_columna += 1
                index_fila += 1
        elif fila_inicial < fila_final and columna_inicial > columna_final: #EL PUNTO INICIAL ES LA ESQUINA SUP DER

            index_fila = fila_inicial
            for fila in range (filas_nueva_matriz):
                nueva_matriz.append([])
                index_columna = columna_final
                for columna in range (columnas_nueva_matriz):
                    nueva_matriz[fila].append(matriz[index_fila][index_columna])
                    index_columna += 1
                index_fila += 1
        
        elif fila_inicial > fila_final and columna_inicial < columna_final: #EL PUNTO INICIAL ES LA ESQUINA INF IZQ

            index_fila = fila_final
            for fila in range (filas_nueva_matriz):
                nueva_matriz.append([])
                index_columna = columna_inicial
                for columna in range (columnas_nueva_matriz):
                    nueva_matriz[fila].append(matriz[index_fila][index_columna])
                    index_columna += 1
                index_fila += 1
        
        elif fila_inicial > fila_final and columna_inicial > columna_final: #EL PUNTO INICIAL ES LA ESQUINA INF DER

            index_fila = fila_final
            for fila in range (filas_nueva_matriz):
                nueva_matriz.append([])
                index_columna = columna_final
                for columna in range (columnas_nueva_matriz):
                    nueva_matriz[fila].append(matriz[index_fila][index_columna])
                    index_columna += 1
                index_fila += 1

        self.matriz_zoomed = nueva_matriz
        self.isZoom = True
        self.mostrar_matriz_zoomed()
        
        #print("MATRIZ CLEARED:")
        #print()
        for fila in self.matriz_zoomed:
            for columna in fila:
                print(' {} '.format(columna),end='')
            print()
    

                
    #Funcion que permite abrir un archivo json de la aplicacion desde el explorador
    def abrir_json(self):
        filename = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.json")])
        if filename:
            try:
                with open(filename, 'r') as file:
                    data = json.load(file)
                    self.set_creador(data.get('dueno'))
                    self.set_estado(data.get('estado'))
                    self.set_matriz(data.get('matriz'))
                    self.actualiza_lienzo()
                    self.pantalla.creadortxt.delete(0, END)
                    self.pantalla.creadortxt.insert(0, self.get_creador())
                    self.pantalla.varible.set(self.get_estado())
            except Exception as e:
                print("Error al abrir el archivo:", e)
            
    #Funcion que permite guardar la imagen en un archivo json    
    def guardar_json(self):
        if self.pantalla.creadortxt.get() == "":
            messagebox.showinfo("Alert", "Ingrese el nombre del creador")
        else:
            self.set_creador(self.pantalla.creadortxt.get())
            self.set_estado(self.pantalla.variable.get())
            filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivo JSON", "*.json")])
            if filename:
                data = {
                    'dueno': self.get_creador(),
                    'estado': self.get_estado(),
                    'matriz': self.get_matriz()
                }
                try:
                    with open(filename, 'w') as file:
                        json.dump(data, file, indent=4)
                        print("Archivo JSON guardado correctamente:", filename)
                        messagebox.showinfo("Exito", "Archivo a sido guardado")
                except Exception as e:
                    print("Error al guardar el archivo JSON:", e)

objeto = editor()
objeto.mostrar_interfaz()