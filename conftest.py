from _pytest.monkeypatch import derive_importpath
from pytest import fixture
from selenium import webdriver
@fixture
def spam():
    print("Launching browser")
    driver=webdriver.Chrome("./chromedriver")
    driver.get("http://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    print("closing browser")
    driver.quit()
