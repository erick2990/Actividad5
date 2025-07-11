from gtweak.utils import execute_subprocess

estudiantes = []

class estudiante:

    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_fin = nota_final

    def presentar_estudiante(self):
        print(f'Nombre: {self.nombre} carné: {self.carne} carrera: {self.carrera} nota Final: {self.nota_fin}')

    def nota_est(self):
        return self.nota_fin
    def nombre(self):
        return self.nombre()


def registrar_estudiante():
        nombre = input('Ingrese el nombre del estudiante: ')
        carne = int(input('Ingrese el carné del estudiante: '))
        carrera = input('Ingrese la carrera del estudiante: ')
        nota_final = int(input('Ingrese la nota del estudiante: '))
        estudiante_tmp = estudiante(nombre, carne, carrera, nota_final)
        estudiantes.append(estudiante_tmp) #se añade a la lista
        print('Añadido con exito!!!')


def mostrar_estudiante():
    if len(estudiantes) > 0:
        for tmp in estudiantes:
            tmp.presentar_estudiante()
    else:
        print('No hay estudiantes registrados aún...')

def calculo_prom():
    prom =0
    if len(estudiantes)>0:
        print('Calculando el promedio general de estudiantes: ')
        for nota in estudiantes:
            prom = prom + nota.nota_est()

        print(f'El promedio general de todos lo estudiantes es: {prom}')
    else:
        print('No hay estudiantes registrados aún')

def buscar_estudiante():
    encontrado = False
    if len(estudiantes)>0:
        nombre_buscar = input('Ingrese el nombre del estudiante que desee buscar: ')
        for busqueda in estudiantes:
            if busqueda.nombre() == nombre_buscar:
                print('El estudiante que usted busca esta en la lisa')
                encontrado= True
                break

        if encontrado:
            print('El estudiante se encontro exitosamente')
        else:
            print('El estudiante no se encuentra en la lista')

    else:
        print('No hay estudiantes registrados aún')


fin_menu = True

while fin_menu:
    try:
        print('\r\t\r\t===Bienvenido usuario:==')
        print('1. Registrar un nuevo estudiante\r\n2. Mostrar lista de estudiantes\r\n3.Buscar estudiante por carné')
        print('4. Calcular promedio de notas\r\n0.Salir')
        op = int(input('Seleccione una opcion: '))
        match op:
            case 0:
                print('Adios gracias por usar el sistema')
                fin_menu = False
            case 1:
                registrar_estudiante()
            case 2:
                mostrar_estudiante()
            case 3:
                buscar_estudiante()
            case 4:
                calculo_prom()
            case _:
                print('Error presiono una tecla incorrecta')

    except ValueError:
        print('Error dato invalido por favor vuelva a intentarlo')

