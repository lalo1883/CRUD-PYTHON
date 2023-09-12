from conexion import conectar


def revisar_profesores():
    con, cursor = conectar()
    cursor.execute(
        """
        SELECT * FROM maestros
        """
    )

    profesores = cursor.fetchall()
    for profesor in profesores:
        print(profesor)
    con.commit()
    con.close()