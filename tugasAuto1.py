from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

def getUrls(targeturl):
    driver.minimize_window()
    driver.get("http://www."+targeturl+".com")
    sleep(3)
    title = driver.title
    print (title)

webPage = ['tokopedia','tiket','orangsiber','automatetheboringstuff']
for i in webPage:
    getUrls(i)
driver.quit()