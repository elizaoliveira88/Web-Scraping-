import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://storage.googleapis.com/infosimples-output/commercia/case/product.html"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)
time.sleep(10)



driver.quit()