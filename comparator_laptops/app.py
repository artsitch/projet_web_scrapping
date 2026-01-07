from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Connexion à la base
    conn =  mysql.connector.connect(
    host=os.environ.get("DB_HOST", "db"),
    port=3306,
    user="root",
    password="arthur_scrapy",
    database="comparator",
)

    
    cursor = conn.cursor(dictionary=True)
    
    # Ta requête de comparaison
    query = """
            SELECT
            a.slug,
            a.name,
            a.price AS price_allinone,
            b.price AS price_static,
            a.image_url,
            a.product_url AS url_allinone,
            b.product_url AS url_static
            FROM laptops a
            JOIN laptops b ON a.slug = b.slug
            WHERE a.site = 'all-in-one'
            AND b.site = 'static'
"""
    
    cursor.execute(query)
    laptops = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('index.html', laptops=laptops)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
