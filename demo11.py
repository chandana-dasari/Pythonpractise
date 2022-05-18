from selenium import webdriver
from time import sleep
driver=webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
links=driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
for link in links:
    print(link.text)
    sleep(1)
