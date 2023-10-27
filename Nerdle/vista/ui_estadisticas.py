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
        self.fig = self.estadisticas.crear_grafica()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = EstadisticasApp(root)
    root.mainloop()






