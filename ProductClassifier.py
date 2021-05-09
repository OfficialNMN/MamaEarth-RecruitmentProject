from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver

# Using selenium to get every product Links
driver = webdriver.Chrome (executable_path=r"C:\Users\NAMANJEET SINGH\Documents\chromedriver_win32\chromedriver.exe")
driver.get('https://mamaearth.in/product-category/beauty')

AllProducts=driver.find_elements_by_class_name('uniquewhite')

ProductLinks=[]
for product in AllProducts:
    link=product.find_element_by_tag_name('a')
    ProductLinks.append(link.get_property('href'))

# For every product in Products
ProductList=[]
for link in ProductLinks:

    driver.get(link)
    product_name=driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div[2]/div[2]/div/h1/div').text
    name=str(product_name).split(" ")
    try:    
    	Ingredient=driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div[3]/div[2]/div/ul/li[1]/span/strong').text
    except:
    	Ingredient=N/A
    prod={'ProductName':" ".join(name[:-2]), 
     	'Ingredients':Ingredient}
    ProductList.append(prod)

df=pd.DataFrame(ProductList)
df.to_csv('MamaEarthProductClassifier.csv')

driver.quit()

