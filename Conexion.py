import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(host="localhost",port=3306,user="root",password="C1sc0conpa",db="akinator")
        if conexion.is_connected():
            return conexion
    except Error as ex:
        print("Error durante la conexion",ex)