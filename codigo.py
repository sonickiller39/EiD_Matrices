import customtkinter as ctk
from tkinter import messagebox
import ast

class CalculadoraMatrices(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Matrices")
        self.geometry("500x600")
        self.configure(fg_color="#f5f5f5")
        self.iconbitmap("logo.ico")
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

    def leer_matriz(self, texto_matriz):
        try:
            matrix = ast.literal_eval(texto_matriz)
            if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
                raise ValueError("Debe ser una lista de listas")
            if not all(len(row) == len(matrix[0]) for row in matrix):
                raise ValueError("Todas las filas deben tener la misma longitud")
            return [[float(val) for val in row] for row in matrix]
        except Exception:
            raise ValueError("Formato de matriz inválido. Usa: [[1,2],[3,4]]")

    def formatear_matriz(self, matriz):
        filas = []
        for fila in matriz:
            fila_formateada = "  ".join(
                f"{val:.2f}".rstrip('0').rstrip('.') if isinstance(val, float) else str(val)
                for val in fila
            )
            filas.append(f"[ {fila_formateada} ]")
        return "\n".join(filas)

    def calcular_suma(self):
        try:
            A = self.leer_matriz(self.entry_matriz_a.get())
            B = self.leer_matriz(self.entry_matriz_b.get())
            if len(A) != len(B) or len(A[0]) != len(B[0]):
                raise ValueError("Las matrices deben tener la misma dimensión")
            resultado = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
            self.label_resultado.configure(text=f"Suma:\n{self.formatear_matriz(resultado)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_resta(self):
        try:
            A = self.leer_matriz(self.entry_matriz_a.get())
            B = self.leer_matriz(self.entry_matriz_b.get())
            if len(A) != len(B) or len(A[0]) != len(B[0]):
                raise ValueError("Las matrices deben tener la misma dimensión")
            resultado = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
            self.label_resultado.configure(text=f"Resta:\n{self.formatear_matriz(resultado)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_multiplicacion(self):
        try:
            A = self.leer_matriz(self.entry_matriz_a.get())
            B = self.leer_matriz(self.entry_matriz_b.get())
            if len(A[0]) != len(B):
                raise ValueError("El número de columnas de A debe igualar el número de filas de B")
            resultado = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
            self.label_resultado.configure(text=f"Multiplicación:\n{self.formatear_matriz(resultado)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_determinante(self):
        try:
            A = self.leer_matriz(self.entry_matriz_a.get())
            det = self.determinante(A)
            self.label_resultado.configure(text=f"Determinante: {round(det, 2)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_inversa(self):
        try:
            A = self.leer_matriz(self.entry_matriz_a.get())
            inv = self.inversa(A)
            self.label_resultado.configure(text=f"Inversa:\n{self.formatear_matriz(inv)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def determinante(self, M):
        if len(M) != len(M[0]):
            raise ValueError("La matriz debe ser cuadrada")
        n = len(M)
        if n == 1:
            return M[0][0]
        if n == 2:
            return M[0][0]*M[1][1] - M[0][1]*M[1][0]
        det = 0
        for c in range(n):
            menor = self.matriz_menor(M, 0, c)
            det += ((-1) ** c) * M[0][c] * self.determinante(menor)
        return det

    def matriz_menor(self, M, i, j):
        return [fila[:j] + fila[j+1:] for k, fila in enumerate(M) if k != i]

    def inversa(self, M):
        if len(M) != len(M[0]):
            raise ValueError("La matriz debe ser cuadrada")
        det = self.determinante(M)
        if det == 0:
            raise ValueError("La matriz no es invertible")

        n = len(M)
        cofactores = []
        for i in range(n):
            fila = []
            for j in range(n):
                menor = self.matriz_menor(M, i, j)
                signo = (-1) ** (i + j)
                fila.append(signo * self.determinante(menor))
            cofactores.append(fila)

        cofactores_T = list(map(list, zip(*cofactores)))
        inversa = [[cofactores_T[i][j] / det for j in range(n)] for i in range(n)]
        return inversa

if __name__ == "__main__":
    app = CalculadoraMatrices()
    app.mainloop()
