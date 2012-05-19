from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from MotoGP.items import Item,Circuito


class Circuitos(CrawlSpider):
    name = 'circuitos'
    allowed_domains = ['www.motogp.com']
    start_urls = ['http://www.motogp.com/es']
    
    
    rules = (
            
            Rule(SgmlLinkExtractor(allow=('/events/.+/2012' )), callback='parse_circuito'),
            )

    

    def parse_circuito(self, response):
        
        hxs = HtmlXPathSelector(response)
        
        elemento = Circuito()
        
        #import ipdb
        #ipdb.set_trace()
        
        elemento['nombre'] = hxs.select('//div[@id="info_track"]/h2/text()').extract()
        elemento['longitud'] = hxs.select('//div[@class="circuit_info"]/p[2]/text()').extract()
        elemento['ancho'] = hxs.select('//div[@class="circuit_info"]/p[3]/text()').extract()
        elemento['curvas_izquierda'] = hxs.select('//div[@class="circuit_info"]/p[4]/text()').extract()
        elemento['curvas_derecha'] = hxs.select('//div[@class="circuit_info"]/p[5]/text()').extract()
        elemento['recta_larga'] = hxs.select('//div[@class="circuit_info"]/p[6]/text()').extract()
        elemento['fecha_construccion'] = hxs.select('//div[@class="circuit_info"]/p[7]/text()').extract()
        elemento['fecha_modificacion'] = hxs.select('//div[@class="circuit_info"]/p[8]/text()').extract()
        return elemento