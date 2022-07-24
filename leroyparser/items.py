# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def process_price(value):
    print()
    value = value.replace(' ', '')
    try:
        value = float(value)
    except:
        pass
    return value


class LeroyparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    print()
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(process_price),output_processor=TakeFirst())
    photos = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())



