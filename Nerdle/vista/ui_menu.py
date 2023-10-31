import subprocess
import tkinter as tk
from tkinter import messagebox

ventana_principal = tk.Tk()


def iniciar_juego():
    try:
        subprocess.Popen(["python", "ui_tablero.py"])
    except FileNotFoundError:
        print("El archivo del tablero no se encuentra.")


boton_iniciar_juego = tk.Button(ventana_principal, text="INICIAR JUEGO", command=iniciar_juego, bg="#6EF592",
                                fg="white")
boton_iniciar_juego.grid(row=2, column=0, padx=10)


def ver_instrucciones():
    try:
        subprocess.Popen(["python", "ui_intrucciones.py"])
    except FileNotFoundError:
        print("El archivo del otro programa no se encuentra.")


boton_intrucciones = tk.Button(ventana_principal, text="INSTRUCCIONES", command=ver_instrucciones, bg="#6EF592",
                               fg="white")
boton_intrucciones.grid(row=2, column=1, padx=10)


def ver_estadistica():
    try:
        subprocess.Popen(["python", "ui_estadisticas.py"])
    except FileNotFoundError:
        print("El archivo no se encuentra")


boton_estadistica = tk.Button(ventana_principal, text="ESTADISTICA", command=ver_estadistica, bg="#6EF592", fg="white")
boton_estadistica.grid(row=2, column=2, padx=10)


def cerrar_sesion():
    respuesta = messagebox.askyesno("Cerrar Sesión", "¿Seguro que quieres cerrar la sesión?")
    if respuesta:
        ventana_principal.destroy()


boton_cerrar_sesion = tk.Button(ventana_principal, text="CERRAR SESIÓN", command=cerrar_sesion, bg="red", fg="white")
boton_cerrar_sesion.grid(row=2, column=3, padx=10)

ventana_principal.geometry("450x300")  # Tamaño de la ventana
ventana_principal.resizable(0,0)

# Configurar color de fondo
ventana_principal.configure(bg='#6EF5C0')

# Centrar el título
nombre_juego_label = tk.Label(ventana_principal, text="NERDLE", fg='white', font=("Arial", 20), bg="#6EF5C0")
nombre_juego_label.grid(row=1, column=0, columnspan=4, pady=20)

ventana_principal.title("Menú")

ventana_principal.mainloop()

