# Eli Orians

# Resources:
#https://www.newegg.com/robots.txt

#Links to 5 item pages


#Attributes Scrapped
##Brand
##GPU
##GPU Series
##Price
##Chipset MAnu.
##Memory Size
##Rating
##Num of Ratings
##Card Dimensions
##Reccomended Wattage
##Release Date


#Additional Work to exced a B


from bs4 import BeautifulSoup
from protego import Protego
import requests
import json

url = "https://www.newegg.com/p/pl?N=100007709"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

print(soup.title)


#-----#


#scrape at least 5 item pages with at least 5 attributes
#use find/find_all for at least 1 element
#use select/select_all for at least 1 element
#each item should produce one dictionary wiht attribute:value pairs
#use a regular expression

d = {}
with open('data.jl', 'a') as fp:
    s = json.dumps(d)
    fp.writes(s + '\n')



