
#Eli Orians

#Resources:
#https://docs.scrapy.org/en/latest/index.html
#https://coderslegacy.com/python/scrapy-xpath-tutorial/

#Additional Work
#had to restart :(
#use of a mix of xpath and css together to get certain attributes
#use of string manipulation to combine attributes into useful information
#use of regular expression to make information more readable
#use of global variables to keep all attributes together, rather than page by page

import scrapy
import json
import re

# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
name = []           #name of CPU
price = []          #price of CPU
shipPrice = []      #shipping price
rating = []         #rating out of 5
ratingNumber = []   #number of ratings recieved
link = []           #link to the CPU
feature = []        #first listed feature of cpu
brand = []          #CPU brand
promo = []          #promotion, if there is one
savings = []        #savings, if there is any

dic ={
        "Title": name,
        "Brand": brand,
        "Price": price,
        "Shipping Price": shipPrice,
        "Rating out of 5": rating,
        "Number of Ratings": ratingNumber,
        "Link to Product": link,
        "First Listed Feature" : feature,
        "Promotion": promo,
        "Savings Percent": savings
        } 

class NewEggCPUSpider(scrapy.Spider):
    name = "newegg"

    def start_requests(self):
        urls = ['https://www.newegg.com/Desktop-Memory/SubCategory/ID-147']

        pageCount = 2
        for i in range(100):
            nextUrl = "https://www.newegg.com/Desktop-Memory/SubCategory/ID-147/Page-" + str(pageCount)
            urls.append(nextUrl)
            pageCount = pageCount + 1 
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        with open('Newegg_Scrapy.json', 'a') as write_file:
            json.dump(dic, write_file, indent = 4)  


    def parse(self, response):
        
        global dic

        #Attributes
        name = []           #name of CPU
        price = []          #price of CPU
        shipPrice = []      #shipping price
        rating = []         #rating out of 5
        ratingNumber = []   #number of ratings recieved
        link = []           #link to the CPU
        feature = []        #first listed feature of cpu
        brand = []          #CPU brand
        promo = []          #promotion, if there is one
        savings = []        #savings, if there is any
        
        #1
        name = response.xpath('//a[@class="item-title"]//text()').getall()

        #2
        #!combine two lists together to piece the <strong> whole number and <sup> decimal
        #!Mix of xpath and css
        priceWhole = response.xpath('//li[@class="price-current"]').css('strong::text').getall()
        priceDeci = response.xpath('//li[@class="price-current"]').css('sup::text').getall()
        for i in range(len(priceWhole)):
            price.append("$" + priceWhole[i] + priceDeci[i])
        
        #3
        shipPrice = response.xpath('//li[@class="price-ship"]//text()').getall()

        #4
        rating = response.xpath('//i[@class="rating rating-5"]/@aria-label').getall()

        #5
        #!Regular Expression here to format text
        ratingNumber = response.xpath('//span[@class="item-rating-num"]//text()').getall()
        formatted = []
        for i in ratingNumber:
            formatted.append(re.sub('[()]', '', i))
        ratingNumber = formatted

        #6
        link = response.xpath('//a[@class="item-title"]/@href').getall()

        #7
        #!Couldn't pick particular feature as it was never consistent, but every item had at least one feature listed
        #!Mix of xpath and css
        key = response.xpath('//ul[@class="item-features"]//li[1]').css('strong::text').getall()
        value = response.xpath('//ul[@class="item-features"]//li[1]/text()').getall()
        for i in range(len(key)):
            feature.append(key[i] + value[i])

        #8
        #!pulling the brand off of the image
        brand = response.xpath('//a[@class="item-brand"]//img/@title').getall()
    
        #9
        promo = response.xpath('//p[@class="item-promo"]//text()').getall()

        #10
        savings = response.xpath('//span[@class="price-save-percent"]//text()').getall()

        #!Add to dictionary
        dic["Title"] += name
        dic["Brand"] += brand
        dic["Price"] += price
        dic["Shipping Price"] += shipPrice
        dic["Rating out of 5"] += rating
        dic["Number of Ratings"] += ratingNumber
        dic["Link to Product"] += link
        dic["First Listed Feature"] += feature
        dic["Promotion"] += promo
        dic["Savings Percent"] += savings