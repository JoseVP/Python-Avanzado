#!/usr/python
# -*- coding: utf-8 -*-

import MySQLdb
import os

def clear():
    os.system(['clear','cls'][os.name == 'nt'])

def Menu():
    
    opcion= 0 
    opciones = [1,2,3]
    while( opcion not in opciones):
        print ""
        print "********************************************"
        print "*---------- Victimas  de CONAN ------------*"
        print "********************************************"
        print "--> Que desea hacer:                        "
        print "    1) Insertar nueva Victima               "
        print "    2) Ver Victimas de Conan                "
        print "    3) Salir                                "
        print "********************************************"
        
        opcion=int(raw_input("  Opcion: "))
        print "********************************************"
        clear()
    return opcion


# Establecemos la conexi
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
# Creamos el cursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

#Comprobamos si ya hay datos en la tabla de victimas

query = "SELECT id FROM Victimas"
micursor.execute(query)
resultados = micursor.fetchall()
# Si ya hay datos ordenamos los ids para ver el numero de id mas alto
# esto seria mucho mas simple con la sentencia SQL "SELECT id FROM Victimas ORDER BY id"
if resultados:
    lista_ids = []

    for res in resultados:
        lista_ids.append( int(res['id']) )

    lista_ids.sort()
    primer_id = lista_ids[-1]
    
else:
    primer_id = 0



querys = {  "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+1) + ", \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");",
            "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+2) + ", \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");",
            "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+3) + ", \"Bruja Malvada\",\"Brujisimas\",\"Espadazo en la cabeza\");",
            "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+4) + ", \"Demonio\",\"Rey del infierno\",\"Escupitajo\");",
            "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+5) + ", \"Gemelo Malvado\",\"Anticonans\",\"Susto\");",
            "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+6) + ", \"Spiderman\",\"Americanos\",\"Cucal\");",
            "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+7) + ", \"Superman\",\"Americanos\",\"Criptonita\");",
            "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+8) + ", \"2 Caras\",\"Americanos\",\"Guantazo\");",
            "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+9) + ", \"El Bute\",\"Ladronzuelos\",\"Hachazo\");",
            "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(primer_id+10) + ", \"Frankestein\",\"Muertos Vivientes\",\"Espadazo\");"
        }

for query in querys:
    micursor.execute(query)
    
# Hacemos un commit, por si las moscas
Conexion.commit()
nuevo_id = primer_id +10

 


opcion = Menu()
        
while (opcion != 3):
   
    
    if(opcion == 1):
        victima = {}
        print "Introduzca los siguientes datos de la nueva victima de Conan:"
        victima['Nombre']= raw_input("Nombre: ")
        victima['Profesion'] = raw_input("Profesion: ")
        victima['Muerte'] = raw_input("Muerte: ")
        
        if not victima['Nombre'] or not victima['Profesion'] or not victima['Muerte']:
            print "*** ERROR: Uno de los campos estaba vacio, la insercion ha sido cancelada ***"
        else:
            nuevo_id=nuevo_id+1
            query = "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(nuevo_id) + ", \"" + victima['Nombre'] + "\",\"" + victima['Profesion'] + "\",\"" + victima['Muerte'] +"\");"
            micursor.execute(query)
            print "Inserción realizada correctamente"
            
    elif (opcion == 2):
        print "Victimas de Conan: "
        query = "SELECT * FROM Victimas"
        micursor.execute(query)
        datos = micursor.fetchall()
        for vict in datos:
            print "     * " + vict['Nombre'] + " del tipo " + vict['Profesion'] + " que murió por " +  vict['Muerte']
     
   
    opcion = Menu()
    
 



print " RESULTADO FINAL DE LAS VICTIMAS DE CONAN: "
query = "SELECT * FROM Victimas"
micursor.execute(query)
datos = micursor.fetchall()
for vict in datos:
    print "     ->  " + vict['Nombre'] + " del tipo " + vict['Profesion'] + " que murió por " +  vict['Muerte']

Conexion.commit()
print " ** COMMIT REALIZADO ** "
print " ** SALIENDO DE LA BASE DE DATOS **" 


#cerramos y limpiamos
micursor.close () 
Conexion.close()