
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora - Semana 13")
ventana.geometry("300x400")
ventana.resizable(False, False)

# Pantalla de la calculadora
pantalla = tk.Entry(
    ventana,
    font=("Arial", 19),
    justify="right",
    bd=5,
    width=1
)

pantalla.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=5,
    pady=5
)

# Ajustar las columnas
for columna in range(4):
    ventana.grid_columnconfigure(columna, weight=1)

# Funcion para realizar las operaciones
def click(valor):
    if valor == "C":
        pantalla.delete(0, tk.END)

    elif valor == "=":
        try:
            expresion = pantalla.get()

            # Validar caracteres permitidos
            permitidos = "0123456789+-*/(). "

            if not expresion or any(
                c not in permitidos for c in expresion
            ):
                raise ValueError("Expresion invalida")

            resultado = eval(
                expresion,
                {"__builtins__": {}},
                {}
            )

            if type(resultado) not in (int, float):
                raise ValueError("Resultado invalido")

            pantalla.delete(0, tk.END)
            pantalla.insert(0, str(resultado))

        except Exception:
            messagebox.showerror(
                "Error",
                "Expresion matematica invalida"
            )
            pantalla.delete(0, tk.END)

    else:
        pantalla.insert(tk.END, valor)


# Distribucion de los botones
botones = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# Crear los botones de la calculadora
for i, fila in enumerate(botones):
    for j, texto in enumerate(fila):
        btn = tk.Button(
            ventana,
            text=texto,
            font=("Arial", 18),
            height=2,
            command=lambda t=texto: click(t)
        )

        btn.grid(
            row=i+1,
            column=j,
            padx=2,
            pady=2,
            sticky="nsew"
        )

ventana.mainloop()
