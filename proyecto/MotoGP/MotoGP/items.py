# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html
#coding=utf-8 
from scrapy.item import Item, Field

 


class Circuito(Item):

    nombre = Field()
    gran_premio = Field()
    longitud = Field()
    ancho = Field()
    curvas_derecha = Field()
    curvas_izquierda = Field()
    recta_larga = Field()
    fecha_construccion = Field()
    fecha_modificacion = Field()
    
    records = Field()
    
    
