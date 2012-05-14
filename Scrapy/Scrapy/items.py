# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Post(Item):
    titulo = Field()
    contenido = Field()
    imagenes = Field()
    categorias = Field()
    tags = Field()
    
    
 