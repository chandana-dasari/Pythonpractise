from registrationpage import RegistraionPage
from pytest import mark

headers = "fname, lname, email, password"
data = [
        ("Steve", "Jobs", "Steve.Jobs@company.com", "Password123"), 
        ("Bill", "Gates", "Bill.Gates@company.com", "Password123")
        ]
@mark.parametrize(headers, data)
def test_registration(_driver, fname, lname, email, password):
    rp = RegistraionPage(_driver)
    rp.base_click_register()
    rp.register_select_male()
    rp.register_enter_firstname(fname)
    rp.register_enter_lastname(lname)
    rp.register_enter_email(email)
    rp.register_enter_password(password)
    rp.register_enter_confirm_password(password)
    rp.register_click_register()