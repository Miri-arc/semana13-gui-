
import tkinter as tk
from tkinter import messagebox
import re


class FormularioRegistro:
    def __init__(self):
        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("Registro de Usuario")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Variables del formulario
        self.nombre = tk.StringVar()
        self.email = tk.StringVar()
        self.celular = tk.StringVar()
        self.password = tk.StringVar()
        self.confirm_pass = tk.StringVar()
        self.edad = tk.StringVar()
        self.genero = tk.StringVar(value="Sin seleccionar")
        self.acepto = tk.BooleanVar(value=False)

        # Crear los elementos del formulario
        self.crear_widgets()

    def crear_widgets(self):
        # Contenedor principal
        frame = tk.Frame(
            self.root,
            padx=20,
            pady=20
        )
        frame.pack(fill="both", expand=True)

        # Titulo del formulario
        tk.Label(
            frame,
            text="Registro de Usuario",
            font=("Arial", 16, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0, 15)
        )

        # Campos de texto
        campos = [
            ("Nombre completo:", self.nombre, False),
            ("Email:", self.email, False),
            ("Celular:", self.celular, False),
            ("Contraseña:", self.password, True),
            ("Confirmar contraseña:", self.confirm_pass, True),
            ("Edad:", self.edad, False)
        ]

        # Crear etiquetas y entradas
        for i, (label, var, oculto) in enumerate(campos):
            tk.Label(
                frame,
                text=label,
                anchor="e"
            ).grid(
                row=i + 1,
                column=0,
                sticky="e",
                pady=5,
                padx=(0, 10)
            )

            entry = tk.Entry(
                frame,
                textvariable=var,
                width=30,
                show="*" if oculto else ""
            )

            entry.grid(
                row=i + 1,
                column=1,
                pady=5,
                sticky="w"
            )

        # Seleccion de genero
        tk.Label(
            frame,
            text="Genero:"
        ).grid(
            row=7,
            column=0,
            sticky="e",
            pady=5
        )

        genero_frame = tk.Frame(frame)
        genero_frame.grid(
            row=7,
            column=1,
            sticky="w"
        )

        for opcion in ["Masculino", "Femenino", "Otro"]:
            tk.Radiobutton(
                genero_frame,
                text=opcion,
                variable=self.genero,
                value=opcion
            ).pack(side="left", padx=3)

        # Casilla de terminos y condiciones
        tk.Checkbutton(
            frame,
            text="Acepto los terminos y condiciones",
            variable=self.acepto
        ).grid(
            row=8,
            column=0,
            columnspan=2,
            pady=10
        )

        # Contenedor de botones
        btn_frame = tk.Frame(frame)
        btn_frame.grid(
            row=9,
            column=0,
            columnspan=2,
            pady=15
        )

        # Boton Registrar
        tk.Button(
            btn_frame,
            text="Registrar",
            command=self.validar,
            width=15,
            bg="#4CAF50",
            fg="white"
        ).pack(side="left", padx=10)

        # Boton Limpiar
        tk.Button(
            btn_frame,
            text="Limpiar",
            command=self.limpiar,
            width=15
        ).pack(side="left", padx=10)

    # Validaciones del formulario
    def validar(self):
        errores = []

        # Validar nombre
        if not self.nombre.get().strip():
            errores.append(
                "El nombre es obligatorio"
            )

        # Validar correo electronico
        email = self.email.get().strip()

        if not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+", email
        ):
            errores.append(
                "Email invalido (debe contener @ y dominio)"
            )

        # Validar celular 
        celular = self.celular.get().strip()

        if not re.fullmatch(r"9\d{8}", celular):
            errores.append(
                "El celular debe tener 9 digitos y empezar con 9"
            )

        # Validar contraseña
        if len(self.password.get()) < 8:
            errores.append(
                "La contraseña debe tener minimo 8 caracteres"
            )

        # Confirmar contraseña
        if self.password.get() != self.confirm_pass.get():
            errores.append(
                "Las contraseñas no coinciden"
            )

        # Validar edad
        try:
            edad = int(self.edad.get())

            if edad < 15 or edad > 99:
                errores.append(
                    "La edad debe estar entre 15 y 99"
                )

        except ValueError:
            errores.append(
                "La edad debe ser un numero"
            )

        # Validar genero
        if self.genero.get() == "Sin seleccionar":
            errores.append(
                "Seleccione un genero"
            )

        # Validar terminos
        if not self.acepto.get():
            errores.append(
                "Debe aceptar los terminos"
            )

        # Mostrar errores o registro exitoso
        if errores:
            messagebox.showerror(
                "Errores de validacion",
                "\n".join(errores)
            )
        else:
            messagebox.showinfo(
                "Registro exitoso",
                f"¡Bienvenido {self.nombre.get()}!\n"
                f"Email: {self.email.get()}\n"
                f"Celular: {self.celular.get()}"
            )

    # Limpiar todos los campos
    def limpiar(self):
        self.nombre.set("")
        self.email.set("")
        self.celular.set("")
        self.password.set("")
        self.confirm_pass.set("")
        self.edad.set("")
        self.genero.set("Sin seleccionar")
        self.acepto.set(False)


# Ejecutar el formulario
if __name__ == "__main__":
    app = FormularioRegistro()
    app.root.mainloop()
