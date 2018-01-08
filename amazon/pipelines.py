# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from amazon.items import BookItem
from re import findall

class AmazonPipeline(object):
    def process_item(self, item, spider):
        return item

class BooksPipeline(object):
    months = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dez': '12'
    }

    def process_item(self, item, spider):
        if('year_pub' in item):
            item['year_pub'] = self.__model_year_pub__(item['year_pub'])
        return item

    def __model_year_pub__(self, year_pub):
        day = findall(r"(\d+) [a-z]{3} \d+", year_pub)
        year = findall("\d+ [a-z]{3} (\d+)", year_pub)
        for month in self.months.keys():
            if(month in year_pub):
                month = self.months[month]
                break
        if(day and year and month):
            return "{}/{}/{}".format(day.pop(), month, year.pop())
        return year_pub