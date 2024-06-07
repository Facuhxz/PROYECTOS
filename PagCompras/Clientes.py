# Creacion de cliente

class Cliente:
    def __init__(self, nombre, correo, telefono, direccion):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        print(f"Se a creado el cliente", self.nombre)
        
     # Esto nos permite ver el nombre del cliente
    def __str__(self):
        return self.nombre 
    
     # Esto nos permite ver la direccion de entrega del cliente
    def direccion_de_entrega(self, direccion):
        self.direccion = direccion
        print(f"La compra de {self.nombre} llegara a: {self.direccion}")
        
     # Esto nos muesta la info del cliente
    def mostrar_info(self):
        return f"Cliente: {self.nombre}\nCorreo: {self.correo}\nTeléfono: {self.telefono}\nDirección: {self.direccion}"
    
     # Esto nos muestra la compra del cliente
    def comprar(self, laptop, movil):
        self.laptop = laptop
        self.movil = movil
        print(f"El cliente", self.nombre, "compro una", self.laptop, "y un", self.movil)
        

# #Ejemplo de uso
# cliente1 = Cliente("Juan Pérez", "juan.perez@example.com", "123456789", "Avenida Siempreviva 742")
# print(cliente1)

# cliente1.direccion_de_entrega("Avenida Siempreviva 742")
# print(cliente1.mostrar_info())

# cliente1.comprar("laptop", "movil")
