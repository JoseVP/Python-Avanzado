
#!/usr/python
# -*- coding: utf-8 -*-
import MySQLdb
# Establecemos la conexi
Conexion = MySQLdb.connect(host='localhost', user='jose',passwd='jo33gu', db='dbpython')
# Creamos el cursor
micursor = Conexion.cursor()
# Ejecutamos un insert directamente
micursor.execute("INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");")
# Lo mismo, pero por medio de una variable
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"
micursor.execute(query)
# Hacemos un commit, por si las moscas
Conexion.commit()
# Ahora vamos a hacer un SELECT
query= "SELECT * FROM Victimas WHERE id=1;"
micursor.execute(query)
# Obtenemos el resultado con fetchone
registro= micursor.fetchone()
# Imprimimos el registro resultante
print registro

# Esto que sigue es para borrar el contenido de la base de datos,
# y que no se nos acumule al ir haciendo pruebas
query= "DELETE FROM Victimas WHERE 1;"
micursor.execute(query)