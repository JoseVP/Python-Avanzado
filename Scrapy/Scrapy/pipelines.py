# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter

import re

class PostsPipeline(object):
    
    
    def process_item(self, item, spider):
        
        contenido_final = ''
        for texto in item['contenido']:
            
            texto = re.sub(r'<[^>]*?>',' ', texto)
            contenido_final = contenido_final + texto
        
        item['contenido'] = contenido_final
        
        imagenes = []
        for imagen in item['imagenes']:
            import ipdb
            ipdb.set_trace()
            imagen = re.sub(r'<img\s+.*src="','',imagen)
            imagen = re.sub(r'".*>','',imagen)
            imagenes.append(imagen)
        
        item['imagenes'] = imagenes
        
        return item

        
class FicheroXmlPipeline(object):
    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.files = {}

    def spider_opened(self, spider):
        file = open('posts_con_tags.xml' , 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
        