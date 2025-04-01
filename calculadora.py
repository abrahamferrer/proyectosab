import tkinter as tk
# importamos la clase tkinter

ventana = tk.Tk()
#titulo
ventana.title("Calculadora")

#icono
ruta_icono="C:/Users/abrah/OneDrive - White Rabbit Capital/Documentos/cursopython/5 proyectos python/calculadora/calculadora.ico"
ventana.iconbitmap(ruta_icono)  # Cambiar icono de la ventana

#variable para almacenar expresion atematica
expresion = ""

#variable para almacenar resultado
resultado_mostrado = False

#crear funsion para actalizar el visor
def pulsar_tecla(tecla):
    global expresion,resultado_mostrado
    #si el resultado esta mostrado limpiar el visor
    if resultado_mostrado:
        #evaluar si se presiona un numero o un operador
        if tecla.isdigit() or tecla ==".":
            expresion = str(tecla)
        else:
            expresion += str(tecla)
            resultado_mostrado = False
    else:
        expresion += str(tecla)
    visor_texto.set(expresion)

#crear funcion para evaluar la expresion
def evaluar():
    global expresion, resultado_mostrado
    try:
        resultado = eval(expresion)
        #quitar decimales si es entero
        if resultado==int(resultado):
            resultado=int(resultado)

        visor_texto.set (str(resultado))
        expresion = (str(resultado))
        resultado_mostrado = True
    except:
        visor_texto.set("Calcula Mejor! Esta mal la expresion")
        resultado_mostrado = False

#limpiar pantalla
def limpiar_pantalla():
    global expresion
    expresion = ""
    resultado_mostrado = False
    visor_texto.set(expresion)

#dimensiones
ventana.minsize(400, 600),ventana.maxsize(800, 1200), ventana.resizable(0, 0)  

# No se puede cambiar el tamaño de la ventana

for i in range(5):
    ventana.rowconfigure(i, weight=1)
for i in range(4):
    ventana.columnconfigure(i, weight=1)

#Visor
visor_texto = tk.StringVar()
visor = tk.Entry(ventana, 
              font=("DS-DIGI", 20), 
              bd=10,
              insertwidth=4,
              bg="powder blue",
              textvariable=visor_texto, 
              width=20,
              borderwidth=2, 
              justify="right")

visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#crear botones con una tupla en una lista
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3)
]


#crear y posicionar los botones
for (texto, fila, columna) in botones:
    if texto == "C":
        comando = limpiar_pantalla
    else: comando = lambda x=texto: pulsar_tecla(x)

    boton = tk.Button(ventana, text=texto,command=comando,
     font=("DS-DIGI", 20), width=4, height=2)
    boton.grid(row=fila, column=columna, padx=5, pady=5)
#boton igual
for (texto, fila, columna) in botones:
    boton_igual = tk.Button(ventana,text="=", padx=20,command=evaluar, pady=20, font=("DS-DIGI", 20))
    boton_igual.grid(
    row=5,column=0, columnspan=4, sticky="nsew"
    ) 
    



ventana.mainloop()

