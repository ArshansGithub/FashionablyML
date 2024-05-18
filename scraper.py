from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install() 

# urls = open("websites.txt", "r").read().splitlines()

driver = webdriver.Chrome()

def getImages(link):
    toSave = ""
    driver.get(link)
    
    imgTags = driver.find_elements(By.TAG_NAME, "img")
    
    for eachImg in imgTags:
        src = eachImg.get_attribute('src')
        if (src is not None) and (src) and (not "swatch" in src):
            toSave += f"{eachImg.get_attribute('src')}\n"
        
    return toSave
    #print(imgTags)
    
levi = "https://www.levi.com/US/en_US/apparel/clothing/c/levi_clothing_category2/facets/feature-gender/women/feature-gender/men/productitemtype/jeans?page="
for i in range(6):
    open("pluh.txt", "a").write(getImages(levi + str(i)))