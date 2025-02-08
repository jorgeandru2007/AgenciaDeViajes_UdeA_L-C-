import numpy as np
from reserva import Reserva

class Reservas():
    _reservas: Reserva
    _cant_reservas: int

    #Se añade el arreglo reservas como parametro para tenerlo en cuenta en la creacion de la reserva
    def __init__(self, max_reservas):
        self._cant_reservas = 0
        self._reservas = np.full((max_reservas), fill_value = None, dtype=object)

    def verificar_reserva(self, reserva) -> bool:
        if(reserva._buscar_habitacion_cliente_capacidad(self._reservas, self._cant_reservas)):
            self._reservas[self._cant_reservas] = reserva
            self._cant_reservas += 1
            return True
        else:
            return False

    def imprimir_reservas(self):
        for i in range(0, self._cant_reservas):
            print(f"Reserva N°{i + 1}: {self._reservas[i].get_paquete().get_hotel().get_nombre()}, con habitacion {self._reservas[i].get_habitacion().get_id()}")
    

    def generar_factura_reserva_usuario(self, usuario) -> int:
        cant_reservas_usuario = 0
        for i in range(0, self._cant_reservas):
            if(self._reservas[i].get_persona() == usuario):
                diferencia = self._reservas[i].get_fecha_final() - self._reservas[i].get_fecha_inicial()
                costo = self._reservas[i].get_habitacion().get_precio_noche() * diferencia.days
                print(f"Reserva N°{i + 1}: {self._reservas[i].get_paquete().get_hotel().get_nombre()}, con un costo de: {costo}$ y una estancia de {diferencia.days} días")
                cant_reservas_usuario += 1
        return cant_reservas_usuario
    
    def eliminar_reserva_usuario(self):
        reserva_eliminada = False
        while(not reserva_eliminada):
            try:
                i_reserva = int(input("Digite el numero de reserva que desea eliminar: ")) - 1
                if(i_reserva <= self._cant_reservas and i_reserva >= 0 ):
                    for i in range(i_reserva, self._cant_reservas - 1):
                        self._reservas[i] = self._reservas[i + 1]
                    self._reservas[self._cant_reservas] = None
                    reserva_eliminada = True
                    self._cant_reservas -= 1
                    print("Se elimino la reserva con exito")
                else:
                    print("¡Digito un numero de reserva incorrecto!")
            except ValueError:
                print("¡No digito un numero, vuelva a intentarlo!")

    #Metodos Getters

    def get_reservas(self) -> object:
        return self._reservas

    def get_cant_reservas(self) -> int:
        return self._cant_reservas
