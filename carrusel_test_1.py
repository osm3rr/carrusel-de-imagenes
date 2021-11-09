#****** Carrusel de imagenes *******

# Muestra las imagenes disponibles en
# una dirección específica, con las 
# facilidades para ir hacia adelante
# y hacia atrás en el carrusel.

# Librerías necesarias
from tkinter import *

# para el trabajo con imágenes
from PIL import ImageTk, Image

# principal window
window = Tk()

window.title('Carrusel')

#--- Carga de las imagenes --
# revisar que primero se abre y 
# luego se pasa a tipo foto.
img1 = ImageTk.PhotoImage( Image.open('images/1.jpg') )
img2 = ImageTk.PhotoImage( Image.open('images/2.jpg') )
img3 = ImageTk.PhotoImage( Image.open('images/3.png') )

# Creamos una lista con las imagenes creadas
image_list = [ img1, img2, img3]

#-- Etiquetas con las imagene
lbl_img = Label(window, image=img1)
# la imagen tomará las 3 columnas
lbl_img.grid( row=0, column=0,columnspan=3 )

#--- Creamos las funciones: aelante y atrás---
def adelante(img_num):
    
    global lbl_img
    global btn_atras
    global btn_adelante
    
    # indicamos que la imagen debe olvidar lo que 
    # tenia
    lbl_img.grid_forget()
    
    # se asigna el nuevo valor que tendrá
    # la imagen
    lbl_img = Label( window, image= image_list[ img_num ] )
    
    btn_atras = Button( window, text= '<-',
                       command= lambda: atras( img_num -1 ))
    
    btn_adelante = Button( window, text= '->',
                   command= lambda: adelante( img_num + 1 ))
    
    # Validación para evitar avanzar
    # cuando no hay imagene
    if img_num == 2:
        
        btn_adelante = Button( window, text= 'N/A', state= DISABLED)
    
    lbl_img.grid( row=0, column=0, columnspan=3 )
    
    btn_atras.grid( row=1, column=0 )
    btn_adelante.grid( row=1, column=2 )

# atras
def atras(img_num):
    global lbl_img
    global btn_atras
    global btn_adelante
    
    # indicamos que la imagen debe olvidar lo que 
    # tenia
    lbl_img.grid_forget()

    # se asigna el nuevo valor que tendrá
    # la imagen
    lbl_img = Label( window, image= image_list[ img_num ] )

    btn_atras = Button( window, text= '<-',
                       command= lambda: atras( img_num -1 ))

    btn_adelante = Button( window, text= '->',
                   command= lambda: adelante( img_num + 1 ))

    # Validación para evitar avanzar
    # cuando no hay imagene
    if img_num == 0:

        btn_atras = Button( window, text= 'N/A', state= DISABLED)

    lbl_img.grid( row=0, column=0, columnspan=3 )

    btn_atras.grid( row=1, column=0 )
    btn_adelante.grid( row=1, column=2 )


    
#--- agregamos los botones ---
# atras
btn_atras = Button( window, text= 'N/A', state=DISABLED) 
btn_atras.grid( row=1, column=0 )

#adelante
btn_adelante = Button( window, text= '->', command= lambda: adelante(1) )
btn_adelante.grid( row=1, column=2 )


window.mainloop()
