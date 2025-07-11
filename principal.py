class estudiante:

    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_fin = nota_final




fin_menu = True

while fin_menu:
    print('\r\t\r\t===Bienvenido usuario:==')
    print('1. Registrar un nuevo estudiante\r\n2. Mostrar lista de estudiantes\r\n3.Buscar estudiante por carné')
    print('4. Calcular promedio de notas')
