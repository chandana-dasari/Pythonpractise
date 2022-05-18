#By using package
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
sleep(5)
def enter_text(locator,*,value):
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)
def click_element(locator):
    driver.find_element(*locator).click()
def select_item(locator,*,item):
    lst_box=driver.find_element(*locator)
    s=Select(lst_box)
    s.select_by_visible_text(item)
click_element(("xpath","//a[text()='Register']"))
sleep(2)
click_element(("id","gender-male"))
sleep(2)
enter_text(("id","FirstName"),value="Chandana")
sleep(2)
enter_text(("id","LastName"),value="dasari")
sleep(2)
enter_text(("id","Email"),value="dasarichandana111@gmail.com")
sleep(2)
enter_text(("id","Password"),value="chandu")
sleep(2)
enter_text(("id","ConfirmPassword"),value="chandu")
sleep(2)
click_element(("id","register-button"))
sleep(2)





