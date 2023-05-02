class Persona:
    def __init__ (self,nombre:str=None, apellido:str=None, diccionario:dict=None):
        if diccionario is not None:
            self.apellido=diccionario.get('apellido')
            self.nombre=diccionario.get('nombre')
        if nombre is not None:
            self.nombre=nombre
        if apellido is not None:
            self.apellido=apellido
        
    def __repr__(self):
        return f'Nombre:{self.nombre} Apellido:{self.apellido}'

persona_json_1={'nombre':'Indiana', 'apellido':'Jones'}
persona_json_2={'nombre':'Steve', 'apellido':'Pingers'}

if __name__=='__main__':
    persona_1=Persona(diccionario=persona_json_1)
    persona_2=Persona(nombre='Tony',apellido='Stark')
    print(persona_1)
    print(persona_2)