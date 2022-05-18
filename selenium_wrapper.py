from selenium.webdriver.support.select import Select
from Wait import wait 
#from Library import *
class Selenium_Wrapper:
    def __init__(self,driver):
        self.driver=driver
    @wait
    def enter_text(self,locator,*,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)
    @wait
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
    @wait
    def select_item(self,locator,*,item):
        lst_box=self.driver.find_element(*locator)
        s=Select(lst_box)
        s.select_by_visible_text(item)
#s=Selenium_Wrapper(instance.driver)