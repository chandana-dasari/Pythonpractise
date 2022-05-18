#USING ABSOLUTE PATH
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome("./chromedriver")
#driver.get("file:///C:/Users/Jagadeesh/Desktop/Selenium_Training/Training/html%20files/xpath.html")
#sleep(5)
driver.get("http://demowebshop.tricentis.com/")
#sleep(5)
#driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()
#sleep(3)
#driver.refresh()
#driver.maximize_window()
#sleep(3)
#driver.minimize_window()
#sleep(5)
#foot=driver.find_element_by_xpath("(//div[@class='footer-menu-wrapper']//li)[1]")
#for link in foot:
#print(foot.text)
#search=driver.find_element_by_xpath('//input[contains(@class,"search-box-text ui-autocomplete-input")]').send_keys("Python")
#print(search.text)
#search.click()
#driver.find_element_by_xpath("//input[@value='Search']").click()
#driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys("Good")
#sleep(5)
#driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys("Morning")
#sleep(5)
#driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys("HGS")
#sleep(5)
#driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys("Bangalore")
#sleep(5)
#driver.find_element_by_xpath("//a[text()='Simple Computer']/../..//input[@value='Add to cart']").click()
'''expected_price={
                "$25 Virtual Gift Card":25.00,
                "14.1-inch Laptop":1590.00,
                "Build your own cheap computer":800,
                "Build your own computer":1200,
                "Build your own expensive computer":1800,
                "Simple Computer":800
                }
for gadget,expected_price in expected_price.items():
    _xpath=f"//a[text()='{item}']/../..//span[@class='price actual-price']"
    actual_price=driver.find_element_by_xpath("_xpath").text
    print(actual_price)
    if expected_price==float(actual_price):
        print("PASS")
    else:
        print("FAIL")
        #print(f"The expected price for {item} is {expected_price}but the actual price is {actual_price}")
'''
items=[
       "$25 Virtual Gift Card",
        "14.1-inch Laptop",
        "Build your own cheap computer",
        "Build your own computer",
        "Build your own expensive computer",
        "Simple Computer"
       ] 
for item in items:
    _xpath=f"//a[text()='{item}']/../..//span[@class='price actual-price']"
    actual_price=driver.find_element_by_xpath(_xpath).text
    print(actual_price)  
item=[
       ("$25 Virtual Gift Card",25.00),
        ("14.1-inch Laptop",1590.00),
        ("Build your own cheap computer",800),
        ("Build your own computer",1200),
        ("Build your own expensive computer",1800),
        ("Simple Computer",800)
       ] 
for item in items:
    gadget,expected_price=item
    _xpath=f"//a[text()='{item}']/../..//span[@class='price actual-price']"
    actual_price=driver.find_element_by_xpath("_xpath").text
    print(actual_price)
    if float(actual_price)==expected_price:
        print("PASS")
    else:
        print("FAIL")
