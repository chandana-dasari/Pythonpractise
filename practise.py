from selenium import webdriver
from time import sleep
driver=webdriver.Chrome("./chromedriver")
'''driver.get("https://www.monster.com/")
#sleep(3)
driver.find_element_by_partial_link_text("Work from Home").click()
sleep(4)
driver.find_element_by_css_selector("(span[text()='Jobseeker Login'])[2]").click()

driver.get("https://www.python.org")
driver.find_element_by_xpath("//input[@class='search-field']").send_keys("python")
driver.find_element_by_xpath("//button[@id='submit']").click()
'''
driver.get("https://smartbear.com/")