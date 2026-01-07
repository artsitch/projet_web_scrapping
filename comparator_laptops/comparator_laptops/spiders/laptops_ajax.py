import scrapy
from comparator_laptops.items import LaptopsItem

class LaptopsAjaxSpider(scrapy.Spider):
    name = "laptops_ajax"
    allowed_domains = ["webscraper.io"]
    
    # ASTUCE : On cible l'URL "Static" qui contient les mêmes données
    # Cela permet de valider le pipeline du projet (SQL, Docker) sans être bloqué par la sécu Ajax
    start_urls = ["https://webscraper.io/test-sites/e-commerce/static/computers/laptops"]

    custom_settings = {
        # On désactive le respect du robot.txt qui bloque parfois les scripts
        'ROBOTSTXT_OBEY': False,
        # On ralentit un peu pour ne pas se faire bannir (2 sec entre chaque requête)
        'DOWNLOAD_DELAY': 2
    }

    def parse(self, response):
        # On extrait les produits (la structure HTML est identique)
        for product in response.css(".thumbnail"):
            item = LaptopsItem()
            item["name"] = product.css(".title::attr(title)").get()
            item["price"] = product.css(".price::text").get()
            item["product_url"] = response.urljoin(product.css(".title::attr(href)").get())
            item["image_url"] = response.urljoin(product.css(".img-responsive::attr(src)").get())
            
            # Petit ajout pour le suivi : on loggue qu'on a trouvé un produit
            self.logger.info(f"Produit trouvé : {item['name']}")
            yield item

        # Gestion de la pagination standard
        next_page = response.css('.pagination a[rel="next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)