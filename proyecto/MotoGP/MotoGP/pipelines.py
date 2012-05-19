# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter
import MySQLdb

import re

class CircuitosPipeline(object):
    
    
    def process_item(self, item, spider):
        
        grandes_premios =  {    'QAT':'Qatar' ,
                                'SPA':'España',
                                'POR':'Portugal',
                                'FRA':'Francia',
                                'CAT':'Cataluña',
                                'GBR':'Gran Bretaña',
                                'NED':'Holanda',
                                'GER':'Alemania',
                                'ITA':'Italia',
                                'USA':'Estados Unidos' ,
                                'INP':'Indianapolis',
                                'CZE':'Republica Checa',
                                'RSM':'San Marino' ,
                                'ARA':'Aragon',
                                'JPN':'Japon' ,
                                'MAL':'Malasia',
                                'AUS':'Australia',
                                'VAL':'Valencia',
                        }
        
        
        
        Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        
        query = "INSERT INTO circuitos (gran_premio,nombre,longitud,anchura,curvas_der,curvas_izq,recta_larga,fecha_construccion,fecha_modificacion) VALUES ('"
        
        query+=grandes_premios[item.['gran_premio']] + "','"
        query+=item.['nombre'] + "','"
        query+=item.['longitud'] + "','"
        query+=item.['anchura'] + "','"
        query+=item.['curvas_derecha'] + "','"
        query+=item.['curvas_izquierda'] + "','"
        query+=item.['recta_larga'] + "','"
        query+=item.['fecha_construccion'] + "','"
        query+=item.['fecha_modificacion'] + "')"
        
        micursor.execute(query)
        
        Conexion.commit()
        micursor.close () 
        Conexion.close()
        return item
