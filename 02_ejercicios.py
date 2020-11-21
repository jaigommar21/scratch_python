'''
Crear la clase Persona

- Crear atributos:
   * nombre
   * apelido
   * dni

- Crear atributo de clase
   * pais
   * listados_de_personas

- crear un metodo que me obtenga
  el [apellido : dni] , por ejemplo
  "[Gomez : 1234567]"

- Cada vez que se instancia un clase, 
  se debe agregar el nombre de la persona
  a un atributo de clase llamado listado_de_personas

'''

class Persona:

    pais="Perú"
    listado_de_personas=[]

    def __init__(self,nombre,apellido,dni):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        Persona.listado_de_personas.append(nombre)

    def obtener_info(self):
        cadena=self.apellido+":"+self.dni
        return cadena

per1=Persona("Jorge","Garcia","52565988")
combina=per1.obtener_info()
print(combina)

per2=Persona("Jaime","Perez","12345646")

Persona("Milagros","Huaman","1234588")

print(Persona.listado_de_personas)

nombre = "Jaime"
print(len(nombre))
print(nombre.upper())


class SesionDeClase:
    pais = ""
    listado_personas = []
    def __init__(self, nombre, apellido,dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        SesionDeClase.listado_personas.append(nombre)
    def datos(self):
        return self.apellido+":"+self.dni
sesion1 = SesionDeClase("Juan","Perez","12345678")
sesion2 = SesionDeClase("Miguel","Gomez","10000001")
sesion3 = SesionDeClase("Celeste","Alva","20000002")
sesion1.datos()
sesion2.datos()
sesion3.datos()
print(SesionDeClase.listado_personas)


