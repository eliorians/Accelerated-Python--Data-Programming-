
#Eli Orians

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\Eli Orians\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.nexusmods.com/skyrim/mods/')


#Attributes
modName = []            #name of mod
#modLink = []            #link to the mod
#modAuthor = []          #original writer of mod
#modUploader = []        #uploader of mod
#modUploaderProfile = [] #link to uploader profiler
#modDesc = []            #mod description
#modSize = []            #download size of mod
#modLikes = []           #number of likes
#modDate = []            #original upload date 
#modUpdate = []          #date of last update


for i in driver.find_elements(By.XPATH, r'//li[@class="mod-tile"]//p[@class="tile-name"]'):
    modName.append(i.text)
modName = modName[::2]

driver.quit()