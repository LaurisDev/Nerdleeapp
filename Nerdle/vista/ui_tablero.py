
import subprocess
import tkinter as tk


ventana = tk.Tk()
ventana.title("NERDLE")
filas = 6
columnas = 8

# Crear un contenedor para el tablero
contenedor_tablero = tk.Frame(ventana)
contenedor_tablero.pack()


def crear_celda(fila_celda, columna_celda):
    celda = tk.Label(contenedor_tablero, text=" ", width=10, height=4, relief="ridge")
    celda.grid(row=fila_celda, column=columna_celda)
    return celda


tablero = [[" " for _ in range(columnas)] for _ in range(filas)]
celdas_tablero = [[crear_celda(fila, columna) for columna in range(columnas)] for fila in range(filas)]


def boton_numero_clic(numero):
    global casilla_activa
    tablero[0][casilla_activa] = str(numero)
    celdas_tablero[0][casilla_activa].config(text=str(numero))
    casilla_activa += 1


def boton_suma_clic():
    global casilla_activa
    if casilla_activa < columnas - 1:  # Verifica que haya suficientes casillas disponibles
        tablero[0][casilla_activa] = "+"
        celdas_tablero[0][casilla_activa].config(text="+")
        casilla_activa += 1


def boton_resta_clic():
    global casilla_activa
    if casilla_activa < columnas - 1:
        tablero[0][casilla_activa] = "-"
        celdas_tablero[0][casilla_activa].config(text="-")
        casilla_activa += 1


def boton_multi_clic():
    global casilla_activa
    if casilla_activa < columnas - 1:
        tablero[0][casilla_activa] = "*"
        celdas_tablero[0][casilla_activa].config(text="*")
        casilla_activa += 1


def boton_div_clic():
    global casilla_activa
    if casilla_activa < columnas - 1:
        tablero[0][casilla_activa] = "/"
        celdas_tablero[0][casilla_activa].config(text="/")
        casilla_activa += 1


def boton_igual_clic():
    global casilla_activa
    if casilla_activa < columnas - 1:
        tablero[0][casilla_activa] = "="
        celdas_tablero[0][casilla_activa].config(text="=")
        casilla_activa += 1


def boton_borrar_clic():
    global casilla_activa
    if casilla_activa > 0:
        casilla_activa -= 1
        tablero[0][casilla_activa] = " "
        celdas_tablero[0][casilla_activa].config(text=" ")


casilla_activa = 0

# Crear botones numéricos
for numero in range(0, 10):
    boton = tk.Button(contenedor_tablero, text=str(numero), width=10, height=2, command=lambda num=numero: boton_numero_clic(num))
    fila_boton = filas + numero // columnas
    columna_boton = numero % columnas
    boton.grid(row=fila_boton, column=columna_boton, padx=2, pady=2)


# Boton de operación de suma
boton_suma = tk.Button(contenedor_tablero, text='+', width=10, height=2, command=boton_suma_clic)
fila_boton_suma = filas + 1
columna_boton_suma = 2
boton_suma.grid(row=fila_boton_suma, column=columna_boton_suma, padx=2, pady=2)

# Boton de operación de resta
boton_resta = tk.Button(contenedor_tablero, text="-", width=10, height=2, command=boton_resta_clic)
fila_boton_resta = filas + 1
columna_boton_resta = 3
boton_resta.grid(row=fila_boton_resta, column=columna_boton_resta, padx=2, pady=2)

# Boton de operación de multiplicacion
boton_multiplicacion = tk.Button(contenedor_tablero, text="*", width=10, height=2, command=boton_multi_clic)
fila_boton_multiplicacion = filas + 1
columna_boton_multiplicacion = 4
boton_multiplicacion.grid(row=fila_boton_multiplicacion, column=columna_boton_multiplicacion, padx=2, pady=2)

# Boton de operación de division
boton_division = tk.Button(contenedor_tablero, text="/", width=10, height=2, command=boton_div_clic)
fila_boton_div = filas + 1
columna_boton_div = 5
boton_division.grid(row=fila_boton_div, column=columna_boton_div, padx=2, pady=2)

# Boton de operación de igual
boton_igual = tk.Button(contenedor_tablero, text="=", width=10, height=2, command=boton_igual_clic)
fila_boton_igual = filas + 1
columna_boton_igual = 6
boton_igual.grid(row=fila_boton_igual, column=columna_boton_igual, padx=2, pady=2)

# Boton de operación de borrar
boton_borrar = tk.Button(contenedor_tablero, text="Borrar", width=10, height=2, command= boton_borrar_clic)
fila_boton_borrar = filas + 2
columna_boton_borrar = 3 % columnas
boton_borrar.grid(row=fila_boton_borrar, column=columna_boton_borrar, padx=2, pady=2)

# boton de ingresar la ecuacion para posteriormente compararla
boton_ingresar = tk.Button(contenedor_tablero, text="Ingresar", width=10, height=2)
fila_boton_ingresar = filas + 2
columna_boton_ingresar = 4 % columnas
boton_ingresar.grid(row=fila_boton_ingresar, column=columna_boton_ingresar, padx=2, pady=2)


# Función para abrir el otro programa
def abrir_intrucciones():
    try:
        subprocess.Popen(["python", "ui_intrucciones.py"])
    except FileNotFoundError:
        print("El archivo del otro programa no se encuentra.")


boton_intrucciones = tk.Button(ventana, text=" Ver instrucciones", command=abrir_intrucciones)
boton_intrucciones.pack()

ventana.mainloop()



