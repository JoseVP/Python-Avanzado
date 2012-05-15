# Scrapy settings for Scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Scrapy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['Scrapy.spiders']
NEWSPIDER_MODULE = 'Scrapy.spiders'

ITEM_PIPELINES = [
                    'Scrapy.pipelines.PostsPipeline',
                    'Scrapy.pipelines.FicheroXmlPipeline',
]

FEED_FORMAT= 'xml'
FEED_EXPORTERS_BASE = {
    'json': 'scrapy.contrib.exporter.JsonItemExporter',
    'jsonlines': 'scrapy.contrib.exporter.JsonLinesItemExporter',
    'csv': 'scrapy.contrib.exporter.CsvItemExporter',
    'xml': 'scrapy.contrib.exporter.XmlItemExporter',
    'marshal': 'scrapy.contrib.exporter.MarshalItemExporter',
}
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

