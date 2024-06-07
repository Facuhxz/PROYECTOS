# main.py

from PagCompras.Clientes import Cliente


# Crear instancias de Cliente
cliente1 = Cliente("Juan Pérez", "juan.perez@example.com", "123456789", "Avenida Siempreviva 742")
cliente2 = Cliente("Ana García", "ana.garcia@example.com", "987654321", "Calle Real 321")

# Mostrar información de los clientes
print(cliente1)
print(cliente1.mostrar_info())
print(cliente2)
print(cliente2.mostrar_info())

# Mostrar la compra del cliente
cliente1.comprar("laptop", "movil")

# Mostrar la direccion de entrega de un cliente
cliente1.direccion_de_entrega("Avenida Siempreviva 742")


    

    
