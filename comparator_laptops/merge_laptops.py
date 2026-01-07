# import of the library which permit to process json file
import json
import pandas as pd

#load the laptop data from both site all-in-one and static
with open("laptops_allinone.json", encoding="utf-8") as f:
    data_allinone = json.load(f)

with open("laptops_static.json", encoding="utf-8") as f1:
    data_static = json.load(f1)

#print the number of raw of our dataset
print(f"le nombre d'ordi provenant d ' allinone {len(data_allinone)}")
print(f"le nombre d'ordi provenant de static {len(data_static)}")

#load rhe data in datasets
df_allinone = pd.DataFrame(data_allinone)
df_static = pd.DataFrame(data=data_static)

print(f"the laptop data from webscrapper.io/all-in-one are  {df_allinone.head()} \n")
print(f"the laptop data from webscrapper.io/static are {df_static.head()} \n")

#transform the price column

df_static["price"] = df_static["price"].str.replace("$","").astype("float")
df_allinone["price"] = df_allinone["price"].str.replace("$","").astype("float")

print(df_allinone["price"].head())
print(df_static["price"].head())

df_allinone["website"] = "all-in-one"
df_static["website"] = "static"

print(df_static.head())
print(df_allinone.head())