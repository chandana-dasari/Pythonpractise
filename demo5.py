from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("./chromedriver")
driver.get("https://www.myntra.com/")
sleep(5)
actions=ActionChains(driver)
kids=driver.find_element_by_xpath("(//a[text()='Kids'])[1]")
actions.move_to_element(kids).perform()
sleep(2)
t_shirts=driver.find_element_by_xpath("(//a[text()='T-Shirts'])[1]").click()
actions.move_to_element(t_shirts).perform()
sleep(2)