import tkinter as tk
import bases_datos_15 as bd

"""creamos una lista de strings con todos los numeros y simbolos que vamos a necesitar en nuestra calculadora."""
lista_botones = ["7","8","9","C",
                 "4","5","6","x",
                 "1","2","3","=",
                 "/","0","+","-"]

#creamo una lista vacia para los objetos botones que se iran almacenando al iniciar el programa.
lista_botones_visuales = []
#string donde se guardara la operacion.
operacion = ""

"""
esta funcion tiene la tarea de reconocer cada caracter para realizar la operacion que el usuario necesita.
"""
def presionar_boton(signo):
    global operacion
    #si el signo es "=" usamos una funcion eval() para resolver la operacion siempre que no haya una division por 0.
    if signo == "=":
        if "/0" in operacion:
            pantalla_calculadora.delete(0, tk.END)
            pantalla_calculadora.insert(0, "SYNTAX ERROR")
        else:
            try:
                #obtenemos el resultado de la operacion.
                resultado = eval(operacion)
                #guardamos la operacion y resultado en una tupla.
                valores = (operacion,str(resultado))
                #del modulo que creamos e importamos llamamos al objeto y el metodo insertar_datos().
                #le pasamos como parametro la tupla con los valores.
                bd.objeto.insertar_datos(valores)
                #borramos la pantalla.
                pantalla_calculadora.delete(0, tk.END)
                #y mostramos el resultado.
                pantalla_calculadora.insert(0, resultado)
                #reestablecemos el string de la operacion para que quede vacio.
                operacion = ""
            except:
                pantalla_calculadora.delete(0, tk.END)
                pantalla_calculadora.insert(0, "0")
    #borramos todos los elementos de la variable que se muestra en pantalla.        
    elif signo == "C":
        operacion = ""
        pantalla_calculadora.delete(0, tk.END)
    #sino concatenamos el signo pasado al final de la string.
    else:
        if signo == "x":
            signo = "*"
        operacion += signo
        pantalla_calculadora.delete(0, tk.END)
        pantalla_calculadora.insert(0, operacion)


#creamos la app con Tkinter.
app = tk.Tk()
#le ponemos un titulo a la ventana.
app.title("Calculadora")

#creamos la pantalla donde se mostraran los datos de las operaciones.
pantalla_calculadora = tk.Entry(app, font="arial 20",width=16*3)
#le damos una posicion.
pantalla_calculadora.grid(row=0,column=0,columnspan=5)


#inicializamos los valores de las filas y columnas para posicionar el resto de botones en la pantalla.
#iniciamos en la fila 1 ya que en la fila 0 esta el widget de entrada.
fila = 1
columna = 0
"""
este bucle for crea los botones les asigna un lugar y un valor y luego los coloca dentro de una lista.
se crea un boton por cada string dentro de la lista previamente creada con los valores que necesitamos en 
nuestra calculadora.
"""
for boton in lista_botones:
    #crea un boton que va a contener el numero o signo que le corresponde y utiliza una funcion lambda para enviar el parametro a la funcion que gestiona el contenido del boton.
    boton_funcion = tk.Button(app, text=boton, font="arial 16",width=16,command=lambda valor = boton: presionar_boton(valor))
    #agregamos el boton a la lista vacia de botones para luego mostrarlos.
    lista_botones_visuales.append(boton_funcion)
    #la lanzamos segun los valores de fila y columna del ciclo actual.
    boton_funcion.grid(row=fila,column=columna)
    #incrementamos los valores de filas y columnas dependiendo el ciclo en el que nos encontremos.
    columna+=1
    if columna == 4:
        columna = 0
        fila+=1
    else:
        pass




app.mainloop()
