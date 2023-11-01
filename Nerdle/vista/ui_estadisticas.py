import smtplib
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Nerdle.modelo.estadisticas import Estadisticas


class EstadisticasApp:
    def _init_(self, root):
        self.correo_entry = None
        self.root = root
        self.root.title("Estadísticas")
        self.estadisticas = Estadisticas()
        self.create_widgets()
        self.create_plot()

    def create_widgets(self):
        label = tk.Label(self.root, text="Estadísticas de Juego")
        label.pack(pady=10)
        correo_label = tk.Label(self.root, text="¿Desea recibir sus estadísticas de juego por correo electrónico?:")
        correo_label.pack()
        self.correo_entry = tk.Entry(self.root)
        self.correo_entry.pack()
        enviar_button = tk.Button(self.root, text="Enviar Estadísticas", command=self.enviar_estadisticas)
        enviar_button.pack()

    def create_plot(self):
        fig = self.estadisticas.crear_grafica()
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

    def enviar_estadisticas(self):
        correo = self.correo_entry.get()
        if not correo:
            messagebox.showerror("Error", "Por favor, ingrese su correo electrónico.")
            return

        # para el servidor SMTP y credenciales
        smtp_server = 'tu_servidor_smtp'
        smtp_port = 587
        smtp_user = 'tu_correo@gmail.com'
        smtp_password = 'tu_contraseña'

        # lo que diria el mensaje de correo
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = correo
        msg['Subject'] = "Estadísticas de Juego"
        estadisticas_text = "Aquí van tus estadísticas:"
        msg.attach(MIMEText(estadisticas_text, 'plain'))  # formato para las estadisticas

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, correo, msg.as_string())
            server.quit()
            messagebox.showinfo("Éxito", "Estadísticas enviadas exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron enviar las estadísticas. Error: {str(e)}")


if __name__ == "_main_":
    root = tk.Tk()
    app = EstadisticasApp(root)
    root.mainloop()
