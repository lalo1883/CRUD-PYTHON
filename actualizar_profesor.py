from conexion import conectar


def actualizar_profesor():
    con, cursor = conectar()

    id = input('Id del profesor a actualizar: ')
    nombre = input('Nuevo nombre: ')
    materia = input('Nueva materia: ')
    telefono = input('Nuevo telefono: ')

    cursor.execute(
        """
        UPDATE maestros SET nombre = ?, materia = ?, telefono = ? WHERE id = ?
        """,
        (nombre, materia, telefono, id)
    )
    con.commit()
    con.close()
    