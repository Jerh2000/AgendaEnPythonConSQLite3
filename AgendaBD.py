#AGENDA DE CONTACTOS: DESARROLLDA POR JAIRO ROJAS HERRERA
from tkinter import *
from tkinter import messagebox
import Contactos


class Agenda:
    def __init__(self):
        self.bg = "SeaGreen1"
        self.letraColor = "#FFF"
        self.numModificar = 0
        self.contacto = Contactos.Contacto()
        self.ventana = Tk()
        self.ventana.title("Agenda de contactos")
        self.ventana.geometry("700x500")
        self.ventana.configure(bg=self.bg)
        self.labelTitulo = Label(self.ventana, text="Agenda", bg=self.bg,fg=self.letraColor, font=("Verdana", 12)).place(x=270, y=10)
        
        
        self.nombre = StringVar()
        self.labelNombre = Label(self.ventana, text="Nombre:", bg=self.bg,fg=self.letraColor, font=("Verdana", 12)).place(x=50, y=50)
        self.inputNombre = Entry(self.ventana, textvariable=self.nombre).place(x=200, y=50)

        self.apellidoP = StringVar()
        self.labelApp = Label(self.ventana, text="Apellido Paterno:", bg=self.bg,fg=self.letraColor, font=("Verdana", 12)).place(x=50, y=80)
        self.inputApp = Entry(self.ventana, textvariable=self.apellidoP).place(x=200, y=80)

        self.apellidoM = StringVar()
        self.labelApm = Label(self.ventana, text="Apellido Materno:", bg=self.bg,fg=self.letraColor, font=("Verdana", 12)).place(x=50, y=110)
        self.inputApm = Entry(self.ventana, textvariable=self.apellidoM).place(x=200, y=110)

        self.telefono = StringVar()
        self.labelTelefono = Label(self.ventana, text="Telefono:", bg=self.bg,fg=self.letraColor, font=("Verdana", 12)).place(x=50, y=140)
        self.inputTelefono = Entry(self.ventana, textvariable=self.telefono).place(x=200, y=140)

        self.correo = StringVar()
        self.labelCorreo = Label(self.ventana, text="Correo:", bg=self.bg,fg=self.letraColor, font=("Verdana", 12)).place(x=50, y=170)
        self.inputCorreo = Entry(self.ventana, textvariable=self.correo).place(x=200, y=170)

        self.telefono2 = StringVar()
        self.labelEliminar = Label(self.ventana, text="Telefono:", bg=self.bg,fg=self.letraColor, font=("Verdana", 12)).place(x=370, y=50)
        self.spinTelefono = Spinbox(self.ventana, textvariable=self.telefono2).place(x=450, y=50)

        self.btnGuardar = Button(self.ventana, text="Guardar",command=self.agregar, bg="lime green",fg="black").place(x=230, y=200)
        self.btnGuardarC = Button(self.ventana, text="Guardar Cambios",command=self.guardarCambios, bg="lime green",fg="black")
        self.btnEliminar = Button(self.ventana, text="Eliminar",command=self.eliminar,bg="firebrick1", fg="black").place(x=460, y=80)
        self.btnEditar = Button(self.ventana, text="Editar",command=self.modificar,bg="yellow2", fg="black").place(x=520, y=80)
        
        self.cargar()
        self.ventana.mainloop()
            
    
        
    def cargar(self):
        
        self.textArea = Text(self.ventana, width=80, height=15)
        self.contactosR = self.contacto.MostrarTodo()
        self.textArea.insert(INSERT, "Nombre\tApellido P\t\tApellido M\t\tTeléfono\t\tCorreo\n")
        for row in self.contactosR:
            self.textArea.insert(INSERT,str(row[0])+"\t"+str(row[1])+"\t\t"+str(row[2])+"\t\t"+str(row[3])+"\t\t"+str(row[4])+"\n")
        self.textArea.place(x=20,y=230)
        self.textArea.config(state=DISABLED)
        
        
        
    def agregar(self):
        if(self.nombre.get() == "" or self.apellidoP.get() == "" or self.apellidoM.get()=="" or self.telefono.get()=="" or self.correo.get() ==""):
            messagebox.showwarning("Dato vacio","Por favor no deje campos vacios");
        else:
            if(self.telefono.get().isdigit()):
                datos = (self.nombre.get(),self.apellidoP.get(),self.apellidoM.get(),self.telefono.get(),self.correo.get())
                a = True
                a = self.contacto.AgregarContacto(datos)
                if a:
                    messagebox.showinfo("Información", "Los datos fueron cargados")
                    self.nombre.set("")
                    self.apellidoP.set("")
                    self.apellidoM.set("")
                    self.telefono.set("")
                    self.correo.set("")
                    self.cargar()
            else:
                messagebox.showwarning("Dato no valido","Ingrese un numero de telefono valido");
                
    
    def eliminar(self):
        if(self.telefono2.get() == ""):
            messagebox.showwarning("Dato vacio","Por favor escriba el telefono del contacto a eliminar")
        else:
            if(self.telefono2.get().isdigit()):
                self.num = (self.telefono2.get(),)
                a = self.contacto.Eliminar(self.num)
                if(a == 1):
                    self.telefono2.set("")
                    self.cargar()
                    messagebox.showinfo("Eliminado", "El contacto ha sido eliminado")
                else:
                    messagebox.showinfo("No eliminado", "El contacto no existe")
            else:
                messagebox.showwarning("Dato no valido","Ingrese un numero de telefono valido");
                
    def modificar(self):
        if(self.telefono2.get() == ""):
            messagebox.showwarning("Dato vacio","Por favor escriba el telefono del contacto a editar")
        else:
            if(self.telefono2.get().isdigit()):
                self.numModificar = (self.telefono2.get())
                numero = (self.telefono2.get(),)
                self.datos = self.contacto.Consulta(numero)
                if(len(self.datos) > 0):
                    self.btnGuardarC.place(x=230, y=200)
                    self.nombre.set(self.datos[0][0])
                    self.apellidoP.set(self.datos[0][1])
                    self.apellidoM.set(self.datos[0][2])
                    self.telefono.set(self.datos[0][3])
                    self.correo.set(self.datos[0][4])
                    messagebox.showinfo("Editar","Por favor edite el contacto en el formulario de la izquierda")
                    self.telefono2.set("")
                    self.cargar()
                else:
                    messagebox.showinfo("Contacto no existe","No existen contactos registrados con ese teléfono")
            else:
                messagebox.showwarning("Dato no valido","Ingrese un numero de telefono valido")
        
        
    def guardarCambios(self):
        if(self.nombre.get() == "" or self.apellidoP.get() == "" or self.apellidoM.get()=="" or self.telefono.get()=="" or self.correo.get() ==""):
            messagebox.showwarning("Dato vacio","Por favor no deje campos vacios");
        else:
            if(self.telefono.get().isdigit()):
                datos = (self.nombre.get(),self.apellidoP.get(),self.apellidoM.get(),self.telefono.get(),self.correo.get())
                a = False
                a = self.contacto.Actualizar(datos,self.numModificar)
                if a:
                    messagebox.showinfo("Información", "Los datos fueron modificados")
                    self.nombre.set("")
                    self.apellidoP.set("")
                    self.apellidoM.set("")
                    self.telefono.set("")
                    self.correo.set("")
                    self.cargar()
                    self.btnGuardarC.place_forget()
            else:
                messagebox.showwarning("Dato no valido","Ingrese un numero de telefono valido")
        
        
aplicacion = Agenda()