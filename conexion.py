import sqlite3

def conectar():
    con = sqlite3.connect('maestros.db')
    cursor = con.cursor()
    return con, cursor
