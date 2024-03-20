import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import math

# Funiónes elemtales
def sin(t):
    return np.sin(t)
def cos(t):
    return np.cos(t)
def tan(t):
    return np.tan(t)


# Función para graficar la función ingresada por el usuario
def plot_function():
    # Obtener la función ingresada por el usuario desde la entrada de texto
    function_str = entry_function.get()
    
    # Reemplazar '^' por '**' para los exponentes
    function_str = function_str.replace('^', '**')
    
    # Limpiar el área de dibujo antes de graficar
    ax.clear()
    
    # Definir el rango de valores de x
    x = np.linspace(x_min_var.get(), x_max_var.get(), 400)
    
    # Evaluar la función ingresada por el usuario para obtener los valores de y
    try:
        y = eval(function_str)
    except Exception as e:
        # Si hay un error al evaluar la función, mostrar un mensaje de error
        ax.text(0.5, 0.5, "Error: " + str(e), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    else:
        # Graficar la función si la evaluación fue exitosa
        ax.plot(x, y)
        ax.set_title('Gráfico de ' + function_str)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        
        # Fijar los límites de los ejes x e y
        ax.set_xlim(x_min_var.get(), x_max_var.get())
        ax.set_ylim(y_min_var.get(), y_max_var.get())
    
    # Actualizar el lienzo de Matplotlib en el widget de Tkinter
    canvas.draw()

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Graficador de funciones")

# Crear un marco para contener los widgets
frame = tk.Frame(root)
frame.pack()

# Crear un widget de entrada de texto para que el usuario ingrese la función
entry_function = tk.Entry(frame)
entry_function.pack(side=tk.TOP, padx=5, pady=5)

# Crear un marco para los ajustes de escala
scale_frame = tk.Frame(frame)
scale_frame.pack()

# Crear etiquetas y campos de entrada para los límites de los ejes x e y
x_min_label = tk.Label(scale_frame, text="x min:")
x_min_label.grid(row=0, column=0, padx=5, pady=5)
x_min_var = tk.DoubleVar()
x_min_entry = tk.Entry(scale_frame, textvariable=x_min_var)
x_min_entry.grid(row=0, column=1, padx=5, pady=5)
x_min_var.set(-10)

x_max_label = tk.Label(scale_frame, text="x max:")
x_max_label.grid(row=0, column=2, padx=5, pady=5)
x_max_var = tk.DoubleVar()
x_max_entry = tk.Entry(scale_frame, textvariable=x_max_var)
x_max_entry.grid(row=0, column=3, padx=5, pady=5)
x_max_var.set(10)

y_min_label = tk.Label(scale_frame, text="y min:")
y_min_label.grid(row=1, column=0, padx=5, pady=5)
y_min_var = tk.DoubleVar()
y_min_entry = tk.Entry(scale_frame, textvariable=y_min_var)
y_min_entry.grid(row=1, column=1, padx=5, pady=5)
y_min_var.set(-100)

y_max_label = tk.Label(scale_frame, text="y max:")
y_max_label.grid(row=1, column=2, padx=5, pady=5)
y_max_var = tk.DoubleVar()
y_max_entry = tk.Entry(scale_frame, textvariable=y_max_var)
y_max_entry.grid(row=1, column=3, padx=5, pady=5)
y_max_var.set(100)

# Crear un botón para graficar la función ingresada por el usuario
plot_button = tk.Button(frame, text="Graficar función", command=plot_function)
plot_button.pack(side=tk.TOP, padx=5, pady=5)

# Crear una figura de Matplotlib
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)

# Crear un lienzo de Matplotlib en el marco de Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Ejecutar la aplicación
root.mainloop()