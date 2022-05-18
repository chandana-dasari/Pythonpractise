#from selenium import webdriver
#from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self,driver):
        result=super().__call__(driver)
        if isinstance(result,WebElement):
            return result.is_enabled()
        else:
            return False
def wait(func):
    def wrapper(*args,**kwargs):
        instance=args[0]
        #print(instance)
        locator=args[1]
        #print(locator)
        w=WebDriverWait(instance.driver,10)
        v=_visibility_of_element_located(locator)
        w.until(v)
        return func(*args,**kwargs)
    return wrapper