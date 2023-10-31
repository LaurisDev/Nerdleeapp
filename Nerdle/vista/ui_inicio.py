import subprocess
import tkinter as tk
import sqlite3
from tkinter import messagebox


# Crear una conexión a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear la tabla de usuarios si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (usuario TEXT PRIMARY KEY, contraseña TEXT)''')
conn.commit()


# Función para el registro de usuario
def registrar_usuario():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if usuario and contraseña:
        try:
            cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contraseña))
            conn.commit()
            messagebox.showinfo("Registro", "Registro exitoso")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El usuario ya existe")
    else:
        messagebox.showerror("Error", "Por favor, ingresa usuario y contraseña.")


# Función para el inicio de sesión
# Función para el inicio de sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if usuario and contraseña:
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?", (usuario, contraseña))
        if cursor.fetchone() is not None:
            try:
                subprocess.Popen(["python", "ui_menu.py"])
            except FileNotFoundError:
                print("El archivo del menú no se encuentra.")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    else:
        messagebox.showerror("Error", "Por favor, ingresa usuario y contraseña.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Inicio de Sesión y Registro")

# Crear campos de entrada
label_usuario = tk.Label(ventana, text="Usuario:")
label_contraseña = tk.Label(ventana, text="Contraseña:")
entry_usuario = tk.Entry(ventana)
entry_contraseña = tk.Entry(ventana, show='*')

# Crear botones para registro e inicio de sesión
boton_registrar = tk.Button(ventana, text="Registrar", command=registrar_usuario)
boton_iniciar = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)

# Colocar elementos en la ventana
label_usuario.grid(row=0, column=0)
label_contraseña.grid(row=1, column=0)
entry_usuario.grid(row=0, column=1)
entry_contraseña.grid(row=1, column=1)
boton_registrar.grid(row=2, column=0, columnspan=2)
boton_iniciar.grid(row=3, column=0, columnspan=2)

ventana.mainloop()
