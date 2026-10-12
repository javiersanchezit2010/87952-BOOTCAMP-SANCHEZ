import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Saludo")
ventana.geometry("640x480")

# Texto de indicación
label_nombre = tk.Label(ventana, text="Ingrese su nombre:")
label_nombre.pack(pady=20)

# Cuadro de texto
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Label donde aparecerá el saludo
label_saludo = tk.Label(ventana, text="")
label_saludo.pack(pady=20)


# Función que se ejecuta al presionar el botón
# Este saludar es horrible, es una funcion impura! Usa cosas de afuera
#def saludar():
#    nombre = entrada_nombre.get()
#    label_saludo.config(text="¡Hola " + nombre + "!")

def saludar(campo_nombre, label_resultado):
    nombre = campo_nombre.get()
    label_resultado.config(text="¡Hola " + nombre + "!") 

# Botón
boton = tk.Button(ventana, text="Saludar", command=lambda: saludar(entrada_nombre, label_saludo))
boton.pack()

# Mantener la ventana abierta
ventana.mainloop()