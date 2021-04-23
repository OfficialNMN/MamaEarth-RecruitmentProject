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

print(ProductLinks)
driver.quit()


headers={
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}


# For every product in Products
ProductList=[]
for link in ProductLinks:

    product=requests.get(link)
    soup=BeautifulSoup(product.content,'html.parser')

    fullname=soup.find('div',class_='ProductDetails__ProdName-sc-1htzzsm-0 gdpggr').text
    name=str(fullname).split(" ")
    price=soup.find('div',class_='price').text
    try:
        review=soup.find('div',class_='ReviewItem_content').text
    except:
        review='N/A'
    rating=soup.find('div',style='margin:0rem 0.05rem').text
    try:
        discount=soup.find('div',class_='price__discount').text
    except:
        discount='N/A'

    prod={"ProductName":" ".join(name[:-2]),
           "ProductLink":link,
           "PackSize":name[-1],
           "Price":price,
           "Review":review,
           "Rating":rating,
           "Discount":discount}
    ProductList.append(prod)

df=pd.DataFrame(ProductList)
df.to_csv('MamaEarthScrape.csv')

