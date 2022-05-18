from basepage import BasePage
from excel_lib import read_objects

class RegistraionPage(BasePage):
    regpage = read_objects("RegistrationPage")

    def register_select_male(self):
        self.click_element(self.regpage['rdo_male'])
    
    def register_select_female(self):
        self.click_element(self.regpage['rdo_female'])
    
    def register_enter_firstname(self, fname):
        self.enter_text(self.regpage['txt_firstname'], value=fname)
    
    def register_enter_lastname(self, lname):
        self.enter_text(self.regpage['txt_lastname'], value=lname)
    
    def register_enter_email(self, email):
        
        self.enter_text(self.regpage['txt_email'], value=email)
    
    def register_enter_password(self, password):
        self.enter_text(self.regpage['txt_password'], value=password)
    
    def register_enter_confirm_password(self, confirmpassword):
        self.enter_text(self.regpage['txt_confirm_password'], value=confirmpassword)
    
    def register_click_register(self):
        self.click_element(self.regpage['btn_register'])