
from tkinter import *

root = Tk()

miFrame = Frame(root, width=800, height=600)
miFrame.pack()

#miImagen = PhotoImage(file="pikachu.png")
miImagen = PhotoImage(file="/Users/belensoto/Documents/GitHub/App_Taxi/Prueba/pikachu.png")
Label(miFrame, image=miImagen).place(x=10, y=10)

# Crear un label dentro del frame */
miLabel = Label(miFrame, text="Hola, soy un label dentro de un Frame", fg="blue", font=("Arial", 20))
miLabel.place(x=50, y=200)
# otra forma simplificada. */
# Label(miFrame, text="Hola, soy un label2 dentro de un Frame", fg="red", font("Comic Sans MS", 18)).place(x=100, y=300)
Label(miFrame, text="Hola, soy un label3 dentro de un Frame", fg="red", font=("karate", 25)).place(x=100, y=300)

root.mainloop()