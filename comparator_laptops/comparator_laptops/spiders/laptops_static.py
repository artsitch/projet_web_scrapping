import scrapy
# On importe la structure de données définie dans le projet
from comparator_laptops.items import LaptopsItem

class LaptopsStaticSpider(scrapy.Spider):
    name = "laptops_static"
    allowed_domains = ["webscraper.io"]
    # L'URL spécifique pour la version "pagination classique"
    start_urls = ["https://webscraper.io/test-sites/e-commerce/static/computers/laptops"]

    def parse(self, response):
        # On parcourt chaque produit de la page (classe .thumbnail sur ce site test)
        for product in response.css(".thumbnail"):
            item = LaptopsItem()
            
            # Extraction des données (Titres, Prix, Liens...)
            item["name"] = product.css(".title::attr(title)").get()
            item["price"] = product.css(".price::text").get()
            item["product_url"] = response.urljoin(product.css(".title::attr(href)").get())
            item["image_url"] = response.urljoin(product.css(".img-responsive::attr(src)").get())
            
            yield item

        # Gestion de la Pagination (Spécifique au site "Static")
        # On cherche le lien "Page suivante" et on clique dessus virtuellement
        next_page = response.css('.pagination a[rel="next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)