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
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
rp = Protego.parse(robotstxt)


if (rp.can_fetch(url, useragent)):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
else:
    print("Not allowed to scrape " + url)
    exit()



price = []
prices = soup.select('.price-current')
print(prices)

#looping
#get next link
#set url and remake soup object