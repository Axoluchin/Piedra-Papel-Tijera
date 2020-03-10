from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import random

# 0 Piedra
# 1 Papel
# 2 Tijeras

puntosazul = 0
puntosrojos = 0

ventana = Tk()
ventana.geometry('760x600+390+160')
ventana.maxsize(760, 600)
ventana.minsize(760, 600)
ventana.title('Piedra Papel o Tijera    v1.0')
ventana.iconbitmap(r'Imagenes/Logo.ico')
ventana.configure(bg = '#3261a8')

def Ganar():
    AzulPuntos = azulscore.get(0)
    RojoPuntos = rojoscore.get(0)
    AzulPuntos = int(AzulPuntos)
    RojoPuntos = int(RojoPuntos)

    if AzulPuntos == 10:
        showinfo("Ganaste","El equipo Azul gana, Felicidades!!")
        azulscore.delete(0)
        rojoscore.delete(0)
        azulscore.insert(0,0)
        rojoscore.insert(0,0)   

    if RojoPuntos == 10:
        showinfo("Ganaste","El equipo Rojo gana, Felicidades!!")
        azulscore.delete(0)
        rojoscore.delete(0)
        azulscore.insert(0,0)
        rojoscore.insert(0,0)

def azulpi():
    AzulPuntos = azulscore.get(0)
    RojoPuntos = rojoscore.get(0)
    AzulPuntos = int(AzulPuntos)
    RojoPuntos = int(RojoPuntos)
    azulscore.delete(0)
    rojoscore.delete(0)
    z=random.randrange(3)
    y = 0

    if y == z :
        Resultado = "Empate"
    if (z==1):
        Resultado = "Perdiste"
        RojoPuntos += 1
    if (z==2):
        Resultado = "Ganaste"
        AzulPuntos +=1
    
    azulscore.insert(0,AzulPuntos)
    rojoscore.insert(0,RojoPuntos)
    showinfo('Resultados',Resultado)
    Ganar()

def azulpa():
    AzulPuntos = azulscore.get(0)
    RojoPuntos = rojoscore.get(0)
    AzulPuntos = int(AzulPuntos)
    RojoPuntos = int(RojoPuntos)
    azulscore.delete(0)
    rojoscore.delete(0)
    z=random.randrange(3)
    y = 1

    if y == z :
        Resultado = "Empate"
    if (z==2):
        Resultado = "Perdiste"
        RojoPuntos += 1
    if (z==0):
        Resultado = "Ganaste"
        AzulPuntos +=1
    
    azulscore.insert(0,AzulPuntos)
    rojoscore.insert(0,RojoPuntos)
    showinfo('Resultados',Resultado)
    Ganar()

def azulti():
    AzulPuntos = azulscore.get(0)
    RojoPuntos = rojoscore.get(0)
    AzulPuntos = int(AzulPuntos)
    RojoPuntos = int(RojoPuntos)
    azulscore.delete(0)
    rojoscore.delete(0)
    z=random.randrange(3)
    y = 2

    if y == z :
        Resultado = "Empate"
    if (z==0):
        Resultado = "Perdiste"
        RojoPuntos += 1
    if (z==1):
        Resultado = "Ganaste"
        AzulPuntos +=1
    
    azulscore.insert(0,AzulPuntos)
    rojoscore.insert(0,RojoPuntos)
    showinfo('Resultados',Resultado)
    Ganar()

def rojopi():
    AzulPuntos = azulscore.get(0)
    RojoPuntos = rojoscore.get(0)
    AzulPuntos = int(AzulPuntos)
    RojoPuntos = int(RojoPuntos)
    azulscore.delete(0)
    rojoscore.delete(0)
    z=random.randrange(3)
    y = 0

    if y == z :
        Resultado = "Empate"
    if (z==1):
        Resultado = "Perdiste"
        AzulPuntos +=1
    if (z==2):
        Resultado = "Ganaste"
        RojoPuntos += 1
    
    azulscore.insert(0,AzulPuntos)
    rojoscore.insert(0,RojoPuntos)
    showinfo('Resultados',Resultado)
    Ganar()

def rojopa():
    AzulPuntos = azulscore.get(0)
    RojoPuntos = rojoscore.get(0)
    AzulPuntos = int(AzulPuntos)
    RojoPuntos = int(RojoPuntos)
    azulscore.delete(0)
    rojoscore.delete(0)
    z=random.randrange(3)
    y = 1

    if y == z :
        Resultado = "Empate"
    if (z==2):
        Resultado = "Perdiste"
        AzulPuntos += 1
    if (z==0):
        Resultado = "Ganaste"
        RojoPuntos +=1
    
    azulscore.insert(0,AzulPuntos)
    rojoscore.insert(0,RojoPuntos)
    showinfo('Resultados',Resultado)
    Ganar()

def rojoti():
    AzulPuntos = azulscore.get(0)
    RojoPuntos = rojoscore.get(0)
    AzulPuntos = int(AzulPuntos)
    RojoPuntos = int(RojoPuntos)
    azulscore.delete(0)
    rojoscore.delete(0)
    z=random.randrange(3)
    y = 2

    if y == z :
        Resultado = "Empate"
    if (z==0):
        Resultado = "Perdiste"
        AzulPuntos +=1
    if (z==1):
        Resultado = "Ganaste"
        RojoPuntos += 1
    
    azulscore.insert(0,AzulPuntos)
    rojoscore.insert(0,RojoPuntos)
    showinfo('Resultados',Resultado)
    Ganar()

background_image=PhotoImage(file="Imagenes/fondo.png")
background_label = Label(ventana, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

nombre = askstring('Nombre', '¿Cuál es el nombre del equipo Azul?')
nombre2 = askstring('Rivel', '¿Cuál es el nombre del equipo Rojo?')
showinfo('Hola!', 'Bienvedidos, Diviertanse :D')

texto1 = Label(ventana,text = "Piedra, Papel o Tijeras",fg="white",bg= '#29b955')
texto1.grid(row=0,column=1,padx=0)
texto1.config(font=("arial",20,"bold"))

azul = Label(ventana,text = nombre,fg="white",bg= '#29b955')
azul.place(x=70,y=40)
azul.config(font=("arial",20,"bold"))

vs = Label(ventana,text = "vs",fg="white",bg= '#29b955')
vs.grid(row=2,column=1,padx=30)
vs.config(font=("arial",20,"bold"))

rojo = Label(ventana,text = nombre2,fg="white",bg= '#29b955')
rojo.place(x=590, y=40)
rojo.config(font=("arial",20,"bold"))

azulscore = Listbox (ventana, height=1,width=2, background="#29b955",font=("ARLRDBD",20), bd = 0,fg="white",selectbackground="#29b955",highlightcolor="#29b955")
azulscore.grid(row=3,column=0)
azulscore.insert(END, 0)

rojoscore = Listbox (ventana, height=1,width=2, background="#29b955",font=("ARLRDBD",20),bd = 0, fg="white",selectbackground="#29b955",highlightcolor="#29b955")
rojoscore.grid(row=3,column=2,padx=0)
rojoscore.insert(END, 0)

iazulpiedra = PhotoImage(file="Imagenes/AzulPiedra.png")
azulpiedra = Button(ventana,image=iazulpiedra,width=104, height=145,bd=0,bg='#29b955',activebackground="#29b955",command=azulpi)
azulpiedra.grid(row=4, column=0,sticky=W,padx=60)

iazultijera = PhotoImage(file="Imagenes/AzulTijeras.png")
azultijera = Button(ventana,image=iazultijera,width=104, height=145,bd=0,bg='#29b955',activebackground="#29b955",command=azulti)
azultijera.grid(row=5, column=0,sticky=W,padx=20)

iazulpapel = PhotoImage(file="Imagenes/AzulPapel.png")
azulpapel = Button(ventana,image=iazulpapel,width=104, height=145,bd=0,bg='#29b955',activebackground="#29b955",command=azulpa)
azulpapel.grid(row=6, column=0,sticky=W,padx=60)

irojopiedra = PhotoImage(file="Imagenes/RojoPiedra.png")
rojopiedra = Button(ventana,image=irojopiedra,width=104, height=145,bd=0,bg='#29b955',activebackground="#29b955",command=rojoti)
rojopiedra.grid(row=4, column=2,sticky=W,padx=60)

irojotijera = PhotoImage(file="Imagenes/RojoTijeras.png")
rojotijera = Button(ventana,image=irojotijera,width=104, height=145,bd=0,bg='#29b955',activebackground="#29b955",command=rojoti)
rojotijera.grid(row=5, column=2,sticky=W,padx=100)

irojopapel = PhotoImage(file="Imagenes/RojoPapel.png")
rojopapel = Button(ventana,image=irojopapel,width=104, height=145,bd=0,bg='#29b955',activebackground="#29b955",command=rojoti)
rojopapel.grid(row=6, column=2,sticky=W,padx=60)


ventana.mainloop()