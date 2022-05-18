#By using Inheritance & Decorators

from selenium import webdriver
from time import sleep
from selenium_wrapper import Selenium_Wrapper
driver=webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
sleep(5)
s=Selenium_Wrapper(driver)
s.click_element(("xpath","//a[text()='Register']"))
#sleep(2)
s.click_element(("id","gender-female"))
#sleep(2)
s.enter_text(("id","FirstName"),value="Chandana")
#sleep(2)
s.enter_text(("id","LastName"),value="dasari")
#sleep(2)
s.enter_text(("id","Email"),value="dasarichandana111@gmail.com")
#sleep(2)
s.enter_text(("id","Password"),value="chandu")
#sleep(2)
s.enter_text(("id","ConfirmPassword"),value="chandu")
#sleep(2)
s.click_element(("id","register-button"))
#sleep(2)







