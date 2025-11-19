import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Lista desplegable de Carreras")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Elige una opción")
etiqueta.pack(pady=10)

opciones = [
    "ARH",
    "Arquitectura",
    "Comercio electrónico",
    "Comercio internacional y aduanas",
    "Construcción",
    "Contabilidad",
    "Mecatrónica",
    "Programación"
]
ComboCarreras = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboCarreras.pack(pady=5)

def mostrar_seleccion(event):
    seleccion = ComboCarreras.get()
    etiqueta_resultado.config(text=f"Seleccionaste la carrera de: {seleccion}")

ComboCarreras.bind("<<ComboboxSelected>>", mostrar_seleccion)

etiqueta_resultado = tk.Label(ventana, text="Aún no has seleccionado ninguna carrera")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()
