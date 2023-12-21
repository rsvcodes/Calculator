from tkinter import Tk, Button, Entry

# Función para manejar clics en botones numéricos u operadores
def click_boton(valor):
    entrada.insert("end", valor)

# Función para borrar la entrada
def borrar():
    entrada.delete(0, "end")

# Función para realizar la operación al presionar "="
def hacer_operacion():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, "end")
        entrada.insert("end", str(resultado))
    except Exception as e:
        entrada.delete(0, "end")
        entrada.insert("end", "Error")

# Crear la ventana principal
ventana = Tk()
ventana.title("Calculadora")

# Crear la entrada para mostrar la expresión y el resultado
entrada = Entry(ventana, width=20, font=("Arial", 14), borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definir botones
boton0 = Button(ventana, text="0", width=13, height=2, command=lambda: click_boton("0"))
boton_borrar = Button(ventana, text="AC", width=5, height=2, command=borrar)
boton_parentesis1 = Button(ventana, text="(", width=5, height=2, command=lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text=")", width=5, height=2, command=lambda: click_boton(")"))
boton_punto = Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."))

boton_div = Button(ventana, text="/", width=5, height=2, command=lambda: click_boton("/"))
boton_mult = Button(ventana, text="x", width=5, height=2, command=lambda: click_boton("*"))
boton_sum = Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"))
boton_rest = Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"))
boton_igual = Button(ventana, text="=", width=5, height=2, command=hacer_operacion)

# Colocar botones en la ventana
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()