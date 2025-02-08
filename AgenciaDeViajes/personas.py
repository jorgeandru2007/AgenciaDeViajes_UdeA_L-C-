import numpy as np 
from persona import Persona

'''
Autor: Jorge Ruiz
Fecha de creación: 29/11/2024
Clase: Personas para administrar el arreglo personas y agregarlas de manera eficiente
'''
class Personas():
    _personas: Persona
    _cant_personas: int
    _max_personas: int

    def __init__(self, max_personas):
        self._cant_personas = 0
        self._max_personas = max_personas
        self._personas = np.full((max_personas), fill_value = None, dtype=object)
    
    def agregar_persona(self, persona):
        self._personas[self._cant_personas] = persona
        self._cant_personas += 1

    
    #Método Registrar Usuario
    def registrar_persona(self, rol) -> bool:

        if (self._cant_personas < self._max_personas):

            self._personas[self._cant_personas] = Persona()
            self._personas[self._cant_personas].registrar_datos(rol)
            self._personas[self._cant_personas].set_rol(rol)
            self._cant_personas += 1
            
            return True
        
        else:
            return False
    
    def buscar_persona_documento(self, documento) -> int:
        for i in range(0, self._cant_personas):
            if (self._personas[i].get_documento() == int(documento)):
                return i
        return None

    
    #Metodos Getters

    def get_personas(self) -> object:
        return self._personas

    def get_cant_personas(self) -> int:
        return self._cant_personas
    

    #Metodos Setters

    def set_personas(self, personas):
        self._personas = personas
