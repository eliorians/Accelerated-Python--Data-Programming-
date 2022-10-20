# Eli Orians

# Resources:
#https://github.com/scrapy/protego
#https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/

#Links to 5 item pages


#Attributes Scrapped
##Brand
##GPU
##GPU Series
##Price
##Memory Size
##Rating
##Num of Ratings


#Additional Work to exced a B


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
price = []
shipPrice = []
rating = []
numRatings = []

pageCount = 0

#check next url
stuff = rp.can_fetch(url, useragent)
while (pageCount == 0):
    pageCount = pageCount + 1

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    #get prices
    for i in soup.select('.price-was-data'):
        price.append(i.text)

    #get shipPrice
    for i in soup.select('.price-ship'):
        shipPrice.append(i.text)

    #get rating
    for i in soup.select('.aria-label'):
        rating.append(i.text)

    #get ratingNumber
    #for i in soup.find_all('.item-rating-num'):
        #numRatings.append(i.text)

    #get next link

#write to file#
dic ={
    "Price": price, 
    "Shipping Price": shipPrice, 
    "Rating": rating,
    # "Number of Ratings": numRatings
    }

with open('Newegg Webscrape.json', 'a') as write_file:
    json.dump(dic, write_file, indent = 4)
