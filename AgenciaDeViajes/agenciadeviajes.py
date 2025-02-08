#Se importa al sistema la librería previamente instalada para su posterior uso.
import numpy as np
import datetime as dt
import sys

from personas import Personas
from persona import Persona

from reservas import Reservas
from reserva import Reserva

from paquetes import Paquetes
from paquete import Paquete

from hotel import Hotel
from habitacion import Habitacion
from vuelo import Vuelo


'''
Autor: Jorge Ruiz
Fecha de creación: 22/10/2024
Clase: Menu, la cual se ejecutara de manera principal para abrir el menu
'''
class Menu():
    usuario: str
    personas: object
    reservas: object
    paquetes: object

    def __init__(self, personas, reservas, paquetes):
        self.usuario = ""
        self.personas = personas
        self.reservas = reservas
        self.paquetes = paquetes

    def main(self):
        while(True):
            print("""Un cordial saludo querido usuario, seleccione la opción que desea escribiendo el numero correspondientes a las opciones que le brindare a continuacion:\n
                    1: Iniciar Sesion
                    2: Registrarse como Cliente
                    3: Salir de la aplicacion
            """)

            opc = int(input("Digite aqui la Opcion escogida: "))

            match opc:
                case 1:
                    self.iniciar_sesion()
                    break
                case 2:
                    if(self.personas.registrar_persona(1)):
                        print("¡Su usuario ha sido creado con exito!")
                    else:
                        print("¡Al parecer hemos llegado al maximo de usuarios, comunicate con soporte!")
                    
                    print("Presione una tecla para volver al menu")
                    self.esperar()
                    self.main()
                    break
                case 3:
                    break
                case _:
                    print("¡Selecciono una opcion fuera del rango dado!, vuelva a Intentarlo")

    #Esperar la entrada del usuario cuando sea necesario
    def esperar(self):
        if sys.platform == "win32":
            import msvcrt
            # print("Presiona cualquier tecla para volver al menu")
            msvcrt.getch()
        else:
            # print("Presiona Enter para para volver al menu")
            input()



    def iniciar_sesion(self):
        documento = int( input("Digite por favor su documento de identidad: ") )
        contrasenia = input("Digite por favor su contraseña: ")
        n = self.personas.get_personas().size
        fila_documento = None
        for i in range(n):
            if(self.personas.get_personas()[i].get_documento() == documento):
                fila_documento = i
                print(i)
                break

        if(fila_documento is not None):
            if(self.personas.get_personas()[fila_documento].get_contrasenia() == contrasenia):
                print("Usuario autenticado con exito")
            else:
                print("Su documento o la contraseña son incorrectos")

            self.usuario = self.personas.get_personas()[fila_documento]

            match self.usuario.get_rol():
                case 1:
                    self.mostrar_menu_cliente()
                case 2:
                    self.mostrar_menu_empleado()
                case 3:
                    self.mostrar_menu_administrador()


        else:
            print("No se ha encontrado su documento de identidad")
            self.iniciar_sesion()

    def reservar_paquete(self):
            reserva_exitosa = False
            while(not reserva_exitosa):
                self.paquetes.imprimir_disponibilidad_paquetes(self.usuario)
                numero_paquete = self.paquetes.escoger_paquete()

                cant_personas = 1
                while(cant_personas >= 4 and cant_personas < 0):
                    cant_personas = int(input("Digite la cantidad de personas que van a viajar (incluyendo a usted): "))

                error = True
                while(error):
                    print("Ejemplo de fecha 17/03/2024")
                    try:
                        fecha_inicial = dt.datetime.strptime(input("Digite el dia que planea viajar, en formato DD/MM/YYYY: "), "%d/%m/%Y")
                        fecha_final = dt.datetime.strptime(input("Digite el dia que planea terminar su viaje, en formato DD/MM/YYYY: "), "%d/%m/%Y")
                        error = False

                        if(fecha_inicial > fecha_final):
                            print("¡Al parecer tu fecha inicial es mayor a tu fecha final, verifique nuevamente!\n")
                            error = True

                    except ValueError:
                        print("¡Hubo un error al digitar la fechas verifique nuevamente!\n")
                        error = True

                
                reserva = Reserva( self.paquetes.get_paquetes()[numero_paquete] , self.usuario, cant_personas, fecha_inicial, fecha_final)
                reserva_exitosa = reservas.verificar_reserva(reserva)
                if(not reserva_exitosa):
                    opc = input("La reserva no fue exitosa, ¿desea continuar? S/N: ")
                    if(opc.strip().upper() == "N"):
                        reserva_exitosa = True
                    else:
                        reserva_exitosa = False
                else:
                    print("¡La reserva fue exitosa!")
                    self.esperar()
            self.mostrar_menu_cliente()
            
            


    def mostrar_menu_cliente(self):
        while(True):
            print("""
                _____  _  _               _         \n            /  __ \| |(_)             | |        \n            | /  \/| | _   ___  _ __  | |_   ___ \n            | |    | || | / _ \| '_ \ | __| / _ \ \n            | \__/\| || ||  __/| | | || |_ |  __/\n            \_____/|_||_| \___||_| |_| \__| \___|\n
            \n\n
            Seleccione una Opcion:\n
            1: Ver paquetes turísticos\n
            2: Ver el listado de mis reversas\n
            3: Cerrar Sesion\n
            """)
            opc = int(input("Digite aqui la Opcion escogida: "))

            match opc:
                case 1:
                    self.paquetes.imprimir_disponibilidad_paquetes(self.usuario)
                    print("""
                    Seleccione una Opcion:\n
                    1: Registrar una reserva\n
                    2: Volver al menu\n
                    """)
                    opc2 = int(input("Digite aqui la Opcion escogida: "))
                    match opc2:
                        case 1:
                            self.reservar_paquete()
                            print("Presione una tecla para volver al menu")
                            self.esperar()
                        case 2:
                            pass
                case 2:
                    self.reservas.generar_factura_reserva_usuario(self.usuario)
                    print("""
                    Seleccione una Opcion:\n
                    1: Eliminar una reserva\n
                    2: Volver al menu\n
                    """)
                    opc2 = int(input("Digite aqui la Opcion escogida: "))
                    match opc2:
                        case 1:
                            self.reservas.eliminar_reserva_usuario()
                            print("Ingrese una tecla para volver al menu")
                            self.esperar()
                        case 2:
                            pass
                        case _:
                            pass
                    
                case 3:
                    self.main()
                    break
                case _:
                    print("¡Selecciono una opcion fuera del rango dado!, vuelva a Intentarlo")


    def mostrar_menu_empleado(self):
        while(True):
            print("""
                _____                    _                   _         \n            |  ___|                  | |                 | |        \n            | |__   _ __ ___   _ __  | |  ___   __ _   __| |  ___   \n            |  __| | '_ ` _ \ | '_ \ | | / _ \ / _` | / _` | / _ \  \n            | |___ | | | | | || |_) || ||  __/| (_| || (_| || (_) | \n            \____/ |_| |_| |_|| .__/ |_| \___| \__,_| \__,_| \___/  \n                            | |                                     \n                            |_|                                     \n
            \n\n
            Seleccione una Opcion:\n
            1: Administrar el Rango de un Cliente\n
            2: Gestionar Paquete Turístico\n
            3: Consultar la Informacion de un Cliente\n
            4: Generar un Listado de Reservas de un Cliente\n
            5: Registrar a un Cliente\n
            6: Cerrar Sesion\n
            """)
            # 3: Consultar la Disponibilidad de Vuelos y Hoteles\n

            opc = int(input("Digite aqui la Opcion escogida: "))
            match opc:
                case 1:
                    documento = int(input("Digite el documento del cliente: "))
                    indice_cliente = self.personas.buscar_persona_documento(documento)
                    if(indice_cliente is not None):
                        personas.get_personas()[indice_cliente].promocionar_cliente()
                    else:
                        print("No se ha encontrado al usuario")
                    print("Presione una tecla para volver al menu")
                    self.esperar()

                case 2:
                    self.paquetes.imprimir_paquetes()
                    opc2 = input("Desea eliminar un paquete S/N")
                    eliminar = True if opc2.strip().upper() == "S" else False
                    while(eliminar):
                        i_paquete = int(input("Digite el numero de paquete que desea eliminar")) - 1
                    
                        if(i_paquete <= paquetes.get_cant_paquetes() and i_paquete >= 0 ):
                            for i in range(i_paquete, paquetes.get_cant_paquetes() - 1):
                                paquetes.get_reservas()[i] = paquetes.get_reservas()[i + 1]
                            paquetes.get_reservas()[paquetes.get_cant_paquetes()] = None
                            paquetes._cant_paquetes -= 1
                            print("Se elimino el paquete con exito")
                        else:
                            print("¡Digito un numero de paquete incorrecto!")

                        opc2 = input("Desea eliminar otro paquete S/N")
                    print("Presione una tecla para volver al menu")
                    self.esperar()

                case 3:
                    documento = int(input("Digite el documento del cliente: "))
                    indice_cliente = self.personas.buscar_persona_documento(documento)
                    if(indice_cliente is not None):
                        personas.get_personas()[indice_cliente].mostrar_datos()
                    else:
                        print("No se ha encontrado al usuario")
                    print("Presione una tecla para volver al menu")
                    self.esperar()

                case 4:
                    documento = int(input("Digite el documento del cliente: "))
                    indice_cliente = self.personas.buscar_persona_documento(documento)
                    if(indice_cliente is not None):
                        personas.get_personas()[indice_cliente].mostrar_datos()
                        
                        print("\nReservas realizadas por el cliente: \n")
                        reservas_realizadas = False
                        for i in range(0, self.reservas.get_cant_reservas()):
                            if(self.reservas.get_reservas()[i].get_persona().get_documento() == documento):
                                print("Reserva N°" + str(i) + ": ")
                                self.reservas.get_reservas()[i].imprimir_reserva()
                                reservas_realizadas = True

                        if(not reservas_realizadas):
                            print("El cliente no ha realizado reservas")

                    else:
                        print("No se ha encontrado al usuario")
                    print("Presione una tecla para volver al menu")
                    self.esperar()
                case 5:
                    if(self.personas.registrar_persona(1)):
                        print("¡Su usuario ha sido creado con exito!")
                    else:
                        print("¡Al parecer hemos llegado al maximo de usuarios, comunicate con soporte!")
                    
                    print("Presione una tecla para volver al menu")
                    self.esperar()
                
                case 6:
                    self.main()
                    break
                case _:
                    print("¡Selecciono una opcion fuera del rango dado!, vuelva a Intentarlo")
                    


    def mostrar_menu_administrador(self):
        while(True):
            print("""
                ___       _             _         _       _                     _               \n             / _ \     | |           (_)       (_)     | |                   | |              \n            / /_\ \  __| | _ __ ___   _  _ __   _  ___ | |_  _ __   __ _   __| |  ___   _ __  \n            |  _  | / _` || '_ ` _ \ | || '_ \ | |/ __|| __|| '__| / _` | / _` | / _ \ | '__| \n            | | | || (_| || | | | | || || | | || |\__ \| |_ | |   | (_| || (_| || (_) || |    \n            \_| |_/ \__,_||_| |_| |_||_||_| |_||_||___/ \__||_|    \__,_| \__,_| \___/ |_|    \n                                                                                              \n
            \n\n
            Seleccione una Opcion:\n
            1: Administrar el Rango de un Cliente\n
            2: Gestionar Paquete Turístico\n
            3: Generar Factura\n
            4: Consultar la Informacion de un Cliente\n
            5: Registrar un usuario personalizado\n
            6: Cerrar Sesion\n
            """)
            
            opc = int(input("Digite aqui la Opcion escogida: "))
            match opc:
                case 1:
                    documento = int(input("Digite el documento del cliente: "))
                    indice_cliente = self.personas.buscar_persona_documento(documento)
                    if(indice_cliente is not None):
                        personas.get_personas()[indice_cliente].promocionar_cliente()
                    else:
                        print("No se ha encontrado al usuario")
                    print("Presione una tecla para volver al menu")
                    self.esperar()

                case 2:
                    self.paquetes.imprimir_paquetes()
                    opc2 = input("Desea eliminar un paquete S/N")
                    eliminar = True if opc2.strip().upper() == "S" else False
                    while(eliminar):
                        i_paquete = int(input("Digite el numero de paquete que desea eliminar")) - 1
                    
                        if(i_paquete <= paquetes.get_cant_paquetes() and i_paquete >= 0 ):
                            for i in range(i_paquete, paquetes.get_cant_paquetes() - 1):
                                paquetes.get_reservas()[i] = paquetes.get_reservas()[i + 1]
                            paquetes.get_reservas()[paquetes.get_cant_paquetes()] = None
                            paquetes._cant_paquetes -= 1
                            print("Se elimino el paquete con exito")
                        else:
                            print("¡Digito un numero de paquete incorrecto!")

                        opc2 = input("Desea eliminar otro paquete S/N")
                    print("Presione una tecla para volver al menu")
                    self.esperar()

                case 3:
                    documento = int(input("Digite el documento del cliente: "))
                    indice_cliente = self.personas.buscar_persona_documento(documento)
                    if(indice_cliente is not None):
                        personas.get_personas()[indice_cliente].mostrar_datos()
                    else:
                        print("No se ha encontrado al usuario")
                    print("Presione una tecla para volver al menu")
                    self.esperar()

                case 4:
                    documento = int(input("Digite el documento del cliente: "))
                    indice_cliente = self.personas.buscar_persona_documento(documento)
                    if(indice_cliente is not None):
                        personas.get_personas()[indice_cliente].mostrar_datos()
                        
                        print("\nReservas realizadas por el cliente: \n")
                        reservas_realizadas = False
                        for i in range(0, self.reservas.get_cant_reservas()):
                            if(self.reservas.get_reservas()[i].get_persona().get_documento() == documento):
                                print("Reserva N°" + str(i) + ": ")
                                self.reservas.get_reservas()[i].imprimir_reserva()
                                reservas_realizadas = True

                        if(not reservas_realizadas):
                            print("El cliente no ha realizado reservas")

                    else:
                        print("No se ha encontrado al usuario")
                    print("Presione una tecla para volver al menu")
                    self.esperar()
                case 5:
                    rol = input("Digite el rol que tendra el usuario: ")
                    
                    if(self._personas.registrar_persona(rol)):
                        print("¡El usuario ha sido creado con exito!")
                    else:
                        print("¡Al parecer hemos llegado al maximo de usuarios, comunicate con soporte!")
                    
                    print("Presione una tecla para volver al menu")
                    self.esperar()
                    
                case 6:
                    self.main()
                    break
                case _:
                    print("¡Selecciono una opcion fuera del rango dado!, vuelva a Intentarlo")


    def administrar_rango_cliente(self, cliente):
        cliente.promocionar_cliente()


#Usuarios
us1 = Persona("Jorge", 1036542396, "TI", 3201592332, "jorge.ruizf@udea.edu.co", "Jorge Andres", 3242848521, "contrasenia", 3, 0)
us2 = Persona("Carlos", 726362636, "CC", 3224667232, "carlos.mera@udea.edu.co", "Logica I", 3242848521, "contrasenia2", 2, 0)
us3 = Persona("Roger", 1024567741, "CC", 3242343534, "roger.giraldo@udea.edu.co", "Alejandro Roger", 3242848521, "contrasenia3", 1, 0)
us4 = Persona("Jorge1", 123456789, "CC", 3242343534, "jorge.2@udea.edu.co", "Jorge", 3242848521, "contrasenia", 1, 0)
personas = Personas(100)
personas.agregar_persona(us1)
personas.agregar_persona(us2)
personas.agregar_persona(us3)
personas.agregar_persona(us4)

#Vuelos
vl1 = Vuelo(1, "Colombia", "Peru", dt.time(21,15), 26, "Juan Carlos")
vl2 = Vuelo(2, "Colombia", "Argentina", dt.time(18,30), 30, "Carlos Alberto")

#Habitaciones
ha1 = Habitacion(1, 3, "Triple", 130000)
ha2 = Habitacion(2, 2, "Matrimonial", 120000)
ho1_hab = np.full(2, [ha1, ha2], dtype=object)
ho1 = Hotel("Cavellano", "Argentina", "Clle 32", 72031035, "cavellanoARG@gmail.com", "Regular", 2)
ho1.set_habitaciones(ho1_hab)

ha3 = Habitacion(1, 3, "Triple", 110000)
ha4 = Habitacion(2, 2, "Matrimonial", 100000)
ha5 = Habitacion(3, 1, "Sencilla", 80000)
ho2_hab = np.full(3, [ha3, ha4, ha5], dtype=object)
ho2 = Hotel("Lima", "Peru", "Av 53", 91300421, "limaPE@gmail.com", "Regular", 3)
ho2.set_habitaciones(ho2_hab)

#Paquetes
pa1 = Paquete(vl1, ho2)
pa2 = Paquete(vl2, ho1)

paquetes = Paquetes(100)
paquetes.agregar_paquete(pa1)
paquetes.agregar_paquete(pa2)


#Reservas
reservas = Reservas(20)

re1 = Reserva(pa1, us4, 2, dt.datetime(2024, 11, 1), dt.datetime(2024, 11, 5))
reservas.verificar_reserva(re1)

re2 = Reserva(pa1, us4, 2, dt.datetime(2024, 11, 1), dt.datetime(2024, 11, 5))
reservas.verificar_reserva(re2)

re3 = Reserva(pa2, us4, 2, dt.datetime(2024, 11, 1), dt.datetime(2024, 11, 5))
reservas.verificar_reserva(re3)

re4 = Reserva(pa2, us4, 2, dt.datetime(2024, 11, 1), dt.datetime(2024, 11, 5))
reservas.verificar_reserva(re4)

# reservas.imprimir_reservas()

# print(pa1.get_vuelo().get_hora_salida())

menu = Menu(personas, reservas, paquetes)
menu.main()