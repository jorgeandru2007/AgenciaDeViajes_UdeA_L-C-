'''
Autor: Jorge Ruiz
Fecha de creación: 21/10/2024
Clase: Habitacion, esta clase permitira a la clase Hotel tener una lista habitaciones con sus propias caracteristicas
'''
class Habitacion():
    _id: int
    _capacidad: int
    _descripcion: str
    _precio_noche: float
    _disponible: bool

    def __init__(self, id, cantidad = 0, descripcion = "", precio_noche = 0):
        self._id = id
        self._capacidad = cantidad
        self._descripcion = descripcion
        self._precio_noche = precio_noche

    def get_id(self) -> int:
        return self._id

    def get_capacidad(self) -> int:
        return self._capacidad

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_precio_noche(self) -> float:
        return self._precio_noche