import tkinter as tk
from tkinter import messagebox
import random

# Lista de palabras para adivinar
palabras = ["PYTHON", "PROGRAMAR", "AHORCADO", "JUEGO", "COMPUTADORA"]

# Seleccionar palabra aleatoria
palabra = random.choice(palabras)
palabra_oculta = ["_"] * len(palabra)
intentos = 6

# Función para actualizar la palabra mostrada
def actualizar_palabra():
    lbl_palabra.config(text=" ".join(palabra_oculta))

# Función que maneja las letras ingresadas
def probar_letra():
    global intentos
    letra = entry_letra.get().upper()
    entry_letra.delete(0, tk.END)

    if len(letra) != 1 or not letra.isalpha():
        messagebox.showwarning("Entrada inválida", "Introduce solo una letra.")
        return

    if letra in palabra:
        for i, l in enumerate(palabra):
            if l == letra:
                palabra_oculta[i] = letra
        actualizar_palabra()
        if "_" not in palabra_oculta:
            messagebox.showinfo("¡Ganaste!", f"Adivinaste la palabra: {palabra}")
            ventana.quit()
    else:
        intentos -= 1
        lbl_intentos.config(text=f"Intentos restantes: {intentos}")
        dibujar_ahorcado()
        if intentos == 0:
            messagebox.showinfo("Game Over", f"Perdiste. La palabra era: {palabra}")
            ventana.quit()

# Función para dibujar el ahorcado
def dibujar_ahorcado():
    lienzo.delete("all")
    # Base
    lienzo.create_line(20, 180, 180, 180, width=3)
    lienzo.create_line(50, 180, 50, 20, width=3)
    lienzo.create_line(50, 20, 120, 20, width=3)
    lienzo.create_line(120, 20, 120, 40, width=3)

    partes = 6 - intentos
    if partes > 0:
        # Cabeza
        lienzo.create_oval(100, 40, 140, 80, width=2)
    if partes > 1:
        # Cuerpo
        lienzo.create_line(120, 80, 120, 130, width=2)
    if partes > 2:
        # Brazo izquierdo
        lienzo.create_line(120, 90, 90, 110, width=2)
    if partes > 3:
        # Brazo derecho
        lienzo.create_line(120, 90, 150, 110, width=2)
    if partes > 4:
        # Pierna izquierda
        lienzo.create_line(120, 130, 90, 160, width=2)
    if partes > 5:
        # Pierna derecha
        lienzo.create_line(120, 130, 150, 160, width=2)

# Crear ventana
ventana = tk.Tk()
ventana.title("Juego del Ahorcado")

# Mostrar palabra oculta
lbl_palabra = tk.Label(ventana, text="", font=("Consolas", 24))
lbl_palabra.pack(pady=10)

# Entrada de letra
frame_entrada = tk.Frame(ventana)
frame_entrada.pack()

entry_letra = tk.Entry(frame_entrada, font=("Consolas", 14), width=5)
entry_letra.pack(side=tk.LEFT, padx=5)

btn_probar = tk.Button(frame_entrada, text="Probar letra", command=probar_letra)
btn_probar.pack(side=tk.LEFT)

# Intentos restantes
lbl_intentos = tk.Label(ventana, text=f"Intentos restantes: {intentos}", font=("Arial", 12))
lbl_intentos.pack()

# Lienzo para dibujar el ahorcado
lienzo = tk.Canvas(ventana, width=200, height=200, bg="white")
lienzo.pack(pady=10)

actualizar_palabra()
dibujar_ahorcado()

ventana.mainloop()
