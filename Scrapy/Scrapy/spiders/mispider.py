from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from Scrapy.items import Item,Post 


class MiSpider(CrawlSpider):
    name = 'mispider'
    allowed_domains = ['osl.ugr.es']
    start_urls = ['http://osl.ugr.es']
    
    
    rules = (
            
            Rule(SgmlLinkExtractor(allow=('/\d{4}/\d{2}/\d{2}/.' )), callback='parse_post'),
            )

    
    
    def parse_post(self, response):
        
        hxs = HtmlXPathSelector(response)
        
        elemento = Post()
        
        #import ipdb
        #ipdb.set_trace()
        
        elemento['titulo'] = hxs.select('//h1[@class="entry-title"]/text()').extract()
        
        elemento['contenido'] = hxs.select('//div[@class="entry-content"]/p/text()/a/text()').extract()
        
        elemento['categorias'] = hxs.select('//span[@class="entry-categories"]/a/text()').extract()
        
        elemento['tags'] = hxs.select('//span[@class="entry-tags"]/a/text()').extract()
        
        return elemento