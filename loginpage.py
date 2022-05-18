from basepage import *
from excel_lib import read_objects

class LoginPage(BasePage):
    loginpage = read_objects("LoginPage")

    def login_enter_email(self, email):
        self.enter_text(("xpath","//input[@id='Email']"), value=email)
    
    def login_enter_password(self, password):
        self.enter_text(("name","Password"), value=password)
    
    def login_click_login(self):
        self.click_element(("xpath","//input[@value='Log in']"))
