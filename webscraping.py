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
  
 
 
























# import time
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# import json

# url = "https://storage.googleapis.com/infosimples-output/commercia/case/product.html"
# url.encoding = 'utf-8'

# option = Options()
# option.headless = True
# driver = webdriver.Firefox()

# driver.get(url)
# time.sleep(10)

# driver.find_element_by_xpath('//div//*[@id="product_S0002201"]//div[3]').click()


# element = driver.find_element_by_xpath('//div//*[@id="product_S0002201"]//div[3]')
# html_content = element.get_attribute('outerHTML')

# print(html_content)

# driver.quit()