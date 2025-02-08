from paquete import Paquete
from persona import Persona
from habitacion import Habitacion



class Reserva():
    _paquete: Paquete
    _persona: Persona
    _cant_personas: int
    _fecha_inicial: object
    _fecha_final: object
    _habitacion: Habitacion


    #Se añade el arreglo reservas como parametro para tenerlo en cuenta en la creacion de la reserva
    def __init__(self, paquete = None, persona = None, cant_personas = 1, fecha_inicial = None, fecha_final = None, habitacion = None):
        self._paquete = paquete
        self._persona = persona
        self._cant_personas = cant_personas
        self._fecha_inicial = fecha_inicial
        self._fecha_final = fecha_final
        self._habitacion = None

    def _buscar_habitacion_cliente_capacidad(self, reservas, cant_reservas) -> bool:
        hotel = self._paquete.get_hotel()
        habitaciones = hotel.get_habitaciones()
        disponible = False
        #hace un ciclo para recorrer todas las habitaciones del hotel
        for i in range(0, hotel.get_cant_habitaciones()):
            #compara si el hotel tiene la misma capacidad que las personas
            if(habitaciones[i].get_capacidad() == self._cant_personas):
                #verificar si esta disponible en el arreglo de reservas, primero con el hotel y luego con la habitacion
                disponible = True
                n_fila = i
                #recorre el arreglo de reservas
                for j in range(0, cant_reservas):
                    #este try es para evitar un error a la hora de preguntar por el id de la reserva, ya que de alguna manera algun elemento de tipo None se filtra, y si se le pregunta un atributo este fallara
                    try:
                        #si el nombre de un hotel que ya se habia reservado es igual al nombre de nuestro hotel
                        if(reservas[j] is not None):
                            if (reservas[j].get_paquete() is not None and reservas[j].get_paquete().get_hotel() is not None):
                                if(reservas[j].get_paquete().get_hotel().get_nombre() == hotel.get_nombre()):
                                    #recorre la cantidad de habitacion del hotel que ya se habia reservado
                                    for k in range(0, reservas[j].get_paquete().get_hotel().get_cant_habitaciones()):
                                        #si el id de la habitacion del hotel que ya se habia reservado coincide con el id de nuestra habitacion
                                        if(reservas[j].get_paquete().get_hotel().get_habitaciones()[k].get_id() == habitaciones[i].get_id()):
                                            #si las fechas se cruzan
                                            if(reservas[j]._fecha_inicial < self._fecha_final and reservas[j]._fecha_final > self._fecha_inicial):
                                                disponible = False
                                                n_fila = None
                                                k = reservas[j].get_paquete().get_hotel().get_cant_habitaciones()
                                                j = cant_reservas
                                                i = hotel.get_cant_habitaciones()
                    except:
                        pass
        if(disponible and n_fila != None):
            self._habitacion = habitaciones[n_fila]
            return True
        else:
            return False
    
    def imprimir_reserva(self):
        print("N° de vuelo: " + str(self._paquete.get_vuelo().get_numero_vuelo()))
        print("Dia de salida: " + self._fecha_inicial.strftime("%d/%m/%Y"))
        print("Hora de salida: " + self._paquete.get_vuelo().get_hora_salida().strftime("%H:%M"))
        print("Dia de regreso: " + self._fecha_final.strftime("%d/%m/%Y"))
        print("Ciudad de destino: " + self._paquete.get_vuelo().get_ciudad_destino())
        print("Nombre del hotel: " + self._paquete.get_hotel().get_nombre())
        print("Direccion del hotel: " + self._paquete.get_hotel().get_direccion())
        print("Telefono del hotel: " + str(self._paquete.get_hotel().get_telefono()))
        print("E-mail del hotel: " + str(self._paquete.get_hotel().get_e_mail()))
        print("")

    #Metodos Getters

    def get_paquete(self) -> Paquete:
        return self._paquete

    def get_persona(self) -> Persona:
        return self._persona

    def get_cant_personas(self) -> int:
        return self._cant_personas

    def get_fecha_inicial(self) -> object:
        return self._fecha_inicial

    def get_fecha_final(self) -> object:
        return self._fecha_final

    def get_habitacion(self) -> Habitacion:
        return self._habitacion
