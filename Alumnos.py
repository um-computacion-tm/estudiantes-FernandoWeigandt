class alumno:
    def __init__(self,nombre,edad,sexo,):
       self.nombre=nombre
       self.edad=edad
       self.sexo=sexo


    def cambiar_nombre(self,nuevo_nombre):
        self.nombre=nuevo_nombre

    def cambiar_edad(self):
        self.edad+=1

    def establecer_sexo(self,sexo_definido):
        self.sexo=sexo_definido


print('Digame su nombre:')
nombre=input()
print('Cual es tu edad:')
edad=int(input())
print('Defina su sexo?')
sexo=input()
alumno1=alumno(nombre,edad,sexo)

alumno1.cambiar_nombre('Victor')
alumno1.cambiar_edad()
alumno1.establecer_sexo('Helicoptero Apache')
print(alumno1.nombre, alumno1.edad,alumno1.sexo)
