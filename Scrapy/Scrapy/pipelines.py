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
            #import ipdb
            #ipdb.set_trace()
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
        file_tags = open('posts_con_tags.xml' , 'w+b')
        file_notags = open('posts_sin_tags.xml', 'w+b')
        self.files['tags'] = file_tags
        self.files['notags'] = file_notags
        self.exporter_tags = XmlItemExporter(file_tags)
        self.exporter_notags = XmlItemExporter(file_notags)

    def spider_opened(self, spider):        
        self.exporter_tags.start_exporting()
        self.exporter_notags.start_exporting()

    def spider_closed(self, spider):
        self.exporter_tags.finish_exporting()
        self.exporter_notags.finish_exporting()
        
        file = self.files.pop('tags')
        file.close()
        file = self.files.pop('notags')
        file.close()

    def process_item(self, item, spider):
        
        if item['tags']:
            self.exporter_tags.export_item(item)
        else:
            self.exporter_notags.export_item(item)
        return item
        