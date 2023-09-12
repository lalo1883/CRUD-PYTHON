from actualizar_profesor import actualizar_profesor
from agregar_profesor import agregar_profesor
from eliminar_profesor import eliminar_profesor
from revisar_profesores import revisar_profesores

# Loop para que el menu se repita

while True:
    print('''
    1) Revisar profesores
    2) Agregar profesor
    3) Actualizar profesor
    4) Eliminar profesor
    5) Salir
    ''')

    opcion = int(input('Opcion: '))

    if opcion == 1:
        revisar_profesores()
    elif opcion == 2:
        agregar_profesor()
    elif opcion == 3:
        actualizar_profesor()
    elif opcion == 4:
        eliminar_profesor()
    elif opcion == 5:
        break
    else:
        print('Opcion no valida')
    


