import mysql.connector
import json
from merge_laptops import df_allinone, df_static

con = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="arthur_scrapy",
    database="comparator",
)

print("Connexion OK")
insert_query = """
INSERT INTO laptops (name, price, product_url, image_url, site)
VALUES (%s, %s, %s, %s, %s)
"""

cursor = con.cursor()

for df in (df_allinone, df_static):
    for _, row in df.iterrows():
        cursor.execute(
            insert_query,
            (
                row["name"],
                row["price"],
                row["product_url"],
                row["image_url"],
                row["website"],
            ),
        )

con.commit()
cursor.close()
con.close()
print("table remplie")
