
#Eli Orians

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.nexusmods.com/skyrim/mods/')
assert "NexusSkyrimMods" in driver.title


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