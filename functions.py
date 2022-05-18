#By using functions
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
sleep(5)
def enter_text(loctype,locvalue,value):
    driver.find_element(loctype,locvalue).clear()
    driver.find_element(loctype,locvalue).send_keys(value)
def click_element(loctype,locvalue):
    driver.find_element(loctype,locvalue).click()
def select_item(loctype,locvalue,item):
    lst_box=driver.find_element(loctype,locvalue)
    s=Select(lst_box)
    s.select_by_visible_text(item)
click_element("xpath","//a[text()='Register']")
sleep(2)
click_element("id","gender-male")
sleep(2)
enter_text("id","FirstName","Chandana")
sleep(2)
enter_text("id","LastName","dasari")
sleep(2)
enter_text("id","Email","dasarichandana111@gmail.com")
sleep(2)
enter_text("id","Password","chandu")
sleep(2)
enter_text("id","ConfirmPassword","chandu")
sleep(2)
click_element("id","register-button")
sleep(2)





