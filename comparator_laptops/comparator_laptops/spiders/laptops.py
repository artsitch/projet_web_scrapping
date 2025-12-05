import scrapy


class LaptopsSpider(scrapy.Spider):
    name = "laptops"
    allowed_domains = ["webscraper.io"]
    start_urls = [
        "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    ]

    def parse(self, response):
        pass
