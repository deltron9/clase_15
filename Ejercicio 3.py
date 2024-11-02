#Ejercicio 3:  Crear una aplicación de gestión de contactos.
class GestorContactos:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f'Nombre: {self.nombre} \nTelefono: {self.telefono} \ne-mail: {self.email}\n'

def agregar_contacto(contactos, nombre, telefono, email):
    if nombre in contactos:
        print('Este contacto ya existe rey, estas gaga')
    else:
        contactos[nombre] = GestorContactos(nombre, telefono, email)
        print('Contacto agregado rey')

def eliminar_contacto(contactos, nombre):
    if nombre in contactos:
        del contactos[nombre]
        print('Contacto...AFUERA')
    else:
        print('y ese quien e? contacto no encontrado')

def buscar_contacto(contactos, nombre):
    if nombre in contactos:
        print(contactos[nombre])
    else:
        print('y... no está ese aca')

def mostrar_contactos(contactos):
    if contactos:
        for contacto in contactos.values():
            print(contacto)
    else:
        print('No hay contactos perron, soltá la pc y conocé gente')

def menu():
    contactos = {
        'Pablo Conde': GestorContactos('Pablo Conde', '123456789', 'conde@utn-fra.com'),
        'Santino Casado': GestorContactos('Santino Casado', '987654321', 'santino@utn-fra.com'),
        'Marshall Cámara': GestorContactos('Marshall Cámara', '456123789', 'marshall@utn-fra.com')
    }

    while True:
        menu_opciones = f'\n\t---> |Menú de Gestión de Contactos| <--- \n[1] Agregar Contacto. \n[2]Buscar Contacto. \n[3]Eliminar Contacto. \n[4] Mostrar Contactos. \n[5]Salir del programa.\n'

        opcion = input(f'{menu_opciones} \n\tSeleccioná una opción: ')
        
        match opcion:
            case '1':
                nombre = input('Ingresa el nombre: ')
                telefono = input('Ingresa el teléfono: ')
                email = input('Ingresa el email: ')
                agregar_contacto(contactos, nombre, telefono, email)
        
            case '2':
                nombre = input('Ingresa el nombre del contacto a buscar: ')
                buscar_contacto(contactos, nombre)
        
            case '3':
                nombre = input('Ingresa el nombre del contacto a eliminar: ')
                eliminar_contacto(contactos, nombre)
        
            case '4':
                mostrar_contactos(contactos)
        
            case '5':
                print('Saliendo del programa... \n Haasta la proczimaaaa *musica piola dubstep *')
                break

menu()

