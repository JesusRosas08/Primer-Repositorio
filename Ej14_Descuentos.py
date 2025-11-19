import tkinter as tk

ventana = tk.Tk()
ventana.title("Calcular Descuentos")
ventana.geometry("500x400")
ventana.resizable(False, True)

etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana, justify="center")
entrada_cantidad.pack()

# Variable para guardar la opción seleccionada
seleccion = tk.IntVar()
# Botones de radio
tk.Radiobutton(ventana, text="5% de descuento", variable=seleccion, value=1).pack()
tk.Radiobutton(ventana, text="10% de descuento", variable=seleccion, value=2).pack()
tk.Radiobutton(ventana, text="15% de descuento", variable=seleccion, value=3).pack()
# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

def ejecutar_radio():
    try:
        cantidad = float(entrada_cantidad.get())
        opcion = seleccion.get()

        if opcion == 1:
            descuento = cantidad * 0.05
            total = cantidad - descuento
            etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un Descuento del 5% el cual usted pagara: {total:.2f}")
        elif opcion == 2:
            descuento = cantidad * 0.10
            total = cantidad - descuento
            etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un Descuento del 10% el cual usted pagara: {total:.2f}")
        elif opcion == 3:
            descuento = cantidad * 0.15
            total = cantidad - descuento
            etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un Descuento del 15% el cual usted pagara: {total:.2f}")
        else:
            etiqueta_resultado.config(text="Seleccione una opción de descuento.")
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingrese una cantidad válida.")
tk.Button(ventana, text="Calcular", command=ejecutar_radio).pack(pady=10)
ventana.mainloop()
