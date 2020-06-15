import sqlite3
from tkinter import messagebox

class Contacto:
    def abrir(self):
        conexion=sqlite3.connect("Agenda.db")
        return conexion
    
    def MostrarTodo(self):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql = "select * from Contactos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conexion.close()
    
    def AgregarContacto(self,datos):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql = "insert into Contactos(NOMBRE,APELLIDOP,APELLIDOM,TELEFONO,CORREO) values(?,?,?,?,?)"
            cursor.execute(sql,datos)
            conexion.commit()
            conexion.close()
            return True
        except:
            messagebox.showwarning("Numero registrado","Ya has registrado un contacto con ese numero");
            return False
        
    def Eliminar(self,num):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql = "delete from Contactos where telefono=?"
            cursor.execute(sql,num)
            conexion.commit()
            return cursor.rowcount
        except:
            conexion.close()
    
    
    def Consulta(self,num):
        try:
            conexion = self.abrir()
            cursor2 = conexion.cursor()
            sql = "select nombre,apellidop,apellidom,telefono,correo from Contactos where telefono=?"
            cursor2.execute(sql,num)
            return cursor2.fetchall()
        finally:
            conexion.close()
            
    def Actualizar(self,datos,num):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql = (f"update Contactos set nombre=?,apellidop=?,apellidom=?,telefono=?,correo=? where telefono={num}")
            cursor.execute(sql,datos)
            conexion.commit()
            return True
        except:
            conexion.close()
            messagebox.showwarning("Numero registrado","Ya has registrado un contacto con ese numero");
            