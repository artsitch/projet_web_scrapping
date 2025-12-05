## **Comparateur de prix – Laptops (Scrapy + Docker + MySQL)** 

### Description

Projet académique de comparateur de prix pour des ordinateurs portables, utilisant Scrapy pour collecter les données, MySQL pour le stockage et Docker Compose pour orchestrer les différents services (scraping, base de données, serveur web).​​
Les données sont extraites depuis trois variantes d’un même site e‑commerce de test, puis affichées dans une interface web qui montre pour chaque laptop le site proposant le prix le plus bas, avec liens cliquables vers les pages d’origine.​​

### Installation​​
1. Cloner le dépôt du projet et se placer dans le dossier racine.​

2. Créer et activer un environnement virtuel Python, puis installer les dépendances :

'code inline'
--bash
#commande

pip install -r requirements.txt
ou pip install uv ; uv sync

3. Vérifier l’installation de Scrapy en lançant un spider de test :

--bash
#commande

scrapy crawl laptops -o laptops_allinone.json

4.Plus tard, pour l’architecture complète, installer Docker et Docker Compose, puis préparer les fichiers Dockerfile et docker-compose.yml qui lanceront Scrapy, MySQL et le serveur web


### Utilisation

Les spiders Scrapy ciblent la catégorie Computers → Laptops sur trois sous‑sites de test Webscraper.io :​

- All‑in‑one :
https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops​

- Static (pagination classique) :
https://webscraper.io/test-sites/e-commerce/static/computers/laptops​

- Ajax (chargement dynamique) :
https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops​

Exemple d’exécution locale d’un spider avec export JSON :

--bash
#commande

scrapy crawl laptops -o laptops_allinone.json

Chaque item contient au minimum : name, price, product_url, image_url, ce qui permettra ensuite de remplir la base MySQL et de générer l’affichage comparatif dans le serveur web.​​

### Contribution
Les contributions se font via des branches Git dédiées :​

- Créer une branche à partir de main pour chaque évolution (ex. feature/static-laptops-spider).

- Respecter la structure existante : réutiliser LaptopsItem, garder des noms de champs cohérents et mettre à jour les tests / exemples d’utilisation le cas échéant.​​

- Ouvrir une pull request décrivant clairement la modification (nouveau spider, pipeline, amélioration Docker, etc.), en veillant à ce que scrapy crawl ... fonctionne toujours sans erreur.​