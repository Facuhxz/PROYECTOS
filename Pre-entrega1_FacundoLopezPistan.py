def registrar_usuario(base_datos):
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    if nombre_usuario in base_datos:
        print("El usuario ya existe. Intente con otro nombre de usuario.")
    else:
        base_datos[nombre_usuario] = contraseña
        print("Usuario registrado exitosamente.")
        guardar_base_datos(base_datos)

def mostrar_usuarios(base_datos):
    print("Usuarios registrados:")
    for nombre_usuario, contraseña in base_datos.items():
        print(f"Usuario: {nombre_usuario}, Contraseña: {contraseña}")

def login_usuario(base_datos):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre_usuario in base_datos and base_datos[nombre_usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def guardar_base_datos(base_datos):
    with open("base_datos.txt", "r+") as archivo:
        for nombre_usuario, contraseña in base_datos.items():
            archivo.write(f"{nombre_usuario},{contraseña}\n")

def cargar_base_datos():
    base_datos = {}
    try:
        with open("base_datos.txt", "r") as archivo:
            for linea in archivo:
                nombre_usuario, contraseña = linea.strip().split(",")
                base_datos[nombre_usuario] = contraseña
    except FileNotFoundError:
        pass
    return base_datos

def main():
    base_datos = cargar_base_datos()
    while True:
        print("\nBienvenido al sistema de registro y login de usuarios")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(base_datos)
        elif opcion == "2":
            mostrar_usuarios(base_datos)
        elif opcion == "3":
            login_usuario(base_datos)
        elif opcion == "4":
            print("Gracias por usar nuestro sistema.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
