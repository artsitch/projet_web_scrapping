import mysql.connector

# Connexion à la base
conn =  mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="arthur_scrapy",
    database="comparator",
)
cursor = conn.cursor(dictionary=True)  # Pour avoir des dicts

# Ta requête de comparaison
query = """
SELECT
  a.slug,
  a.name,
  a.price AS price_allinone,
  b.price AS price_static,
  a.image_url
FROM laptops a
JOIN laptops b ON a.slug = b.slug
WHERE a.site = 'all-in-one'
  AND b.site = 'static'
"""

cursor.execute(query)
results = cursor.fetchall()  # Liste de dicts

# Affiche pour tester
for row in results:
    print(row)

cursor.close()
conn.close()
