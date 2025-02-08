from hotel import Hotel
from vuelo import Vuelo

class Paquete():
    '''
    Autor: Jorge Ruiz
    Fecha de creación: 19/11/2024
    Clase: Paquete turistico
    '''
    _vuelo: Vuelo
    _hotel: Hotel

    def __init__(self, vuelo = None, hotel = None):
        self._vuelo = vuelo
        self._hotel = hotel

    def get_vuelo(self) -> Vuelo:
        return self._vuelo

    def get_hotel(self) -> Hotel:
        return self._hotel
