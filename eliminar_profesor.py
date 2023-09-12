from conexion import conectar



def eliminar_profesor():
    con, cursor = conectar()

    id = input('Id del profesor a eliminar: ')

    cursor.execute(
        """
        DELETE FROM maestros WHERE id = ?
        """,
        (id,)
    )
    con.commit()
    con.close()