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



