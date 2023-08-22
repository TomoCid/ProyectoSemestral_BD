import tkinter as tk
from tkinter import PhotoImage,Label,Entry

#creacion de ventana
ventana=tk.Tk()

# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

#Calcular las coordenadas para centrar la ventana
posX = (ancho_pantalla - 1280) // 2  # 1280 es el ancho de la ventana
posY = (alto_pantalla - 720) // 2  # 720 es el alto de la ventana

# Establecer la geometría de la ventana
ventana.geometry("1280x720+{}+{}".format(posX, posY))

#titulo de la ventana
ventana.title("El Caribe DataBase")
ventana.configure(bg="black")



# Cargar una imagen para usar como fondo
imagen_fondo = PhotoImage(file="C:/Users/Gaspar/Desktop/Udec/Bases De Datos I/imagen.png")


# Crear un Canvas para mostrar la imagen de fondo
canvas = tk.Canvas(ventana, width=imagen_fondo.width(), height=imagen_fondo.height())
canvas.pack()

# Mostrar la imagen de fondo en el Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=imagen_fondo)

#textos en pantalla
canvas.create_text(600,40,text="El Caribe",font=("Arial", 60), fill="lightblue")
canvas.create_text(80,150,text="Ingresar Objeto:",font=("Arial", 15), fill="lightblue")

#entradas
entrada1=tk.Entry(canvas)
entrada1.place(x=160,y=140)
entrada1.configure(width=50,font=("Arial", 15))





ventana.mainloop()



