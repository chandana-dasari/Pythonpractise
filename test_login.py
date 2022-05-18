from loginpage import LoginPage
import pytest
from pytest import mark
headers="email,password"
data=[("dasarichandana111@gmail.com","chandu"),("steve.jobs@company.com","password123")]
@mark.parametrize(headers,data)
def test_login(_driver,email,password):
    lp=LoginPage(_driver)
    