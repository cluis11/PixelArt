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





def png_to_matrix(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to RGB (if it's not already in that mode)
    image = image.convert('RGB')
    
    # Get the dimensions of the image
    width, height = image.size
    
    # Create an empty matrix to store pixel values
    pixel_matrix = []
    
    # Iterate through each pixel in the image
    for y in range(height):
        row = []
        for x in range(width):
            # Get the RGB values of the pixel
            r, g, b = image.getpixel((x, y))
            
            # Convert RGB to a single value (e.g., grayscale)
            pixel_value = (r << 16) + (g << 8) + b  # Combining RGB values into a single integer
            
            # Append the pixel value to the row
            row.append(pixel_value)
        # Append the row to the matrix
        pixel_matrix.append(row)
    
    return pixel_matrix



def abrir_json():
    filename = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.json")])
    if filename:
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                dueno = data.get('dueno')
                estado = data.get('estado')
                matriz = data.get('matriz')
                print("Dueño:", dueno)
                print("Estado:", estado)
                print("Matriz:", matriz)
                # Puedes usar las variables 'dueno', 'estado' y 'matriz' según sea necesario
        except Exception as e:
            print("Error al abrir el archivo:", e)


def guardar_json(dueno, estado, matriz):
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivo JSON", "*.json")])
    if filename:
        data = {
            'dueno': dueno,
            'estado': estado,
            'matriz': matriz
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
                print("Archivo JSON guardado correctamente:", filename)
        except Exception as e:
            print("Error al guardar el archivo JSON:", e)

root = tk.Tk()
root.title("Guardar Archivo JSON")

dueno = "Luis"
estado = "terminado"
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Por ejemplo, tu matriz aquí

button = tk.Button(root, text="Guardar JSON", command=lambda: guardar_json(dueno, estado, matriz))
button.pack(pady=20)

root.mainloop()
