import customtkinter as ctk
from tkinter import messagebox
import numpy as np

class CalculadoraMatrices(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Matrices")
        self.geometry("500x600")
        self.configure(fg_color="#f5f5f5")
        self.resizable(False, False)
        self.crear_frame_entrada_matrices()
        self.crear_frame_operaciones()
        btn_salir = ctk.CTkButton(self, text="Salir", command=self.destroy, fg_color="#e63946", hover_color="#d62828", 
                                text_color="#ffffff")
        btn_salir.pack(pady=20)

    def crear_frame_entrada_matrices(self):
        frame_entrada = ctk.CTkFrame(self, fg_color="#cce7ff")
        frame_entrada.pack(pady=10, padx=20, fill="both", expand=True)

        label_entrada = ctk.CTkLabel(frame_entrada, text="Entrada de Matrices", font=("Arial", 16), 
                                    text_color="#005A9E")
        label_entrada.pack(pady=10)

        self.entry_matriz_a = ctk.CTkEntry(frame_entrada, placeholder_text="Matriz A (ej: [[1,2],[3,4]])", 
                                         fg_color="#ffffff", border_color="#d1d1d1", 
                                         placeholder_text_color="#6c757d", text_color="gray", width=300)
        self.entry_matriz_a.pack(pady=5)

        self.entry_matriz_b = ctk.CTkEntry(frame_entrada, placeholder_text="Matriz B (ej: [[5,6],[7,8]])", 
                                         fg_color="#ffffff", border_color="#d1d1d1", 
                                         placeholder_text_color="#6c757d", text_color="gray", width=300)
        self.entry_matriz_b.pack(pady=5)

    def crear_frame_operaciones(self):
        frame_operaciones = ctk.CTkFrame(self, fg_color="#cce7ff")
        frame_operaciones.pack(pady=10, padx=20, fill="both", expand=True)

        label_operaciones = ctk.CTkLabel(frame_operaciones, text="Operaciones con Matrices", font=("Arial", 16), 
                                       text_color="#005A9E")
        label_operaciones.pack(pady=10)

        btn_suma = ctk.CTkButton(frame_operaciones, text="Suma", command=self.calcular_suma,
                                fg_color="#0078D7", hover_color="#005A9E", text_color="#ffffff")
        btn_suma.pack(pady=5)

        btn_resta = ctk.CTkButton(frame_operaciones, text="Resta", command=self.calcular_resta,
                                 fg_color="#0078D7", hover_color="#005A9E", text_color="#ffffff")
        btn_resta.pack(pady=5)

        btn_multiplicacion = ctk.CTkButton(frame_operaciones, text="Multiplicación", command=self.calcular_multiplicacion,
                                         fg_color="#0078D7", hover_color="#005A9E", text_color="#ffffff")
        btn_multiplicacion.pack(pady=5)

        btn_inversa = ctk.CTkButton(frame_operaciones, text="Inversa (Matriz A)", command=self.calcular_inversa,
                                   fg_color="#0078D7", hover_color="#005A9E", text_color="#ffffff")
        btn_inversa.pack(pady=5)

        btn_determinante = ctk.CTkButton(frame_operaciones, text="Determinante (Matriz A)", command=self.calcular_determinante,
                                       fg_color="#0078D7", hover_color="#005A9E", text_color="#ffffff")
        btn_determinante.pack(pady=5)

        self.label_resultado = ctk.CTkLabel(frame_operaciones, text="", text_color="#343a40", wraplength=400)
        self.label_resultado.pack(pady=10)

    def parse_matrix(self, matrix_str):
        try:
            matrix = eval(matrix_str, {"__builtins__": None}, {"np": np})
            return np.array(matrix, dtype=float)
        except:
            raise ValueError("Formato de matriz inválido")

    def calcular_suma(self):
        try:
            matriz_a = self.parse_matrix(self.entry_matriz_a.get())
            matriz_b = self.parse_matrix(self.entry_matriz_b.get())
            if matriz_a.shape != matriz_b.shape:
                raise ValueError("Las matrices deben tener la misma dimensión")
            resultado = matriz_a + matriz_b
            self.label_resultado.configure(text=f"Suma:\n{np.array2string(resultado, precision=2)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_resta(self):
        try:
            matriz_a = self.parse_matrix(self.entry_matriz_a.get())
            matriz_b = self.parse_matrix(self.entry_matriz_b.get())
            if matriz_a.shape != matriz_b.shape:
                raise ValueError("Las matrices deben tener la misma dimensión")
            resultado = matriz_a - matriz_b
            self.label_resultado.configure(text=f"Resta:\n{np.array2string(resultado, precision=2)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_multiplicacion(self):
        try:
            matriz_a = self.parse_matrix(self.entry_matriz_a.get())
            matriz_b = self.parse_matrix(self.entry_matriz_b.get())
            if matriz_a.shape[1] != matriz_b.shape[0]:
                raise ValueError("El número de columnas de A debe igualar el número de filas de B")
            resultado = np.dot(matriz_a, matriz_b)
            self.label_resultado.configure(text=f"Multiplicación:\n{np.array2string(resultado, precision=2)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_inversa(self):
        try:
            matriz_a = self.parse_matrix(self.entry_matriz_a.get())
            if matriz_a.shape[0] != matriz_a.shape[1]:
                raise ValueError("La matriz debe ser cuadrada")
            if np.linalg.det(matriz_a) == 0:
                raise ValueError("La matriz no es invertible")
            resultado = np.linalg.inv(matriz_a)
            self.label_resultado.configure(text=f"Inversa:\n{np.array2string(resultado, precision=2)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_determinante(self):
        try:
            matriz_a = self.parse_matrix(self.entry_matriz_a.get())
            if matriz_a.shape[0] != matriz_a.shape[1]:
                raise ValueError("La matriz debe ser cuadrada")
            resultado = np.linalg.det(matriz_a)
            self.label_resultado.configure(text=f"Determinante: {resultado:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = CalculadoraMatrices()
    app.mainloop()