#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from gi.repository import Gtk
import subprocess  
    
    

class Moto_GP:

    #-------------------FUNCIONES INTERNAS---------------------#
    
    
    #Carga los circuitos iniciales en los botones de la Ventana de inicio
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
            #Cargamos los nombres de las carreras en los botones de inicio
            for carrera in self.carreras:
                boton = self.builder.get_object('button%s'%i)
                boton.set_label(carrera)
                i+=1
            
    #Carga los detalles del circuito deseado
    def cargar_informacion_circuito(self,circuito):
        Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        
        query = "SELECT * FROM circuitos WHERE gran_premio = '%s'" % self.grandes_premios[circuito]
        
        micursor.execute(query)

        datos = micursor.fetchone()
        
        #Rellenamos las etiquetas con la informacion obtenida
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
        
        #Cerramos la conexion con la base de datos
        micursor.close () 
        Conexion.close()
        
        
    #Carga los records del circuito deseado
    def cargar_records_circuito(self,circuito):
        Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        
        #Obtenemos el id asociado al circuito para obtener los records exactos del circuito
        query = "SELECT id FROM circuitos WHERE gran_premio = '%s'" % self.grandes_premios[circuito]
        micursor.execute(query)
        id_circuito= micursor.fetchone()
        
        query = "SELECT * FROM records_circuitos WHERE id_circuito = '%s' ORDER BY categoria DESC" % id_circuito['id']
        micursor.execute(query)
        records = micursor.fetchall()
        grid = self.builder.get_object("grid_records")
        
        #Guardamos la categoria inicial para compararla y ver cuando cambia la categoria en los datos
        cat_act = records[0]['categoria']
        i = 2
        for record in records:
            if (record['categoria'] != cat_act):
                #si la categoria ha cambiado comprobamos que categoria es
                #para asignar la fila en la que debemos empezar a rellenar los datos
                if(record['categoria'] == 'MotoGP'):
                    i=2
                elif (record['categoria'] == 'Moto2'):
                    i=7
                elif (record['categoria'] == '125cc'):
                    i=12
                cat_act = record['categoria']
                
                
            label = self.builder.get_object("label_%s_%s" %(i,1))
            #si temporada = 0 significa que no hay resultado 
            #asi que en vez de mostrar un 0 en ese campo lo mostramos vacio
           
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
    
    #Devuelve una tupla con la imagen del circuito y de la bandera correspondiente
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
    
    #Lanza desde el sistema operativo el scrapper para obtener la informacion desde www.motogp.com/es
    def ejecutar_scrapper(self):
        Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        #Para evitar la acumulación innecesaria de datos eliminamos primero las tablas
        #Solo necesitamos eliminar la tabla circuitos ya que por cascada
        #se vacia automaticamente la de records
        query = "DELETE FROM circuitos WHERE 1"
        micursor.execute(query)
        Conexion.commit()
        micursor.close() 
        Conexion.close()
        #se lanza el scrapper sin log para no mostrar nada por el terminal
        subproceso = subprocess.Popen(['scrapy','crawl', 'circuitos','--nolog'])
        subprocess.Popen.wait(subproceso)  
        
        
    #Comprueba que las tablas existan y si no es asi,las crea
    #De existir las tabas se comprueba que haya exactamente 18 circuitos
    def comprobar_tablas(self):
        Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        
        query = "show tables"
        micursor.execute(query)
        tablas = micursor.fetchall()
        tabla_circuitos = False
        tabla_records = False
        tabla_correcta = True
        if tablas:
            for tabla in tablas:

                if 'circuitos' == tabla['Tables_in_MotogpDB']:
                    tabla_circuitos = True
                if 'records_circuitos' == tabla['Tables_in_MotogpDB']:
                    tabla_records = True
        
        if not tabla_circuitos:
            query =" CREATE TABLE circuitos (id int(10) auto_increment primary key,gran_premio varchar(100) not null,nombre varchar(100) not null,longitud varchar(100),anchura varchar(100),curvas_der int(2),curvas_izq int(2),recta_larga varchar(100),fecha_construccion varchar(100),fecha_modificacion varchar(100))ENGINE=INNODB"
           
            micursor.execute(query)
            Conexion.commit()
        else:
            query = " Select id from circuitos "
            num = micursor.execute(query)
            if num != 18 :
                tabla_correcta=False
        if not tabla_records:
            query =" CREATE TABLE records_circuitos (id int(10) auto_increment primary key,id_circuito int(10) not null,categoria varchar(100) not null,record varchar(100) not null,temporada int(4) not null,piloto varchar(100) not null,motocicleta varchar(100),tiempo varchar(100),velocidad varchar(100),foreign key (id_circuito) references circuitos(id) on delete cascade)ENGINE=INNODB;"
            
            micursor.execute(query)
            Conexion.commit()
            
        
        
        
        
        if not tabla_circuitos or not tabla_records or not tabla_correcta:
            return False
        else:
            return True
    
    
    
    
    
    def onInitialCircuit(self,boton):
        self.onVerCircuito(boton)
        self.window_inicial.hide()
        self.window.show_all()
   
   
    def onVerCircuito(self,menuitem):
        #cargamos las imagenes del circuito y la bandera del pais
        imagen = self.builder.get_object('imagen_circuito')
        circuito = menuitem.get_label()
        imagenes = self.cargar_imagenes(circuito)
        imagen.set_from_file(imagenes[0])
        
        #cargamos la informacion y los records
        self.cargar_informacion_circuito(circuito)
        self.cargar_records_circuito(circuito)
        
        #ponemos como icono de la ventana la bandera del pais
        self.window.set_icon_from_file(imagenes[1])
        bandera = self.builder.get_object('imagen_bandera')
        bandera.set_from_file(imagenes[1])
        
        self.window.set_title("Circuito de %s" % circuito)
        
    def onShowAbout(self,menuitem):
        about = self.builder.get_object("about_dialog")
        about.run()
        about.destroy()
    

    def onActualizarCircuitos(self,item):
        #si el label del item es Aceptar significa que viene
        # del dialogo de error de comprobacion de tablas
        #por lo que no mostramos el dialogo para actualizacion
        
        if(item.get_label() != "Aceptar"):
            dialogo = self.builder.get_object("dialogo_actualizar")        
            respuesta = dialogo.run()
        else:
            respuesta = 1
            self.cargar_circuitos_iniciales()
            self.window_inicial.show_all()
            self.dialogo.hide()
            
            
        if respuesta == 1 :
            
            self.ejecutar_scrapper()
            #Una vez actualizados los datos se lo indicamos al usuario
            #suprimimos los botones para obligar a cerrar la ventana
            #y evitar que manipule la ventana principal
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
                            "onShowAbout":self.onShowAbout
                            
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
                                'Valencia':'VAL'}
        #Antes de mostrar ninguna ventana se comprueba la base de datos
        if (self.comprobar_tablas()):
            self.cargar_circuitos_iniciales()
            self.window_inicial.show_all()
        else:
            self.dialogo = self.builder.get_object('dialogo_error_tablas')
            self.dialogo.show_all()
            
            
            
            
         
    
def main():
    window = Moto_GP()
    Gtk.main()

    return 0

if __name__ == '__main__':
    main()
