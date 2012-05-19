# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter

import re

class CircuitosPipeline(object):
    
    
    def process_item(self, item, spider):
        
        contenido_final = ''
        for texto in item['contenido']:
            
            texto = re.sub(r'<[^>]*?>',' ', texto)
            contenido_final = contenido_final + texto
        
        item['contenido'] = contenido_final
        
        imagenes = []
        for imagen in item['imagenes']:
            #import ipdb
            #ipdb.set_trace()
            imagen = re.sub(r'<img\s+.*src="','',imagen)
            imagen = re.sub(r'".*>','',imagen)
            imagenes.append(imagen)
        
        item['imagenes'] = imagenes
        
        return item
