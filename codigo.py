import customtkinter as ctk
from tkinter import messagebox

class CalculadoraMatematica(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Matemática")
        self.geometry("500x600")
        self.configure(fg_color="#f5f5f5")  
        self.iconbitmap("logo.ico")
        self.resizable(False, False)
        self.crear_frame_progresion()
        self.crear_frame_binomio()
        btn_salir = ctk.CTkButton(self, text="Salir", command=self.destroy, fg_color="#e63946", hover_color="#d62828", 
                                text_color="#ffffff")
        btn_salir.pack(pady=20)

    def crear_frame_progresion(self):
        frame_progresion = ctk.CTkFrame(self, fg_color="#cce7ff")  
        frame_progresion.pack(pady=10, padx=20, fill="both", expand=True)

        label_progresion = ctk.CTkLabel(frame_progresion, text="Progresión Aritmética", font=("Arial", 16), 
                                        text_color="#005A9E")
        label_progresion.pack(pady=10)

        self.entry_a1 = ctk.CTkEntry(frame_progresion, placeholder_text="Primer término (a1)", fg_color="#ffffff", 
                                    border_color="#d1d1d1", placeholder_text_color="#6c757d", text_color="gray")
        self.entry_a1.pack(pady=5)

        self.entry_d = ctk.CTkEntry(frame_progresion, placeholder_text="Diferencia común (d)", fg_color="#ffffff", border_color="#d1d1d1", 
                                    placeholder_text_color="#6c757d", text_color="gray")
        self.entry_d.pack(pady=5)

        self.entry_n = ctk.CTkEntry(frame_progresion, placeholder_text="Número del término (n)", fg_color="#ffffff", 
                                    border_color="#d1d1d1", placeholder_text_color="#6c757d", text_color="gray")
        self.entry_n.pack(pady=5)

        btn_calcular_termino = ctk.CTkButton(frame_progresion, text="Calcular término n-ésimo", command=self.calcular_termino_n,
                                            fg_color="#0078D7", hover_color="#005A9E", text_color="#ffffff")
        btn_calcular_termino.pack(pady=10)

        self.label_resultado_termino = ctk.CTkLabel(frame_progresion, text="", text_color="#343a40")
        self.label_resultado_termino.pack()

    def crear_frame_binomio(self):
        frame_binomio = ctk.CTkFrame(self, fg_color="#cce7ff")  
        frame_binomio.pack(pady=10, padx=20, fill="both", expand=True)

        label_binomio = ctk.CTkLabel(frame_binomio, text="Teorema del Binomio", font=("Arial", 16), text_color="#005A9E")
        label_binomio.pack(pady=10)

        self.entry_n_binomio = ctk.CTkEntry(frame_binomio, placeholder_text="Valor de n", fg_color="#ffffff", border_color="#d1d1d1", 
                                            placeholder_text_color="#6c757d", text_color="gray")
        self.entry_n_binomio.pack(pady=5)

        self.entry_x = ctk.CTkEntry(frame_binomio, placeholder_text="Valor de x", fg_color="#ffffff", border_color="#d1d1d1", 
                                    placeholder_text_color="#6c757d", text_color="gray")
        self.entry_x.pack(pady=5)

        self.entry_y = ctk.CTkEntry(frame_binomio, placeholder_text="Valor de y", fg_color="#ffffff", border_color="#d1d1d1", 
                                    placeholder_text_color="#6c757d", text_color="gray")
        self.entry_y.pack(pady=5)

        btn_calcular_binomio = ctk.CTkButton(frame_binomio, text="Calcular suma del binomio", command=self.calcular_suma_binomio,
                                            fg_color="#0078D7", hover_color="#005A9E", text_color="#ffffff")
        btn_calcular_binomio.pack(pady=10)

        self.label_resultado_binomio = ctk.CTkLabel(frame_binomio, text="", text_color="#343a40")
        self.label_resultado_binomio.pack()

    def calcular_termino_n(self):
        try:
            a1 = float(self.entry_a1.get())
            d = float(self.entry_d.get())
            n = int(self.entry_n.get())
            an = a1 + (n - 1) * d
            self.label_resultado_termino.configure(text=f"El término n-ésimo es: {an:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    def calcular_suma_binomio(self):
        try:
            n = int(self.entry_n_binomio.get())
            x = float(self.entry_x.get())
            y = float(self.entry_y.get())

            suma_binomio = (x + y) ** n
            suma_ciclo = 0
            for k in range(n + 1):
                coef_binomial = self.factorial(n) // (self.factorial(k) * self.factorial(n - k))
                suma_ciclo += coef_binomial * (x ** k) * (y ** (n - k))

            resultado = (
                f"Suma (teorema): {suma_binomio:.2f}\n"
                f"Suma (ciclo): {suma_ciclo:.2f}"
            )
            resultado += "\nLos resultados coinciden." if suma_binomio == suma_ciclo else "\nLos resultados no coinciden."
            self.label_resultado_binomio.configure(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    @staticmethod
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        return num * CalculadoraMatematica.factorial(num - 1)


if __name__ == "__main__":
    app = CalculadoraMatematica()
    app.mainloop()