import scrapy
from ..items import LaptopsItem


class LaptopsSpider(scrapy.Spider):
    name = "laptops"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"]

    def parse(self, response):
        products = response.xpath('//div[contains(@class,"thumbnail")]')
        print(f"Nombre de produits trouvé : {len(products)}")
        #self.logger.info(f"Nombre de produits trouvé : {len(products)}"), equivalent du print mieux gere par scrapy


        for prod in products :
            title = prod.xpath('.//a[contains(@class, "title")]/text()').get()
            price = prod.xpath('.//h4[contains(@class, "price")]/text()').get()
            product_url = prod.xpath('.//a[contains(@class, "title")]/@href').get()
            image_url = prod.xpath('.//img[contains(@class, "image")]/@src').get()
            # recuperation des infos sur les produits
            laptop = LaptopsItem()

            if title:
                title = title.strip()
            if price:
                price = price.strip()
            
            laptop["name"] = title
            laptop["price"] = price
            laptop["product_url"] = response.urljoin(product_url)
            laptop["image_url"] = response.urljoin(image_url)

            yield laptop

