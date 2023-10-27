import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Estadisticas:

    def __init__(self):
        self.datos = ["partidas_perdidas", "partidas_ganadas",
                      "ganadas en un intento",
                      "ganadas en 2 intentos",
                      "ganadas en 3 intentos",
                      "ganadas en 4 intentos",
                      "ganadas en mas de 5 intentos"]

        self.numeros = [4, 0, 3, 1, 2, 0, 8]

    def crear_grafica(self):
        fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
        ax.bar(self.datos, self.numeros)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)

        return fig






