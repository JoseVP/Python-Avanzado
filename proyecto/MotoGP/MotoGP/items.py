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
    

class Piloto(Item):

    nombre = Field()
    lugar_nacimiento = Field()
    fecha_nacimiento = Field()
    peso = Field()
    altura = Field()
    equipo = Field()
    moto = Field()
    dorsal = Field()
    pais = Field()

    sumario = Field()
    estadisticas = Field()
    perfil = Field()
    
    
    
