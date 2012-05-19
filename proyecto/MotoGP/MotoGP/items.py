# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html
#coding=utf-8 
from scrapy.item import Item, Field

class Circuito(Item):
    # define the fields for your item here like:
    # name = Field()
    nombre = Field()
    gran_premio = Field()
    longitud = Field()
    ancho = Field()
    curvas_derecha = Field()
    curvas_izquierda = Field()
    recta_larga = Field()
    fecha_construccion = Field()
    fecha_modificacion = Field()
    
    moto3 = {   'fp1' : Field(),
                'fp2' : Field(),
                'fp3' : Field(),
                'qp' : Field(),
                'wup' : Field(),
                'clima' : Field(),
                'condicion de la pista' : Field(),
                'temperatura aire' : Field(),
                'humedad' : Field(),
                'temperatura pista' : Field(),
                'vuelta rapida' : Field(),
                'record circuito' : Field(),
                'mejor vuelta' : Field()
            }
    moto2 = {   'fp1' : Field(),
                'fp2' : Field(),
                'fp3' : Field(),
                'qp' : Field(),
                'wup' : Field(),
                'clima' : Field(),
                'condicion de la pista' : Field(),
                'temperatura aire' : Field(),
                'humedad' : Field(),
                'temperatura pista' : Field(),
                'vuelta rapida' : Field(),
                'record circuito' : Field(),
                'mejor vuelta' : Field()
            }
    motogp = {   'fp1' : Field(),
                'fp2' : Field(),
                'fp3' : Field(),
                'qp' : Field(),
                'wup' : Field(),
                'clima' : Field(),
                'condicion de la pista' : Field(),
                'temperatura aire' : Field(),
                'humedad' : Field(),
                'temperatura pista' : Field(),
                'vuelta rapida' : Field(),
                'record circuito' : Field(),
                'mejor vuelta' : Field()
            }


