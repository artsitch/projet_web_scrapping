import mysql.connector
import json

con = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="arthur_scrapy",
    database="comparator",
)

print("Connexion OK")

