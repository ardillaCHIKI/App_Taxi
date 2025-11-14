import tkinter as tk

root = tk.Tk()

root.title("Mi primera ventana")

root.geometry("400x300")

label = tk.Label(root, text="¡Hola, Mundo!")

label.pack()

root.mainloop()

