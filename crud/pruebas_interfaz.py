#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print "Has clickado el botón %s" % (button.get_label())
        
        
        
# Establecemos la conexi
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
# Creamos el cursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
query = "SELECT * FROM coches"
micursor.execute(query)
resultados = micursor.fetchall()

coche = resultados[0]

linea = coche['marca'] + " , " + coche ['modelo'] + " , " + coche ['color'] + " , " + coche ['matricula'] + " , " + str(coche ['bastidor']) + " , "+ str(coche ['potencia']) + "cv , " + coche ['propietario']
        
builder = Gtk.Builder()
builder.add_from_file("interfaz.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
#mi_etiqueta = builder.get_object("label1")
#mi_etiqueta.set_label(linea) 
window.show_all()



Gtk.main()