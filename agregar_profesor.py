from conexion import conectar



def agregar_profesor():
    con, cursor = conectar()
    nombre = input('Nombre: ')
    materia = input('Materia: ')
    telefono = input('Telefono: ')

    cursor.execute(
        """

        INSERT INTO maestros (nombre, materia, telefono) VALUES (?,?,?)

        """,
        (nombre, materia, telefono)
    )
    con.commit()
    con.close()

