
import numpy as np

'''
Autor: Jorge Ruiz
Fecha de creación: 21/10/2024
Clase: Hotel, la cual permitira hacer registros basados en los hoteles, asi como conocer si tienen habitaciones disponibles
'''
class Hotel():
    _nombre: str
    _ciudad: str
    _direccion: str
    _telefono: int
    _e_mail: str
    _categoria: str
    _cant_habitaciones: int
    _habitaciones: np.array

    def __init__(self, nombre = "", ciudad = "", direccion = "", telefono = 0, e_mail = "", categoria = "", cant_habitaciones = 1):
        self._nombre = nombre
        self._ciudad = ciudad
        self._direccion = direccion
        self._telefono = telefono
        self._e_mail = e_mail
        self._categoria = categoria
        self._cant_habitaciones = cant_habitaciones
        self._habitaciones = np.full((cant_habitaciones), fill_value = None, dtype=object)

    #Metodos Get
    def get_nombre(self) -> str:
        return self._nombre

    def get_ciudad(self) -> str:
        return self._ciudad

    def get_direccion(self) -> str:
        return self._direccion

    def get_telefono(self) -> int:
        return self._telefono

    def get_e_mail(self) -> str:
        return self._e_mail

    def get_categoria(self) -> str:
        return self._categoria

    def get_cant_habitaciones(self) -> int:
        return self._cant_habitaciones

    def get_habitaciones(self) -> np.array:
        return self._habitaciones

    #Metodos Setters
    def set_habitaciones(self, habitaciones):
        self._habitaciones = habitaciones
