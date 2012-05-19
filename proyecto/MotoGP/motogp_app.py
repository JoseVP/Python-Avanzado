#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from gi.repository import Gtk
import subprocess  
    
    

class Moto_GP:
   
    def onVerCircuito(self,menuitem):
        imagen = self.builder.get_object('imagen_circuito')
        circuito = menuitem.get_label()
        imagenes = self.cargar_imagenes(circuito)
        imagen.set_from_file(imagenes[0])
        self.cargar_datos(circuito)
        self.window.set_icon_from_file(imagenes[1])
        bandera = self.builder.get_object('imagen_bandera')
        bandera.set_from_file(imagenes[1])
        self.window.set_title("Circuito de %s" % circuito)
        
    def cargar_datos(self,circuito):
        Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        grandes_premios =  {    'Qatar':'QAT' ,
                                'España':'SPA',
                                'Portugal':'POR',
                                'Francia':'FRA',
                                'Cataluña':'CAT',
                                'Gran Bretaña':'GBR',
                                'Holanda':'NED',
                                'Alemania':'GER',
                                'Italia':'ITA',
                                'Estados Unidos':'USA' ,
                                'Indianapolis':'INP',
                                'Republica Checa':'CZE',
                                'San Marino':'RSM' ,
                                'Aragon':'ARA',
                                'Japon':'JPN' ,
                                'Malasia':'MAL',
                                'Australia':'AUS',
                                'Valencia':'VAL',
                        }
        query = "SELECT * FROM circuitos WHERE gran_premio = '%s'" % grandes_premios[circuito]
        
        micursor.execute(query)
        
        #import ipdb
        #ipdb.set_trace()
        
        datos = micursor.fetchone()


        
        texto_datos = self.builder.get_object("texto_longitud")
        texto_datos.set_label(datos['longitud'])
        texto_datos = self.builder.get_object("texto_ancho")
        texto_datos.set_label(datos['anchura'])
        texto_datos = self.builder.get_object("texto_curvas_der")
        texto_datos.set_label(str(datos['curvas_der']))
        texto_datos = self.builder.get_object("texto_curvas_izq")
        texto_datos.set_label(str(datos['curvas_izq']))
        texto_datos = self.builder.get_object("texto_recta")
        texto_datos.set_label(datos['recta_larga'])
        texto_datos = self.builder.get_object("texto_fecha_const")
        texto_datos.set_label(datos['fecha_construccion'])
        texto_datos = self.builder.get_object("texto_fecha_mod")
        texto_datos.set_label(datos['fecha_modificacion'])
        
        texto_datos = self.builder.get_object("label_nombre")
        texto_datos.set_label('Gran Premio de %s - %s' % (circuito,datos['nombre']))
        
        micursor.close () 
        Conexion.close()
    
    def cargar_imagenes(self,circuito):
        imagenes= {    'Qatar' : 'resources/circuitos/qatar',
                        'España' : 'resources/circuitos/espana',
                        'Portugal' : 'resources/circuitos/portugal',
                        'Francia' : 'resources/circuitos/francia',
                        'Cataluña' : 'resources/circuitos/catalunya',
                        'Gran Bretaña' : 'resources/circuitos/gran_bretanya',
                        'Holanda' : 'resources/circuitos/holanda',
                        'Alemania' : 'resources/circuitos/alemania',
                        'Italia' : 'resources/circuitos/italia',
                        'Estados Unidos' : 'resources/circuitos/estados_unidos',
                        'Indianapolis' : 'resources/circuitos/indianapolis',
                        'Republica Checa' : 'resources/circuitos/republica_checa',
                        'San Marino' : 'resources/circuitos/san_marino',
                        'Aragon' : 'resources/circuitos/aragon',
                        'Japon' : 'resources/circuitos/japon',
                        'Malasia' : 'resources/circuitos/malasia',
                        'Australia' : 'resources/circuitos/australia',
                        'Valencia' : 'resources/circuitos/valencia',
                        }
                        
                        
        return imagenes[circuito]+'-cir.jpg',imagenes[circuito]+'-band.png'
    
    def onActualizarCircuitos(self,menuitem):
       
        dialogo = self.builder.get_object("dialogo_actualizar")        
        respuesta = dialogo.run()
        
        if respuesta == 1 :
            Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
            micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
            query = "DELETE FROM circuitos WHERE 1"
            micursor.execute(query)
            Conexion.commit()
            micursor.close() 
            Conexion.close()
            subproceso = subprocess.Popen(['scrapy','crawl', 'circuitos','--nolog'])
            subprocess.Popen.wait(subproceso)   

            
            texto = self.builder.get_object("label_actualizando")
            texto.set_label("Informacion de los circuitos Actualizada")
            boton = self.builder.get_object("button_aceptar")
            boton.hide()
            boton = self.builder.get_object("button_cancelar")
            boton.hide()
        else:
            dialogo.destroy()
        
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("interfaz.glade")
        self.handlers = {   "onDeleteWindow": Gtk.main_quit,
                            "onVerCircuito": self.onVerCircuito,
                            "onActualizarCircuitos":self.onActualizarCircuitos,
                            
                            }                
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window1")
        self.window.show_all()
        
        
         
    
def main():
    window = Moto_GP()
    Gtk.main()

    return 0

if __name__ == '__main__':
    main()
