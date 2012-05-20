#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from gi.repository import Gtk
import subprocess  
    
    

class Moto_GP:
   
    def cargar_circuitos_iniciales(self):
            self.carreras =  ['Qatar',
                        'España',
                        'Portugal',
                        'Francia',
                        'Cataluña',
                        'Gran Bretaña',
                        'Holanda',
                        'Alemania',
                        'Italia',
                        'Estados Unidos' ,
                        'Indianapolis',
                        'Republica Checa',
                        'San Marino' ,
                        'Aragon',
                        'Japon' ,
                        'Malasia',
                        'Australia',
                        'Valencia']
                        
            i=1
            for carrera in self.carreras:
                boton = self.builder.get_object('button%s'%i)
                boton.set_label(carrera)
                if(i!=1):
                    bandera = self.builder.get_object('imagen_boton_bandera%s'% (i-1))
                else:
                    bandera = self.builder.get_object('imagen_boton_bandera')
                    
                imagenes = self.cargar_imagenes(carrera)
                bandera.set_from_file(imagenes[1])
                i+=1
                
    def onInitialCircuit(self,boton):
        self.onVerCircuito(boton)
        self.window_inicial.hide()
        self.window.show_all()
   
    def onVerCircuito(self,menuitem):
        imagen = self.builder.get_object('imagen_circuito')
        circuito = menuitem.get_label()
        imagenes = self.cargar_imagenes(circuito)
        imagen.set_from_file(imagenes[0])
        self.cargar_informacion_circuito(circuito)
        self.cargar_records_circuito(circuito)
        self.window.set_icon_from_file(imagenes[1])
        bandera = self.builder.get_object('imagen_bandera')
        bandera.set_from_file(imagenes[1])
        self.window.set_title("Circuito de %s" % circuito)
        
        
    def cargar_informacion_circuito(self,circuito):
        Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        
        query = "SELECT * FROM circuitos WHERE gran_premio = '%s'" % self.grandes_premios[circuito]
        
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
        
        
    def cargar_records_circuito(self,circuito):
        Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        
        query = "SELECT id FROM circuitos WHERE gran_premio = '%s'" % self.grandes_premios[circuito]
        micursor.execute(query)
        id_circuito= micursor.fetchone()
        
        query = "SELECT * FROM records_circuitos WHERE id_circuito = '%s' ORDER BY categoria DESC" % id_circuito['id']
        micursor.execute(query)
        records = micursor.fetchall()
        grid = self.builder.get_object("grid_records")
        cat_act = records[0]['categoria']
        i = 2
        for record in records:
            if (record['categoria'] != cat_act):
                if(record['categoria'] == 'MotoGP'):
                    i=2
                elif (record['categoria'] == 'Moto2'):
                    i=7
                elif (record['categoria'] == '125cc'):
                    i=12
                cat_act = record['categoria']
            label = self.builder.get_object("label_%s_%s" %(i,1))
            if (record['temporada'] != 0):
                label.set_label(str(record['temporada']))
            else:
                label.set_label('')
            
            label = self.builder.get_object("label_%s_%s" %(i,2))
            label.set_label(record['piloto'])
            
            label = self.builder.get_object("label_%s_%s" %(i,3))
            label.set_label(record['motocicleta'])
            
            label = self.builder.get_object("label_%s_%s" %(i,4))
            label.set_label(record['tiempo'])
            
            label = self.builder.get_object("label_%s_%s" %(i,5))
            label.set_label(record['velocidad'])

            i+=1
            
        
        grid.show_all()
        #import ipdb
        #ipdb.set_trace()
        
        
    
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
                            "onInitialCircuit":self.onInitialCircuit,
                            
                            }                
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window1")
        
        self.window_inicial = self.builder.get_object("window2")
        self.grandes_premios =  {    'Qatar':'QAT' ,
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
        self.cargar_circuitos_iniciales()
        self.window_inicial.show_all()
        
        
         
    
def main():
    window = Moto_GP()
    Gtk.main()

    return 0

if __name__ == '__main__':
    main()
