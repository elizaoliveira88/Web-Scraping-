from bs4 import BeautifulSoup
import json
import requests


url = "https://storage.googleapis.com/infosimples-output/commercia/case/product.html"
res = requests.get(url)

parsed_html = BeautifulSoup(res.content, 'html.parser')
pageRubberDuck = parsed_html.find_all(class_='content') 

all_pageRubberDuck = []
for page in pageRubberDuck:
  info = page.find(class_='container')
  title = parsed_html.select_one('h2#product_title').get_text()
  brand = parsed_html.select_one('.brand').get_text()
  categories = parsed_html.select_one('.current-category').get_text()
  description = parsed_html.select_one('.product-details').get_text()
  sku = parsed_html.select_one('.skus-area').get_text()
 
  all_pageRubberDuck.append({
    'title':title, 
    'brand':brand, 
    'categories':categories,
    'description':description,
    'sku':sku,
    })
  
  
 
with open('page.json','w') as json_file:
  json.dump(all_pageRubberDuck, json_file)

 
