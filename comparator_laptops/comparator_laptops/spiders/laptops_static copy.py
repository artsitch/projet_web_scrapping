import scrapy
from ..items import LaptopsItem


class LaptopsSpider(scrapy.Spider):
    name = "laptops_ajax"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops"]

    def parse(self, response):
        products = response.xpath('//div[contains(@class,"thumbnail")]')
        self.logger.info(f"Nombre de produits trouvé : {len(products)}")

        for prod in products:
            title = prod.xpath('.//a[contains(@class, "title")]/text()').get()
            price = prod.xpath('.//span[@itemprop="price"]/text()').get()
            product_url = prod.xpath('.//a[contains(@class, "title")]/@href').get()
            image_url = prod.xpath('.//img/@src').get()

            if title:
                title = title.strip()
            if price:
                price = price.strip()

            laptop = LaptopsItem()
            laptop["name"] = title
            laptop["price"] = price
            laptop["product_url"] = response.urljoin(product_url)
            laptop["image_url"] = response.urljoin(image_url)

            yield laptop

        # Pagination : initialiser next_page AVANT la boucle
        next_page = response.xpath('//a[normalize-space(text())="›"]/@href').get()

        if next_page is not None:
            self.logger.info(f"Next page URL: {next_page}")
            yield response.follow(next_page, callback=self.parse)