class Persona:
    def __init__ (self,cliente):
        self.nombre=cliente.get('Nombre')
        self.apellido=cliente.get('Apellido')
    
    def __repr__(self)->str:
        return (f"Nombre:{self.nombre}, Apellido:{self.apellido}")
    

if __name__=='__main__':
    cliente1={'Nombre':'Pepe', 'Apellido': 'Honguito'}
    cliente2={'Nombre':'Pepa', 'Apellido': 'Fernandez'}
    p1=Persona(cliente1)
    p2=Persona(cliente2)
    print(p1)
    print(p2)
