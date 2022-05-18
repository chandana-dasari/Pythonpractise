from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.action_chains import ActionChains 
driver=webdriver.Chrome("./chromedriver")
driver.get("https://www.monsterindia.com/")
#sleep(5)
#actions=ActionChains(driver)
#job_search=driver.find_element_by_xpath("//a[text()='Job search']")
#actions.move_to_element(job_search).perform()
#job_loc=driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
#actions.move_to_element(job_loc).perform()

#driver.find_element_by_xpath("(//a[contains(text(),'Devops Jobs')] )[1]").click()
# driver.find_element_by_xpath("(//input[@type='text'])[9]").send_keys("PythonDeveloper")
# driver.find_element_by_xpath("//input[@value='Search']").click()
# titles=driver.find_elements_by_xpath("//div[@class='job-tittle']/h3/a")
# for title in titles:
#     print(title.text)
#     sleep(1)
