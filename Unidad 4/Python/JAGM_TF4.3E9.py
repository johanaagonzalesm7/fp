from tkinter import *
from math import *

def btnClik(num):
	global operador
	operador=operador+str(num)
	input_text.set(operador)

def resultado():
	global operador
	try:
		opera=str(eval(operador))
		input_text.set(opera)
	except:
		input_text.set("Error")
		operador = ""

def clear():
	global operador
	operador=("")
	input_text.set("0")

ventana=Tk()
ventana.title("calculadora")
ventana.geometry("392*600")
ventana.configure(backgroud='SkyBlue4')
color.boton=("gray77")

ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""

Salida=Entry(ventana,font=('arial',20,'bold')widch=22,textvariable=input_text,bd=20,
	insetwidth=4,bg='powder blue',justify='right')
Salida.place(x=10,y=60)

button(ventana,text='o',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=180)
button(ventana,text='1',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=107,y=180)
button(ventana,text='2',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=197,y=180)
button(ventana,text='3',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=287,y=180)
button(ventana,text='4',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=240)
button(ventana,text='5',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=180)
button(ventana,text='6',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=180)
button(ventana,text='7',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=287,y=180)
button(ventana,text='8',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=17,y=300)
button(ventana,text='9',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=107,y=300)
button(ventana,text='π',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('pi')).place(x=197,y=300)
button(ventana,text=',',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(',')).place(x=287,y=300)
button(ventana,text='+',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('+')).place(x=17,y=360)
button(ventana,text='-',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('-')).place(x=107,y=360)
button(ventana,text='*',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('*')).place(x=197,y=360)
button(ventana,text='/',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('/')).place(x=287,y=360)
button(ventana,text='√',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('sqrt(')).place(x=17,y=420)
button(ventana,text='(',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('(')).place(x=107,y=480)
button(ventana,text=')',widch=ancho_boton,height=alto_boton,command=lambda:btnClik(')')).place(x=107,y=480)
button(ventana,text='%',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('%')).place(x=197,y=480)
button(ventana,text='In',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('long(')).place(x=287,y=180)
button(ventana,text='C',widch=ancho_boton,height=alto_boton).place(x=107,y=420)
button(ventana,text='EXP',widch=ancho_boton,height=alto_boton,command=lambda:btnClik('**')).place(x=197,y=420)
button(ventana,text='=',widch=ancho_boton,height=alto_boton).place(x=287,y=420)


clar()
ventana.mainloop()