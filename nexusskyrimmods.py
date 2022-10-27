
#Eli Orians

#Resources:
#https://docs.scrapy.org/en/latest/index.html
#https://coderslegacy.com/python/scrapy-xpath-tutorial/

#Additional Work
#


import scrapy
import json

# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.



class SkyrimModSpider(scrapy.Spider):
    name = "skyrim-mods"

    def start_requests(self):
        urls = ['https://www.nexusmods.com/skyrim/mods/']

        pageCount = 0
        for i in range(100):
            nextUrl = "https://www.nexusmods.com/skyrim/mods/?BH=" + str(pageCount)
            urls.append(nextUrl)
            pageCount = pageCount + 1 
        

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        #Attributes
        modName = []            #name of mod
        modLink = []            #link to the mod
        modAuthor = []          #original writer of mod
        modUploader = []        #uploader of mod
        modUploaderProfile = [] #link to uploader profiler
        modDesc = []            #mod description
        modSize = []            #download size of mod
        modLikes = []           #number of likes
        modDate = []            #original upload date 
        modUpdate = []          #date of last update
        

        #1
        modName = response.xpath('//li[@class="mod-tile"]//p[@class="tile-name"]//text()').getall()
        modName = modName[::2]

        #2
        modAuthor = response.xpath('//li[@class="mod-tile"]//div[@class="realauthor"]/text()').getall()
        
        #3
        modUploader = response.xpath('//li[@class="mod-tile"]//div[@class="author"]//a//text()').getall()
        modUploader = modUploader[::2]

        #4
        modDesc = response.xpath('//li[@class="mod-tile"]//p[@class="desc"]/text()').getall()
        modDesc = modDesc[::2]

        #5
        modSize = response.xpath('//li[@class="mod-tile"]//li[@class="sizecount inline-flex"]//span[@class="flex-label"]/text()').getall()

        #6
        modLikes = response.xpath('//li[@class="mod-tile"]//li[@class="endorsecount inline-flex"]//span[@class="flex-label"]/text()').getall()

        #7
        modLink = response.xpath('//li[@class="mod-tile"]//p[@class="tile-name"]//a//@href').getall()
        modLink = modLink[::2]

        #8
        modDate = response.xpath('//li[@class="mod-tile"]//time//@datetime').getall()
        modDate = modDate[::2]

        #9
        modUpdate = response.xpath('//li[@class="mod-tile"]//div[@class="date"]//text()').getall()
        modUpdate = modUpdate[::-2]
        modUpdate = modUpdate[::2]

        #10
        modUploaderProfile = response.xpath('//li[@class="mod-tile"]//div[@class="author"]//a//@href').getall()
        modUploaderProfile = modUploaderProfile[::2]
        

        dic ={
            "Mod Title": modName,
            "Mod Description": modDesc,
            "Link to Mod": modLink,
            "Original Author": modAuthor,
            "Mod Uploader": modUploader,
            "Uploader's Profile": modUploaderProfile,
            "Mod Download Size" : modSize,
            "Mod Endorsments": modLikes,
            "Original Upload Date": modDate,
            "Last Update": modUpdate
            }

        with open('NexusSkyrimMods.json', 'a') as write_file:
            json.dump(dic, write_file, indent = 4)
