import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import os

# Variable global para mantener una referencia al widget del gráfico
grafico = None

def cargar_archivo():
    global grafico  # Declarar la variable global

    # Eliminar el gráfico anterior si existe
    if grafico:
        grafico.get_tk_widget().destroy()

    # Definir una función para verificar si un archivo no es oculto
    def no_oculto(archivo):
        return not archivo.startswith('.')
    
    # Obtener el directorio actual como directorio inicial
    directorio_actual = os.getcwd()
    
    # Iterar hacia arriba en el árbol de directorios hasta encontrar un directorio que no contenga archivos ocultos
    while directorio_actual != '/':
        archivos = os.listdir(directorio_actual)
        if any(no_oculto(archivo) for archivo in archivos):
            break
        directorio_actual = os.path.dirname(directorio_actual)
    
    # Abrir el cuadro de diálogo para seleccionar el archivo
    ruta_archivo = filedialog.askopenfilename(initialdir=directorio_actual)
    
    # Verificar si se seleccionó un archivo
    if ruta_archivo:
        try:
            # Leer el archivo seleccionado
            df = pd.read_excel(ruta_archivo)
            # Verificar la cantidad de columnas
            num_columnas = len(df.columns)
            if num_columnas != 2:
                messagebox.showwarning("Advertencia", "El archivo seleccionado no tiene dos columnas. Por favor, seleccione un archivo con exactamente dos columnas.")
                return
            # Obtener las dos columnas del DataFrame
            x_data = df.iloc[:, 0].values.reshape(-1, 1)  # Datos en la primera columna
            y_data = df.iloc[:, 1].values  # Datos en la segunda columna

            # Ajustar el modelo polinómico
            grado_polinomio = 2  # Grado del polinomio de ajuste (puedes ajustar esto según sea necesario)
            poly_features = PolynomialFeatures(degree=grado_polinomio)
            x_poly = poly_features.fit_transform(x_data)
            model = LinearRegression()
            model.fit(x_poly, y_data)

            # Generar puntos para el gráfico del polinomio aproximado
            x_puntos = np.linspace(min(x_data), max(x_data), 100).reshape(-1, 1)
            x_puntos_poly = poly_features.transform(x_puntos)
            y_puntos = model.predict(x_puntos_poly)

            # Crear una cadena de texto con el polinomio aproximado
            coeficientes = model.coef_
            polinomio_texto = "Polinomio Aproximado: "
            for i, coeficiente in enumerate(coeficientes):
                polinomio_texto += f"{coeficiente:.2f}x^{i}"
                if i < grado_polinomio:
                    polinomio_texto += " + "

            # Graficar los datos y el polinomio aproximado
            plt.figure(figsize=(6, 4))
            plt.plot(x_data, y_data, marker='o', linestyle='', label='Datos')
            plt.plot(x_puntos, y_puntos, label=polinomio_texto, color='red')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Aproximación Polinómica')
            plt.legend()
            plt.grid(True)
            
            # Crear el widget para mostrar el gráfico en la interfaz
            grafico = FigureCanvasTkAgg(plt.gcf(), master=cont)
            grafico.draw()
            grafico.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            messagebox.showinfo("Información", "Aproximación polinómica realizada y graficada exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

def cerrar_ventana():
    cont.quit()  # Cerrar la ventana principal

# Crear la ventana principal
cont = tk.Tk()
cont.title("Graficadora")
cont.geometry("800x600")  # Tamaño de la ventana (ancho x alto)

# Bloquear el cambio de tamaño de la ventana
cont.resizable(False, False)

# Botón para cargar el archivo
btn_cargar = tk.Button(cont, text="Cargar Archivo", command=cargar_archivo)
btn_cargar.pack(pady=10)

# Asociar la función de cierre al evento de cerrar ventana
cont.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Ejecutar el bucle principal de la ventana
cont.mainloop()
