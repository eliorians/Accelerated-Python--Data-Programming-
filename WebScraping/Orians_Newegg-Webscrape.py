# Eli Orians

# Resources:
#https://github.com/scrapy/protego
#https://www.skytowner.com/explore/beautiful_soup_find_all_method
#https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/
#https://stackoverflow.com/questions/10993612/how-to-remove-xa0-from-string-in-python/34669482#34669482
#https://note.nkmk.me/en/python-str-replace-translate-re-sub/

#ADDITIONAL WORK
# Used reg expression
# Scraped more than 5 attributes
# used string manipulation
# used a mix of find_all and select
# had to find info becasue textbook was bad

import unicodedata
from bs4 import BeautifulSoup
from protego import Protego
import requests
import re
import json

url = "https://www.newegg.com/p/pl?N=100007709"
robotstxt = "https://www.newegg.com/robots.txt"
rp = Protego.parse(robotstxt)
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

#Attributes Scraped
name = []
brand = []
price = []
shipPrice = []
rating = []
numRatings = []

pageCount = 0

#check next url
#page count is limit of pages to scrape
while (rp.can_fetch(url, useragent) and pageCount < 1):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    #get name
    #get brand
    for i in soup.select('.item-title'):
        i = i.text
        x = i.split(' ')
        name.append(i)
        brand.append(x[0])


    #get prices
    for i in soup.find_all('li', class_='price-current'):
        i = i.text
        i = unicodedata.normalize("NFKD", i)
        x = i.split(' ')
        price.append(x[0])

    #get shipPrice
    for i in soup.select('.price-ship'):
        shipPrice.append(i.text)

    #get rating
    for i in soup.find_all('i', class_='rating rating-4-5'):
        rating.append(i.get('aria-label'))

    #get ratingNumber
    for i in soup.select('.item-rating'):
        i = i.text
        i = re.sub('[()]', '', i)
        i = i + " ratings received"
        numRatings.append(i)

    pageCount = pageCount + 1

    #get next link
    #url = soup.select_one('')


#write to file
dic ={
    "Name": name,
    "Brand": brand,
    "Price": price, 
    "Shipping Price": shipPrice, 
    "Rating": rating,
    "Number of Ratings": numRatings,
    }


with open('Newegg Webscrape.json', 'a') as write_file:
    json.dump(dic, write_file, indent = 4)
print("JSON created with {} pages scrapped".format(pageCount))