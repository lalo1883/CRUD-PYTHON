from conexion import conectar

def crear_tabla():
    con, cursor = conectar()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS maestros (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            materia TEXT,
            telefono TEXT
        )'''
    )
    con.commit()
    con.close()


