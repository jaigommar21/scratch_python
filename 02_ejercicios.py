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

print(Persona.listado_de_personas)
