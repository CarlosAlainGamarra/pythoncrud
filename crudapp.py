from tkinter import *
from tkinter import messagebox
import sqlite3

#--------------------FUNCIONES--------------------------

def conexionBBDD():
    miConexion=sqlite3.connect("USUARIOS")

    miCursor=miConexion.cursor()

    try:

        miCursor.execute('''
            CREATE TABLE DATOS_USUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(200),
                COMENTARIOS VARCHAR(500)
            )
        ''')

        messagebox.showinfo("BBDD", "Base de datos creada con éxito")

    except:

        messagebox.showwarning("¡Atención!", "La base de datos ya existe")

def salir():
    valor=messagebox.askquestion("Salir", "¿Quieres salir?")

    if(valor=="yes"):
        root.destroy()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    textoComentario.delete("1.0", END)


def crear():
    miConexion=sqlite3.connect("USUARIOS")

    miCursor=miConexion.cursor()
    """miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '"+ miNombre.get() + 
    "','" + miPass.get() +
    "','" + miApellido.get()+ 
    "','" + miDireccion.get()+
    "','" + textoComentario.get("1.0", END)+"') ")"""

    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)

    miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)", (datos))

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con éxito")


def leer():
    miConexion=sqlite3.connect("USUARIOS")

    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + miId.get())

    elUsuario=miCursor.fetchall()

    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert("1.0", usuario[5])

    miConexion.commit()



def actualizar():
    miConexion=sqlite3.connect("USUARIOS")

    miCursor=miConexion.cursor()
    miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE='" + miNombre.get() + 
    "', PASSWORD='" + miPass.get() +
    "', APELLIDO='" + miApellido.get() + 
    "', DIRECCION='" + miDireccion.get()+
    "', COMENTARIOS='" + textoComentario.get("1.0", END)+
    "' WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con éxito")


def eliminar():
    miConexion=sqlite3.connect("USUARIOS")

    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro borrado con éxito")

#---------------------------------------------------------



root=Tk()

#-----------------------MENU-----------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salir)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")


barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="BORRAR", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="AYUDA", menu=ayudaMenu)


#--------------------CAMPOS-----------------------------

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=15)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

#------------------------LABELS---------------------

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Pass:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#------------------------BOTONES------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)


root.mainloop()
