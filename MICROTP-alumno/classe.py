class Alumno:
    def __init__(self, nombre, edad, curso, notas):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.notas = notas

    def getInfo(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Curso:", self.curso)

    def getNotas(self):
        if self.notas == []:
            print("No hay notas.")
        else:
            for i in range(len(self.notas)):
                print(i, "-", self.notas[i])

    def setNota(self, nota):
        if nota >= 1 and nota <= 10:
            self.notas.append(nota)
            print("Nota cargada.")
        else:
            print("La nota debe estar entre 1 y 10.")


def menu():
    print(" menu ")
    print("1. Mostrar la información.")
    print("2. Mostrar las notas.")
    print("3. Ingresar notas.")
    print("4. Salir.")

    opcion = int(input("Ingrese una opción: "))
    return opcion