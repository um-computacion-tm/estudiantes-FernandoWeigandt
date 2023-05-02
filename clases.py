class Fecha:
    def __init__(self,anho:int=2023,mes:int=5,dia:int=2):
        self.anho=anho
        self.mes=mes
        self.dia=dia

    def __repr__(self):
        return f'{self.anho}/{self.mes}/{self.dia}'

class Persona:
    def __init__(self,nombre:str, apellido:str, nacimiento:Fecha):
        self.nombre=nombre
        self.apellido=apellido
        self.nacimiento=nacimiento

    def __repr__(self):
        return f'Persona->Nombre={self.nombre} Apellido={self.apellido}, Nacimiento={self.nacimiento}'