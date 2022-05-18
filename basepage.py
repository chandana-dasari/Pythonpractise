from selenium_wrapper import Selenium_Wrapper

class BasePage(Selenium_Wrapper):

    def base_click_login(self):

        self.click_element(("xpath","//a[text()='Log in']"))

    def base_click_register(self):
        
        self.click_element(("xpath","//a[text()='Register']"))
