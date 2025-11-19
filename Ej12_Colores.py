import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Lista desplegable ComboBox")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Elige un color")
etiqueta.pack(pady=10)

opciones = ["Rojo", "Verde", "Azul", "Amarillo", "Morado"]
ComboColores = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboColores.pack(pady=5)

# Diccionario para relacionar el nombre del color con su color real
colores_dict = {
    "Rojo": "red",
    "Verde": "green",
    "Azul": "blue",
    "Amarillo": "yellow",
    "Morado": "purple"
}

def mostrar_seleccion(event):
    seleccion = ComboColores.get()
    etiqueta_resultado.config(
        text=f"Seleccionaste: {seleccion}",
        fg=colores_dict.get(seleccion, "black")
    )
ComboColores.bind("<<ComboboxSelected>>", mostrar_seleccion)

etiqueta_resultado = tk.Label(ventana, text="Aún no has seleccionado nada")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()
