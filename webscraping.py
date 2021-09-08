import requests
from bs4 import BeautifulSoup

res = requests.get("https://storage.googleapis.com/infosimples-output/commercia/case/product.html")
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

pageRubberDuck = soup.find_all(class_='content') 



all_pageRubberDuck = []
for page in pageRubberDuck:
  info = page.find(class_='container')
  title = info.h2.text
  brand = info.find(class_='brand')
  categories = info.find(class_='sku-name')
  description = info.find(class_='procuct-details')
  properties = info.find(class_='pure-table pure-table-bordered')
  rewins = info.find(class_='review-box')
  eviews_average_score = info.find('//*[@id="comments"]//h4')
  url = info.find(class_='about')
  all_pageRubberDuck.append({
    'title':title, 
    'brand':brand, 
    'categories':categories,
    'description':description,
    'properties':properties,
    'rewins':rewins,
    'eviews_average_score':eviews_average_score,
    'url':url,
    })
  print(all_pageRubberDuck)
  
 
