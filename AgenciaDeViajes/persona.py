"""Autor: Diego Alejandro Vergara Ruiz"""


class Persona():

    #Declaración de variables
    _nombre: str
    _documento: int
    _tipo_documento: str
    _telefono: int
    _email: str
    _nombre_contacto_emergencia: str
    _telefono_contacto_emergencia: int
    _contrasenia: str
    _categoria: str
    _rol: int #1: Cliente, 2: Empleado, 3: Administrador
    _num_reservas: int

    #Metodo constructor de la clase Persona
    def __init__(self, nombre = "", documento = "", tipo_documento = "", telefono = 0, email = "", nombre_contacto_emergencia = "", telefono_contacto_emergencia = 0, contrasenia = "", rol = 1, num_reservas = 0):
        self._nombre = nombre
        self._documento = documento
        self._tipo_documento = tipo_documento
        self._telefono = telefono
        self._email = email
        self._nombre_contacto_emergencia = nombre_contacto_emergencia
        self._telefono_contacto_emergencia = telefono_contacto_emergencia
        self._contrasenia = contrasenia
        self._categoria = "Regular" #Se establece la categoría "Regular" como valor determinado, dado que en una primera instancia todos los clientes son de esta categoría.
        self._rol = rol
        self._num_reservas = num_reservas

    #Metodos de la clase Persona

    #Método Registrar Datos
    def registrar_datos(self, rol):
        self._nombre = str(input("Ingrese su nombre completo: "))

        """Se genera una estructura "según sea" dentro de una validación,
        dado que se le pretende mostrar al usuario una lista de opciones con el fin de hacer la elección del documento."""

        while(True):
            opc = int(input("Seleccione el tipo de documento: \n1: Cédula de ciudadanía\n2: Tarjeta de identidad\n3: Cédula de extranjería\n4: Pasaporte\n"))
            if (opc != 1 and opc !=2 and opc != 3 and opc != 4):
                print("Error: Valor no válido")
            else:
                match opc:
                    case 1:
                        self._tipo_documento = "Cédula de ciudadanía"
                        break
                    case 2:
                        self._tipo_documento = "Tarjeta de identidad"
                        break
                    case 3:
                        self._tipo_documento = "Cédula de extranjería"
                        break
                    case 4:
                        self._tipo_documento = "Pasaporte"

                        break

        self._documento = int(input("Ingrese su número de documento: "))
        self._telefono = int(input("Ingrese su número de teléfono: "))

        #Se valida el correo electrónico ingresado por el usuario
        correo_valido = False
        while(not correo_valido):
            self._email = str(input("Ingrese su correo electrónico: "))
            if "@" in self._email and "." in self._email:
                correo_valido = True
            else:
                print("Error: Correo electrónico inválido")

        self._nombre_contacto_emergencia = str(input("Ingrese el nombre de su contacto de emergencia: "))
        self._telefono_contacto_emergencia = int(input("Ingrese el número de teléfono de su contacto de emergencia: "))

        #Se valida la contraseña ingresada por el usuario (debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula, un número y un caracter especial)
        contrasenia_valida = False
        while(not contrasenia_valida):
            self._contrasenia = str(input("Ingrese una contraseña que contenga al menos una mayúscula, una minúscula, un número y un carácter especial(@, #, $, %): "))
            if len(self._contrasenia) >= 8 and "A" <= self._contrasenia <= "Z" and "a" <= self._contrasenia <= "z" and "0" <= self._contrasenia <= "9" and "@" in self._contrasenia or "#" in self._contrasenia or "$" in self._contrasenia or "%" in self._contrasenia:
                contrasenia_valida = True
            else:
                print("Error: Contraseña inválida")
        
        self._rol = rol

        print("Datos registrados exitosamente")

    #Métodos Getter
    def get_nombre(self) -> str:
        return self._nombre

    def get_tipo_documento(self) -> str:
        return self._tipo_documento

    def get_documento(self) -> int:
        return self._documento

    def get_telefono(self) -> int:
        return self._telefono

    def get_email(self) -> str:
        return self._email

    def get_nombre_contacto_emergencia(self) -> str:
        return self._nombre_contacto_emergencia

    def get_telefono_contacto_emergencia(self) -> int:
        return self._telefono_contacto_emergencia

    def get_contrasenia(self) -> str:
        return self._contrasenia

    def get_categoria(self) -> str:
        return self._categoria

    def get_rol(self) -> int:
        return self._rol

    def get_num_reservas(self) -> int:
        return self._num_reservas


    #Métodos Setter
    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_tipo_documento(self, tipo_documento: str):
        self._tipo_documento = tipo_documento

    def set_documento(self, documento: int):
        self._documento = documento

    def set_telefono(self, telefono: int):
        self._telefono = telefono

    def set_email(self, email: str):
        self._email = email

    def set_nombre_contacto_emergencia(self, nombre_contacto_emergencia: str):
        self._nombre_contacto_emergencia = nombre_contacto_emergencia

    def set_telefono_contacto_emergencia(self, telefono_contacto_emergencia: int):
        self._telefono_contacto_emergencia = telefono_contacto_emergencia

    def set_contrasenia(self, contrasenia: str):
        self._contrasenia = contrasenia

    def set_categoria(self, categoria: str):
        self._categoria = categoria

    def set_rol(self, rol: int):
        self._rol = rol

    def set_num_reservas(self, num_reservas: int):
        self._num_reservas = num_reservas


    #Método Promocionar Cliente
    def promocionar_cliente(self):
        #cliente = Persona()
        #documento_cliente = int(input("Ingrese el número de documento del cliente a promocionar: "))
        #if (documento_cliente == cliente.get_documento()):
        # Se comprueba que el cliente sea real
        print("La categoría actual del cliente es: ", self.get_categoria())

        nueva_categoria = int(input("Seleccione la nueva categoría del cliente: \n1: Regular\n2: Plata\n3: Oro\n4: Platino\n"))
        match nueva_categoria:
            case 1:
                self.set_categoria("Regular")
            case 2:
                self.set_categoria("Plata")
            case 3:
                self.set_categoria("Oro")
            case 4:
                self.set_categoria("Platino")

        print("La nueva categoría del cliente es: ", self.get_categoria())




    #Método Cambiar Contraseña
    def cambiar_contrasenia(self, usuario):
        usuario = Persona()
        documento_usuario = int(input("Ingrese su número de documento: "))
        if (documento_usuario == usuario.get_documento()):
            contrasenia_valida = False
            while(not contrasenia_valida):
                contrasenia_actual = str(input("Ingrese su contraseña actual: "))
                if (contrasenia_actual == usuario.get_contrasenia()):
                    contrasenia_nueva = str(input("Ingrese su nueva contraseña: "))
                    usuario.set_contrasenia(contrasenia_nueva)
                    contrasenia_valida = True
                else:
                    print("Error: Contraseña incorrecta")
        else:
            print("Error: Número de documento incorrecto")






    # Método para mostrar los datos de un usuario

    def mostrar_datos(self):

        if(self.get_rol() == 1):

            print(f"""
                  Información del Cliente:

            1. Nombre: {self.get_nombre()}
            2. Documento: {self.get_documento()}
            3. Tipo de documento: {self.get_tipo_documento()}
            4. Teléfono: {self.get_telefono()}
            5. Correo electrónico: {self.get_email()}
            6. Nombre del contacto de emergencia: {self.get_nombre_contacto_emergencia()}
            7. Teléfono del contacto de emergencia: {self.get_telefono_contacto_emergencia()}
            8. Categoría: {self.get_categoria()}
            9. Número de reservas: {self.get_num_reservas()}
            """)

        elif(self.get_rol() == 2):

            print(f"""
                  Información del Empleado:

            1. Nombre: {self.get_nombre()}
            2. Documento: {self.get_documento()}
            3. Tipo de documento: {self.get_tipo_documento()}
            4. Teléfono: {self.get_telefono()}
            5. Correo electrónico: {self.get_email()}
            """)

        elif(self.get_rol() == 3):

            print(f"""
                  Información del Administrador:

            1. Nombre: {self.get_nombre()}
            2. Documento: {self.get_documento()}
            3. Tipo de documento: {self.get_tipo_documento()}
            4. Teléfono: {self.get_telefono()}
            5. Correo electrónico: {self.get_email()}
            """)


    #Método para consultar la información de un cliente

    def consultar_informacion_cliente(self, usuarios, reservas):

        documento_cliente = int(input("Ingrese el número de documento del cliente: "))

        for usuario in usuarios:
            if (usuario.get_documento() == documento_cliente):
                usuario.mostrar_datos()

                print("\nReservas realizadas por el cliente: \n")
                reservas_realizadas = False
                for reserva in reservas:
                    if(reserva.id_cliente == documento_cliente):
                        reserva.mostrar_reservas()
                        reservas_realizadas = True

                if(not reservas_realizadas):
                    print("El cliente no ha realizado reservas")

            else:
                print("Error: Cliente no encontrado")
