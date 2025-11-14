import tkinter as tk

root = tk.Tk()
# título de la ventana */
root.title("Mi primera ventana")
# tamaño de la ventana */
root.geometry("400x300")
# evitar que la ventana se pueda redimensionar (width, height) */
root.resizable(False, False)
# establecer un icono para la ventana */
root.iconbitmap("Taxi_Right_Yellow_26335.ico")



# crear un label con el texto "¡Hola, Mundo!" */
label = tk.Label(root, text="¡Hola, Mundo!")
# mostrar el label en la ventana */
label.pack()









#la ventana tiene que estar a la escucha tiene que estar en un bucle infinito */
#debe estar siempre al final del código /
root.mainloop()

