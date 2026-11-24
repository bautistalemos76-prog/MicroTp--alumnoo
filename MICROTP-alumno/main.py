from clase import *

alumnoo = alumno(
    input("Ingrese nombre del estudiante "),
    input("Ingrese edad: "),
    input("Ingrese curso: "),
    [],
)
op = 0
while op != 4:
    op = menu()
    if op == 1:
        alumnoo.getInfo()
    elif op == 2:
        alumnoo.getNotas()
    elif op == 3:
        nota = int(input("Ingrese una nota: "))
        alumnoo.setNota(nota)
    elif op == 4:
        print("Programa finalizado.")
    else:
        print("Opción incorrecta.")