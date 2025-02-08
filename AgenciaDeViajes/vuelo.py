import datetime as dt


class Vuelo():
    '''
    Autor: Jorge Ruiz
    Fecha de creación: 24/10/2024
    Clase: Vuelos
    '''
    _numero_vuelo: int
    _ciudad_origen: str
    _ciudad_destino: str
    """
    uso de la libreria datetime de python como dt,
    para crear un objeto que guarde la hora y minutos se usara el subobjeto time,
    el cual almacena hora, minuto y segundos,
    para instanciarlo hacerlo de la siguiente forma: dt.time(<hora>,<Minutos>)
    !Importante a la hora de comparar usar un objeto dt.time y no un simple string
    """
    _hora_salida: dt.time

    _capacidad: int
    _nombre_piloto: str

    def __init__(self, numero_vuelo=0, ciudad_origen="", ciudad_destino="", hora_salida = dt.time(0,0), capacidad=0, nombre_piloto=""):
        self._numero_vuelo = numero_vuelo
        self._ciudad_origen = ciudad_origen
        self._ciudad_destino = ciudad_destino
        self._hora_salida = hora_salida
        self._capacidad = capacidad
        self._nombre_piloto = nombre_piloto

    def get_numero_vuelo(self) -> int:
        return self._numero_vuelo

    def get_ciudad_origen(self) -> str:
        return self._ciudad_origen

    def get_ciudad_destino(self) -> str:
        return self._ciudad_destino

    def get_hora_salida(self) -> dt.time:
        return self._hora_salida

    def get_capacidad(self) -> int:
        return self._capacidad

    def get_nombre_piloto(self) -> str:
        return self._nombre_piloto
