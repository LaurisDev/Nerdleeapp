import sys
from typing import Optional

from Nerdle.modelo.claseEcuacion import Ecuacion
from Nerdle.modelo.modelo import Nerdle


class UIConsola:
    def __init__(self):
        self.nerdle: Optional[Nerdle] = None
        self.ecuacion = Ecuacion()
        self.opciones = {
            "1": self.mostrar_intrucciones,
            "2": self.iniciar_nuevo_juego,
            "3": self.ver_estadisticas,
            "0": self.salir
        }

    @staticmethod
    def mostrar_menu():
        titulo = "NERDLE"
        print(f"\n{titulo:_^30}")
        print("1. Ver instrucciones")
        print("2. Iniciar nuevo juego")
        print("3. Ver estadisticas")
        print("0.Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        print("\nBIEVENID@ A NUESTRO JUEGO DE NERDLE")
        self.registrar_jugador()
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    @staticmethod
    def mostrar_intrucciones():
        titulo = "¿Cómo Jugar?"
        subtitulo = "Normas: "
        instrucciones = [
                "Bienvenido al juego de adivinanza matemática.",
                "El objetivo es adivinar la secuencia matemática en un número limitado de intentos.",
                "La secuencia consta de números entre 0 y 9, operaciones matemáticas básicas y el signo de igualdad.",
                "Puedes intentar adivinar la secuencia escribiendo una expresión matemática válida.",
                "Por ejemplo, si la secuencia es '2 + 3 = 5', puedes intentar con '2+3=5'.",
                "El juego te dará pistas sobre cuántos números y operadores has adivinado correctamente.",
                "¡Diviértete y buena suerte!"
            ]
        normas = [
            "* Cada suposición es un cálculo.",
            "* Puedes usar 0 1 2 3 4 5 6 7 8 9 + - * / = ",
            "* Debe contener un = ",
            "* Sólo debe tener un número a la derecha de =, no otro cálculo. ",
            "* Se aplica el orden estándar de operaciones, así que calcule * y / antes de + y - ",
            "POR EJEMPLO: 3 + 2 * 5 = 13 no 25.",
            "* Si la respuesta que buscamos es 10+20 = 30, entonces tambien se acepta 20+10=30."
        ]

        print(f"\n{titulo.center(40)}")
        for instruccion in instrucciones:
            print(f"{instruccion}")
        print(f"\n{subtitulo}")
        for normas in normas:
            print(f"\n{normas}")

    def iniciar_nuevo_juego(self):
        print(f"{'_':_^30}")
        titulo = "COMIENZA A JUGAR: "
        print(f"\n{titulo.center(30)}")
        self.nerdle.iniciar_juego()
        print(f"La ecuacion generada es: = {self.ecuacion.generar_ecuacion()}")


    def ver_estadisticas(self):
        pass

    @staticmethod
    def salir():
        print("\nGRACIAS POR JUGAR CON NOSOTROS. VUELVA PRONTO")
        sys.exit(0)

    def registrar_jugador(self):
        nombre: str = input("¿Cuál es tu nombre?: ")
        correo: str = input("¿Cuál es su correo electrónico?: ")
        self.nerdle = Nerdle()
        self.nerdle.registrar_nombre_jugador(nombre)
        self.nerdle.registrar_correo_jugador(correo)