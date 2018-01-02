# -*- coding: utf-8 -*-
import scrapy


class AmazonBooksSpider(scrapy.Spider):
    name = 'amazon_books'
    allowed_domains = ['amazon.com.br']
    start_urls = ['https://www.amazon.com.br/Livros/b/ref=nav__books_all?ie=UTF8&node=6740748011']

    def parse(self, response):
        pass
