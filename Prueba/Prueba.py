
# importar la librería tkinter */
# https://docs.python.org/es/3/library/tk.html */
import tkinter as tk

# ------- crear la ventana principal raiz */
root = tk.Tk()
# título de la ventana */
root.title("Mi primera ventana")
# tamaño de la ventana */
root.geometry("400x300")
# evitar que la ventana se pueda redimensionar (width, height) */
# root.resizable(False, False)
# establecer un icono para la ventana */
root.iconbitmap("/Users/belensoto/Documents/GitHub/App_Taxi/Prueba/Taxi.ico")
# establecer un color de fondo para la ventana */
root.configure(bg="blue")  


# crear un label con el texto "¡Hola, Mundo!" */
label = tk.Label(root, text="¡Hola, Mundo!")
# mostrar el label en la ventana */
label.pack()

# crear un frame */
miFrame=tk.Frame()
# mostrar el frame en la ventana */
miFrame.pack(side="left", anchor="n", padx=10, pady=10)
miFrame.config(bg="red")
miFrame.config(width="650", height="350")

miFrame.config(cursor="hand2")  # cambiar el cursor cuando está sobre el frame








#la ventana tiene que estar a la escucha tiene que estar en un bucle infinito */
#debe estar siempre al final del código /
root.mainloop()

