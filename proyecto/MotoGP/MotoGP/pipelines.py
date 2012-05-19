#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter
import MySQLdb

import re

class CircuitosPipeline(object):
    
    
    def process_item(self, item, spider):
        
        Conexion = MySQLdb.connect(host='localhost', user='admin',passwd='motogpadmin', db='MotogpDB') 
        micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
        
     
        
        
        query = "INSERT INTO circuitos (gran_premio,nombre,longitud,anchura,curvas_der,curvas_izq,recta_larga,fecha_construccion,fecha_modificacion) VALUES ('"
        
        query+=item['gran_premio'][0] + "','"
        query+=item['nombre'][0] + "','"
        query+=item['longitud'][0] + "','"
        query+=item['ancho'][0] + "','"
        query+=item['curvas_derecha'][0] + "','"
        query+=item['curvas_izquierda'][0] + "','"
        query+=item['recta_larga'][0] + "','"
        if item['fecha_modificacion']:
            query+=item['fecha_construccion'][0] + "','"
            query+=item['fecha_modificacion'][0] + "')"
        else:
            query+=item['fecha_construccion'][0] + "',' ')"
        

        micursor.execute(query)
        
        Conexion.commit()
        micursor.close () 
        Conexion.close()
        return item
