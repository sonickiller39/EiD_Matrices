import customtkinter as ctk
from tkinter import messagebox
import ast

class CalculadoraMatrices(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Matrices")
        self.geometry("500x700")  
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

        self.text_pasos = ctk.CTkTextbox(frame_operaciones, height=150, width=400, fg_color="#ffffff", 
                                         text_color="#343a40", border_color="#d1d1d1")
        self.text_pasos.pack(pady=10)

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
            
            pasos = "Pasos para la suma de matrices:\n"
            pasos += f"Matriz A:\n{self.formatear_matriz(A)}\n"
            pasos += f"Matriz B:\n{self.formatear_matriz(B)}\n"
            pasos += "Suma elemento por elemento:\n"
            for i in range(len(A)):
                for j in range(len(A[0])):
                    pasos += f"Posición [{i+1},{j+1}]: {A[i][j]} + {B[i][j]} = {resultado[i][j]}\n"
            pasos += f"Resultado:\n{self.formatear_matriz(resultado)}"
            
            self.text_pasos.delete("1.0", "end")
            self.text_pasos.insert("1.0", pasos)
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
            
            pasos = "Pasos para la resta de matrices:\n"
            pasos += f"Matriz A:\n{self.formatear_matriz(A)}\n"
            pasos += f"Matriz B:\n{self.formatear_matriz(B)}\n"
            pasos += "Resta elemento por elemento:\n"
            for i in range(len(A)):
                for j in range(len(A[0])):
                    pasos += f"Posición [{i+1},{j+1}]: {A[i][j]} - {B[i][j]} = {resultado[i][j]}\n"
            pasos += f"Resultado:\n{self.formatear_matriz(resultado)}"
            
            self.text_pasos.delete("1.0", "end")
            self.text_pasos.insert("1.0", pasos)
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
            
            pasos = "Pasos para la multiplicación de matrices:\n"
            pasos += f"Matriz A ({len(A)}x{len(A[0])}):\n{self.formatear_matriz(A)}\n"
            pasos += f"Matriz B ({len(B)}x{len(B[0])}):\n{self.formatear_matriz(B)}\n"
            pasos += "Cálculo de cada elemento de la matriz resultante:\n"
            for i in range(len(A)):
                for j in range(len(B[0])):
                    calculo = f"Posición [{i+1},{j+1}]: "
                    terms = [f"({A[i][k]} × {B[k][j]})" for k in range(len(B))]
                    calculo += " + ".join(terms) + f" = {resultado[i][j]}\n"
                    pasos += calculo
            pasos += f"Resultado:\n{self.formatear_matriz(resultado)}"
            
            self.text_pasos.delete("1.0", "end")
            self.text_pasos.insert("1.0", pasos)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_determinante(self):
        try:
            A = self.leer_matriz(self.entry_matriz_a.get())
            det, pasos = self.determinante_con_pasos(A)
            self.label_resultado.configure(text=f"Determinante: {round(det, 2)}")
            
            self.text_pasos.delete("1.0", "end")
            self.text_pasos.insert("1.0", pasos)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_inversa(self):
        try:
            A = self.leer_matriz(self.entry_matriz_a.get())
            inv, pasos = self.inversa_con_pasos(A)
            self.label_resultado.configure(text=f"Inversa:\n{self.formatear_matriz(inv)}")
            
            self.text_pasos.delete("1.0", "end")
            self.text_pasos.insert("1.0", pasos)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def matriz_menor(self, M, i, j):
        return [fila[:j] + fila[j+1:] for k, fila in enumerate(M) if k != i]

    def determinante_con_pasos(self, M):
        pasos = "Pasos para calcular el determinante:\n"
        pasos += f"Matriz A:\n{self.formatear_matriz(M)}\n"
        n = len(M)
        if n != len(M[0]):
            raise ValueError("La matriz debe ser cuadrada")
        if n == 1:
            pasos += f"Matriz 1x1: det = {M[0][0]}\n"
            return M[0][0], pasos
        if n == 2:
            det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
            pasos += "Para una matriz 2x2, det = (a*d - b*c):\n"
            pasos += f"({M[0][0]} × {M[1][1]}) - ({M[0][1]} × {M[1][0]}) = {M[0][0] * M[1][1]} - {M[0][1] * M[1][0]} = {det}\n"
            return det, pasos
        det = 0
        pasos += f"Usando expansión por cofactores a lo largo de la primera fila ({n}x{n}):\n"
        pasos += "det = Σ ((-1)^(1+j) × a[1,j] × det(Menor[1,j]))\n"

        for j in range(n):
            cofactor = ((-1) ** (1 + j)) * M[0][j]
            menor = self.matriz_menor(M, 0, j)
            sub_det, sub_pasos = self.determinante_con_pasos(menor)
            det += cofactor * sub_det
            pasos += f"\nCofactor en posición [1,{j+1}]: (-1)^(1+{j+1}) × {M[0][j]} × det(Menor[1,{j+1}])\n"
            pasos += f"Menor[1,{j+1}]:\n{self.formatear_matriz(menor)}\n"
            pasos += f"Determinante del menor:\n{sub_pasos}\n"
            pasos += f"= {(-1) ** (1 + j)} × {M[0][j]} × {sub_det} = {cofactor * sub_det}\n"

        pasos += f"Suma de cofactores: {det}\n"
        pasos += f"Determinante final: {det}\n"
        return det, pasos

    def inversa_con_pasos(self, M):
        pasos = "Pasos para calcular la inversa de la matriz:\n"
        pasos += f"Matriz A:\n{self.formatear_matriz(M)}\n"
        n = len(M)
        if n != len(M[0]):
            raise ValueError("La matriz debe ser cuadrada")

        det, det_pasos = self.determinante_con_pasos(M)
        pasos += "Paso 1: Calcular el determinante\n"
        pasos += det_pasos + "\n"
        
        if det == 0:
            raise ValueError("La matriz no tiene inversa (determinante = 0)")

        pasos += "Paso 2: Calcular la matriz de cofactores\n"
        cofactores = []
        for i in range(n):
            fila_cofactores = []
            for j in range(n):
                menor = self.matriz_menor(M, i, j)
                sub_det, _ = self.determinante_con_pasos(menor)
                cofactor = ((-1) ** (i + j)) * sub_det
                fila_cofactores.append(cofactor)
                pasos += f"Cofactor C[{i+1},{j+1}]: (-1)^({i+1}+{j+1}) × det(Menor[{i+1},{j+1}]) = {(-1) ** (i + j)} × {sub_det} = {cofactor}\n"
            cofactores.append(fila_cofactores)
        
        pasos += f"Matriz de cofactores:\n{self.formatear_matriz(cofactores)}\n"

        pasos += "Paso 3: Transponer la matriz de cofactores para obtener la adjunta\n"
        adjunta = [[cofactores[j][i] for j in range(n)] for i in range(n)]
        pasos += f"Matriz adjunta:\n{self.formatear_matriz(adjunta)}\n"

        pasos += f"Paso 4: Dividir la matriz adjunta por el determinante ({det})\n"
        inversa = [[adjunta[i][j] / det for j in range(n)] for i in range(n)]
        pasos += f"Matriz inversa:\n{self.formatear_matriz(inversa)}\n"

        return inversa, pasos

if __name__ == "__main__":
    app = CalculadoraMatrices()
    app.mainloop()