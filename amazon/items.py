# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class BookItem(Item):
    title = Field()
    lang = Field() 
    authors= Field()
    year_pub = Field()
    pages = Field()
    pub_house = Field()
    details = Field()
    price = Field()
    images = Field()

    andress_url = Field()
    data_scraping = Field()
