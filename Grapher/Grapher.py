import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funciones
#------------------------------------------------------------------------
# Obtener información

def plot():
    max_x_info = max_x.get()
    max_y_info = max_y.get()
    min_x_info = min_x.get()
    min_y_info = min_y.get()
    func_info = str(func.get())
    print("max_x_info")


# Crear interfaz gráfica
#------------------------------------------------------------------------
# Crear una instancia de la clase Tk para la ventana principal
root = tk.Tk()
root.geometry("960x540")
root.resizable(width=False, height=False)
root.title("Graficadora")

# Icono personalizado
icon = tk.PhotoImage(file="LogoUG.png")
root.iconphoto(True, icon)



# Crear y ajustar Frame (contenedor)
#-------------------------------------------------------------------------
# Crear un Frame (contenedor)
head = tk.Frame(root, height= 100, bg="blue")
head.pack(fill="x")
# Definir la malla de head
head.columnconfigure(0, weight = 1)
head.columnconfigure(1, weight = 1)
head.columnconfigure(2, weight = 1)
head.columnconfigure(3, weight = 1)
head.rowconfigure(0, weight = 1)
head.rowconfigure(1, weight = 1)
head.rowconfigure(2, weight = 1)

# Widgets
#-------------------------------------------------------------------------
# Crear entradas
max_x = tk.Entry(head)
min_x = tk.Entry(head)
max_y = tk.Entry(head)
min_y = tk.Entry(head)
func = tk.Entry(head)

# Crear etiquetas
max_x_label = tk.Label(head,text = "max x")
min_x_label = tk.Label(head,text = "min x")
max_y_label = tk.Label(head,text = "max y")
min_y_label = tk.Label(head,text = "min y")
func_label = tk.Label(head,text = "Función")

# Crear botones
graph = tk.Button(head, text="Graficar", command = plot())



# Colocar widgets
max_x.grid(row = 0, column = 1)
min_x.grid(row = 0, column = 3)
max_y.grid(row = 1, column = 1)
min_y.grid(row = 1, column = 3)
func.grid(row = 2, column = 1)

max_x_label.grid(row = 0, column = 0)
max_y_label.grid(row = 0, column = 2)
min_x_label.grid(row = 1, column = 0)
min_y_label.grid(row = 1, column = 2)
func_label.grid(row = 2, column = 0)


graph.grid(row = 2, column = 2)





# Crear gráfico de funciones
#----------------------------------------------------------------------
# Crear un rango de valores de x
#x = np.linspace(0, 2*np.pi, 100)

# Calcular los valores de y para la función seno
#y = np.sin(x)

# Trazar la función
#plt.plot(x, y)

# Personalizar el gráfico
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Función seno')

# Ajustar los límites de los ejes
#plt.xlim(0, 2*np.pi)
#plt.ylim(-1.5, 1.5)  # Ajustar los límites del eje y a -1.5 y 1.5

# Mostrar el gráfico
#plt.show()




# Iniciar el bucle principal de la aplicación
root.mainloop()#############################################################
