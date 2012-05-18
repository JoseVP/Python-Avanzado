#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from gi.repository import Gtk
   
    
    

class Gestor_Coches:
   
        
        
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("interfaz.glade")
        self.handlers = {   "onDeleteWindow": Gtk.main_quit,
                            "onInsertar": self.onInsertar,
                            "onEditar": self.onEditar,
                            "onBuscar": self.onBuscar,
                            "onEliminar": self.onEliminar,
                            "onPasarPagina": self.onPasarPagina,
                            "onSeleccionar": self.onSeleccionar,
                            "onConfirmar": self.onConfirmar,
                            }                
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window1")
        self.cargar_db()
        self.window.show_all()
        
        
         
    def onInsertar(self, menuitem):
        self.accion_actual = 'insertar'
        etiqueta = self.builder.get_object('label_accion')
        etiqueta.set_label('Introduzca los datos del nuevo coche')
        boton = self.builder.get_object('boton_confirmar')
        boton.set_label('Añadir')

        
        
    def onEditar(self, menuitem):
        self.accion_actual = 'editar'
        pass
    
    def onBuscar(self, menuitem):
        self.accion_actual = 'buscar'
        pass
    
    def onEliminar(self, menuitem):
        self.accion_actual = 'eliminar'
        pass
        
    def onPasarPagina(self,boton):
        pass
    
    def onSeleccionar(self, boton):
        pass
        
    def onConfirmar(self,boton):
        
        if self.accion_actual == "insertar":
            
            query = "INSERT INTO coches (marca,modelo,color,potencia,bastidor,matricula,propietario) VALUES ('"
            Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan') 
            micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
            
            
            entrada = self.builder.get_object("entry_marca6")
            query += entrada.get_text() + "','"

            entrada = self.builder.get_object("entry_modelo6")
            query += entrada.get_text() + "','" 
            entrada = self.builder.get_object("entry_color6")
            query += entrada.get_text() + "','"

            entrada = self.builder.get_object("entry_potencia6")
            query += entrada.get_text() + "','"

            entrada = self.builder.get_object("entry_bastidor6")
            query += entrada.get_text() + "','"

            entrada = self.builder.get_object("entry_matricula6")
            query += entrada.get_text() + "','"

            entrada = self.builder.get_object("entry_propietario6")
            query += entrada.get_text() + "')"
            
            print query
            micursor.execute(query)
            Conexion.commit()
            #cerramos la conexión con la base de datos
            micursor.close () 
            Conexion.close()
            
            
            entrada = self.builder.get_object("entry_marca6")
            entrada.set_text('')

            entrada = self.builder.get_object("entry_modelo6")
            entrada.set_text('')
            entrada = self.builder.get_object("entry_color6")
            entrada.set_text('')

            entrada = self.builder.get_object("entry_potencia6")
            entrada.set_text('')

            entrada = self.builder.get_object("entry_bastidor6")
            entrada.set_text('')

            entrada = self.builder.get_object("entry_matricula6")
            entrada.set_text('')

            entrada = self.builder.get_object("entry_propietario6")
            entrada.set_text('')
            
            
            
            self.cargar_db()
            
        pass
    
    
    def cargar_db(self, query = "SELECT * FROM coches ORDER BY id ASC"):
        Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        micursor.execute(query)
        lista_coches = micursor.fetchall()
        #cerramos la conexión con la base de datos
        micursor.close () 
        Conexion.close()
        
        #separamos la lista de coches en grupos de 5 para paginarlos
        
        self.paginas_coches = []
        
        i = 1
        pagina= []
        for coche in lista_coches:
            if ( i % 6 != 0):
                pagina.append(coche)
            else:
                self.paginas_coches.append(pagina)
                pagina = []
            i = i+1
            
        self.paginas_coches.append(pagina)
        
        self.numero_paginas = len(self.paginas_coches)

        self.pagina_actual = 0
        self.cargar_pagina_coches(self.pagina_actual)
        
        
        
    def cargar_pagina_coches(self,num_pag):
        etiqueta_paginas = self.builder.get_object('label_num_pag')
        etiqueta_paginas.set_label(str(num_pag)+'/%s' % self.numero_paginas)
        
        num = 1
        for coche in self.paginas_coches[num_pag]:
            entrada = self.builder.get_object("entry_id%s" % num)
            entrada.set_text(str(coche['id']) )
            
            entrada = self.builder.get_object("entry_marca%s" % num)
            entrada.set_text(coche['marca']) 

            entrada = self.builder.get_object("entry_modelo%s" % num)
            entrada.set_text(coche['modelo']) 
            entrada = self.builder.get_object("entry_color%s" % num)
            entrada.set_text(coche['color']) 

            entrada = self.builder.get_object("entry_potencia%s" % num)
            entrada.set_text(str(coche['potencia']) + "cv")

            entrada = self.builder.get_object("entry_bastidor%s" % num)
            entrada.set_text(str(coche['bastidor']))

            entrada = self.builder.get_object("entry_matricula%s" % num)
            entrada.set_text(coche['matricula'])

            entrada = self.builder.get_object("entry_propietario%s" % num)
            entrada.set_text(coche['propietario'])
            
            num = num + 1

        
        

## Creamos el cursor
#micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
#query = "SELECT * FROM coches"
#micursor.execute(query)
#resultados = micursor.fetchall()

#coche = resultados[0]


        
#builder = Gtk.Builder()
#builder.add_from_file("interfaz.glade")
#builder.connect_signals(Handler())

#window = builder.get_object("window1")

#num = '1';
#entrada = builder.get_object("entry_id%s" % num)
#entrada.set_text(str(coche['id']) )

#entrada = builder.get_object("entry_marca%s" % num)
#entrada.set_text(coche['marca']) 

#entrada = builder.get_object("entry_modelo%s" % num)
#entrada.set_text(coche['modelo']) 
#entrada = builder.get_object("entry_color%s" % num)
#entrada.set_text(coche['color']) 

#entrada = builder.get_object("entry_potencia%s" % num)
#entrada.set_text(str(coche['potencia']) + "cv")

#entrada = builder.get_object("entry_bastidor%s" % num)
#entrada.set_text(str(coche['bastidor']))


#entrada = builder.get_object("entry_matricula%s" % num)
#entrada.set_text(coche['matricula'])

#entrada = builder.get_object("entry_propietario%s" % num)
#entrada.set_text(coche['propietario'])


def main():
    window = Gestor_Coches()
    Gtk.main()

    return 0

if __name__ == '__main__':
    main()
