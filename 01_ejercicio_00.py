'''
Curso : Programacion Basica de Python
Sesion : 03
Tema : Introduccion a Python -  Clases e Instancias
Fecha : 20/11/2020
Author : Jaime Gomez

'''

class Empleado:
    '''
    La clase representa un empleado 
    de Tecsup
    '''
    pass

emp_01 = Empleado()   # Jaime
emp_02 = Empleado()   # Maria
emp_03 = Empleado()   # Eduard

print(emp_01)
print(emp_02)
print(emp_03)


#print("antes", emp_01.nombre) 
emp_01.nombre = "Jaime"  # Crea un atributo en caliente
                         # y le asigna un valor
print("después", emp_01.nombre)


emp_02.cargo = "Directora"  # Crea un atributo en caliente
                            # y le asigna un valor
print("después", emp_02.cargo)


#help(Empleado)

'''
- Crear la clase Empresa
- Crear 2 instancias
- En la 1 instancia crearle el atributo nombre y ruc .
- En la 2 instancia crearle el atributo nombre y direccion .
'''

class Empresa:
    pass

emp01=Empresa()
emp02=Empresa()


emp01.nombre="SalchipapaSA"
emp01.ruc=10457526881
emp02.nombre="HamburguesaSA"
emp02.direccion="av Larco,Miraflores"

print(emp01.nombre)
print(emp02.nombre)


emps = [emp01, emp02]

for emp in emps :
    print(emp.nombre)











