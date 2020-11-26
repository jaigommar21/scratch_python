'''
Ejercicio Adicional:
Crear la clase base Persona , que tenga el atributo
nombre, apellido y dni ; crear la clase hija Estudiante 
que inicialice el nombre, apellido y dni. Agrege el método
obtener_dni en la clase base y usarla desde una instancia
de la clase hija.
'''

# Clase Base
class Persona:

    def __init__(self, nombre, apellido, dni):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
   
    def obtener_dni(self):
        return self.dni

# Clase hija
class Vecino(Persona):
    pass


per_01 = Persona("David","Perez","45698523")
print(per_01.obtener_dni())
vec_01 = Vecino("Joel","Duque","89562355")
print(vec_01.obtener_dni())


'''
Sobrescribir el método obtener_dni en la clase Estudiante
para que siempre retorne "DDD", usarlo en un instancia 
de la clase Estudiante.

'''