from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.naukri.com/")
time.sleep(4)

win_handles = driver.window_handles  # Get all the window handles
for handle in win_handles:
   driver.switch_to.window(handle)
#driver.close()
driver.quit()


#Write a script to count the number of browsers opened by selenium

#from selenium import webdriver
#import time

#driver = webdriver.Chrome('./chromedriver')
#driver.get("https://www.naukri.com/")
#time.sleep(4)

#win_handles = driver.window_handles  # Get all the window handles
#print('No of Browsers: ',len(win_handles))
