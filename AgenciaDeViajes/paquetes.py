import numpy as np
from paquete import Paquete

'''
Autor: Jorge Ruiz
Fecha de creación: 30/11/2024
Clase: Paquetes para administrar el arreglo de paquetes y generar un listado dependiendo de la diponibilidad de estos
'''
class Paquetes():
    _paquetes: Paquete
    _cant_paquetes: int

    def __init__(self, max_paquetes):
        self._cant_paquetes = 0
        self._paquetes = np.full((max_paquetes), fill_value = None, dtype=object)
    
    def agregar_paquete(self, paquete):
        self._paquetes[self._cant_paquetes] = paquete
        self._cant_paquetes += 1

    def imprimir_disponibilidad_paquetes(self, usuario):
        for i in range(0, self._cant_paquetes):
            if(self._paquetes[i].get_hotel().get_categoria() == usuario.get_categoria()):
                vuelo = self._paquetes[i].get_vuelo()
                hotel = self._paquetes[i].get_hotel()
                print("Paquete N°" + str(i + 1) + ":\n")
                print(r"          _           Número de vuelo: " + str(vuelo.get_numero_vuelo()))
                print(r"        -=\`\         Ciudad de origen: " + str(vuelo.get_ciudad_origen()))
                print(r"    |\ ____\_\__      Ciudad de destino: " + str(vuelo.get_ciudad_destino()))
                print(r'  -=\c`""""""" "`)    Hora de salida: ' + str(vuelo.get_hora_salida()))
                print(r"     `~~~~~/ /~~`     Capacidad de pasajeros: " + str(vuelo.get_capacidad()))
                print(r"       -==/ /         Nombre del piloto: " + str(vuelo.get_nombre_piloto()))
                print(r"         '-'")
                print("")

                print("    ___________       Nombre del Hotel: " + str(hotel.get_nombre()))
                print("    | [] _ [] |       Direccion del Hotel: " + str(hotel.get_direccion()))
                print("    | []^  [] |       Telefono: " + str(hotel.get_telefono()))
                print("    |    ()   |       Correo Electronico: " + str(hotel.get_e_mail()))
                print("\n     Habitaciones:")
                for j in range(0, hotel.get_cant_habitaciones()):
                    print("       Habitacion N°" + str(hotel.get_habitaciones()[j].get_id()) + ": ")
                    print("         Precio por noche: " + str(hotel.get_habitaciones()[j].get_precio_noche()) + "$")
                    print("         Capacidad de la habitacion: " + str(hotel.get_habitaciones()[j].get_capacidad()))
                    print('         Descripcion: "' + str(hotel.get_habitaciones()[j].get_descripcion()) + '"\n')
                
                print("\n\n")

    def imprimir_paquetes(self):
        for i in range(0, self._cant_paquetes):
            vuelo = self._paquetes[i].get_vuelo()
            hotel = self._paquetes[i].get_hotel()
            print("Paquete N°" + str(i + 1) + ":\n")
            print("Número de vuelo: " + str(vuelo.get_numero_vuelo()))
            print("Ciudad de origen: " + str(vuelo.get_ciudad_origen()))
            print("Ciudad de destino: " + str(vuelo.get_ciudad_destino()))
            print('Hora de salida: ' + str(vuelo.get_hora_salida()))
            print("Capacidad de pasajeros: " + str(vuelo.get_capacidad()))
            print("Nombre del piloto: " + str(vuelo.get_nombre_piloto()))

            print("Nombre del Hotel: " + str(hotel.get_nombre()))
            print("Direccion del Hotel: " + str(hotel.get_direccion()))
            print("Telefono: " + str(hotel.get_telefono()))
            print("Correo Electronico: " + str(hotel.get_e_mail()))
            print("Categoría: " + str(hotel.get_categoria()))
            print("\n  Habitaciones:")
            for j in range(0, hotel.get_cant_habitaciones()):
                print("   Habitacion N°" + str(hotel.get_habitaciones()[j].get_id()) + ": ")
                print("     Precio por noche: " + str(hotel.get_habitaciones()[j].get_precio_noche()) + "$")
                print("     Capacidad de la habitacion: " + str(hotel.get_habitaciones()[j].get_capacidad()))
                print('     Descripcion: "' + str(hotel.get_habitaciones()[j].get_descripcion()) + '"\n')


    def escoger_paquete(self) -> int:
        return (int(input("\nSeleccione el numero de paquete que ha escogido: ")) - 1)


    
    #Metodos Getters

    def get_paquetes(self) -> object:
        return self._paquetes

    def get_cant_paquetes(self) -> int:
        return self._cant_paquetes
    

    #Metodos Setters

    def set_paquetes(self, paquetes):
        self._paquetes = paquetes
