import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Nerdle.modelo.estadisticas import Estadisticas


class EstadisticasApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Estadísticas")
        self.estadisticas = Estadisticas()
        self.create_widgets()
        self.create_plot()

    def create_widgets(self):
        label = tk.Label(self.root, text="Estadísticas de Juego")
        label.pack(pady=10)

    def create_plot(self):
        fig = self.estadisticas.crear_grafica()
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = EstadisticasApp(root)
    root.mainloop()
