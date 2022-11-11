
#! Eli Orians


#! Resources
#https://selenium-python.readthedocs.io/



#! Additional Work
#8 Attributes with an equal mix of css and xpath
#Scraped 100 pages
#String and List manipulation to make data content presentable
#used selenium to click to next page
#used sleep to wait for webpage to load

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Eli Orians\\chromedriver_win32\\chromedriver.exe')
url = 'https://www.nexusmods.com/skyrim/mods/'

#Attributes
name = []            #name of mod
desc = []            #mod description
link = []            #link to the mod
author = []          #original writer of mod
uploader = []        #uploader of mod
date = []            #original upload date
update = []          #date of last update for the mod
likes = []           #number of likes


for i in range(100):

    driver.get(url)
    time.sleep(7)

    #name
    for i in driver.find_elements(By.XPATH, r'//li[@class="mod-tile"]//p[@class="tile-name"]'):
        name.append(i.text)

    #description
    for i in driver.find_elements(By.CSS_SELECTOR, r'p.desc'):
        desc.append(i.text)

    #link
    for i in driver.find_elements(By.XPATH, r'//li[@class="mod-tile"]//p[@class="tile-name"]//a'):
        link.append(i.get_attribute('href'))

    #author
    for i in driver.find_elements(By.CSS_SELECTOR, r'div.realauthor'):
        author.append(i.text)

    #uploader
    for i in driver.find_elements(By.CSS_SELECTOR, r'div.author'):
        uploader.append(i.text)

    #date
    for i in driver.find_elements(By.XPATH, r'//li[@class="mod-tile"]//time'):
        date.append(i.get_attribute('datetime'))

    #update
    for i in driver.find_elements(By.CSS_SELECTOR, r'div.date'):
        update.append(i.text)  

    #likes
    for i in driver.find_elements(By.XPATH, r'//li[@class="mod-tile"]//li[@class="endorsecount inline-flex"]//span[@class="flex-label"]'):
        likes.append(i.text)

    #loop by .click() next page button and updating url
    driver.find_element(By.XPATH, r'//li[@class="next"]/a').click()
    url = driver.current_url


driver.quit()

#format content
name = list(filter(None, name))
link = list(filter(None, link))
desc = list(filter(None, desc))
date = list(filter(None, date))
update = list(filter(None, update))
uploader = list(filter(None, uploader))


dic ={
    "Mod Title": name,
    "Mod Description": desc,
    "Link to Mod": link,
    "Original Author": author,
    "Mod Uploader": uploader,
    "Mod Endorsments": likes,
    "Original Upload Date": date,
    "Last Update": update
    }

with open('NexusSkyrimMods.json', 'a') as write_file:
    json.dump(dic, write_file, indent = 4)


