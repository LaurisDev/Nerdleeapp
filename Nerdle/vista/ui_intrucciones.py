import tkinter as tk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Instrucciones")

# Tamaño de la ventana
ancho = 900
alto = 850

# Crear un lienzo con un fondo degradado vertical
lienzo = tk.Canvas(ventana, width=ancho, height=alto)
lienzo.pack()

color_inicio = "#FAED52"  # Amarillo
color_fin = "#55FA89"    # Verde

for i in range(ancho):
    r = int(int(color_inicio[1:3], 16) + (int(color_fin[1:3], 16) - int(color_inicio[1:3], 16)) * i / ancho)
    g = int(int(color_inicio[3:5], 16) + (int(color_fin[3:5], 16) - int(color_inicio[3:5], 16)) * i / ancho)
    b = int(int(color_inicio[5:7], 16) + (int(color_fin[5:7], 16) - int(color_inicio[5:7], 16)) * i / ancho)
    color = f"#{r:02X}{g:02X}{b:02X}"
    lienzo.create_line(i, 0, i, alto, fill=color)


# Crear un widget Label para mostrar las instrucciones predefinidas
instrucciones_predefinidas = """ Bienvenido al juego de adivinanza matemática:

El objetivo es adivinar la secuencia matemática en un número limitado de intentos. La secuencia consta de números entre 0 y 9, operaciones matemáticas básicas y el signo de igualdad.",
Puedes intentar adivinar la secuencia escribiendo una expresión matemática válida.
Por ejemplo, si la secuencia es '2 + 3 = 5', puedes intentar con '2+3=5'.
El juego te dará pistas sobre cuántos números y operadores has adivinado correctamente. ¡Diviértete y buena suerte!

NORMAS:

 * Cada suposición es un cálculo.
            * Puedes usar 0 1 2 3 4 5 6 7 8 9 + - * / = 
            * Debe contener un = 
            * Sólo debe tener un número a la derecha de =, no otro cálculo. 
            * Se aplica el orden estándar de operaciones, así que calcule * y / antes de + y - 
            POR EJEMPLO: 3 + 2 * 5 = 13 no 25.
            * Si la respuesta que buscamos es 10+20 = 30, entonces tambien se acepta 20+10=30
"""

# Configurar la fuente y el ancho del Label
font_style = ("Helvetica", 15)  # Cambiar "Helvetica" al tipo de fuente que desees y 20 al tamaño de fuente
etiqueta_instrucciones = tk.Label(ventana, text=instrucciones_predefinidas, justify="left", font=font_style, wraplength=900)
etiqueta_instrucciones.place(relx=0.5, rely=0.5, anchor="center")  # Posiciona el Label en el centro

titulo = """
⭒＊*•̩̩͙✩•̩̩͙*˚⍣˚*•̩̩͙✩•̩̩͙*˚＊⭒ INSTRUCCIONES ⭒＊*•̩̩͙✩•̩̩͙*˚⍣˚*•̩̩͙✩•̩̩͙*˚＊⭒

"""
font_style = ("Helvetica", 20)  # Cambiar "Helvetica" al tipo de fuente que desees y 20 al tamaño de fuente
etiqueta_titulo = tk.Label(ventana, text=titulo, justify="left", font=font_style, wraplength=900)
etiqueta_titulo.place(relx=0.5, rely=0.1, anchor="center")  # Posiciona el título en la parte superior

# Iniciar la aplicación
ventana.mainloop()


