from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chromeDriverDirectory = './chromedriver'
driver = webdriver.Chrome(chromeDriverDirectory)
driver.get('https://www.google.com/maps')
time.sleep(2) # Let the user actually see something!
search_box = driver.find_element_by_id("searchboxinput")
search_box.send_keys('Cal Poly Pomona')
search_box.send_keys(Keys.ENTER)
photos = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "section-carouselphoto-photo-container"))
)[1].click()
time.sleep(5)
anchors = driver.find_element_by_class_name("widget-pane-visible").find_elements_by_tag_name('a')
print(len(anchors))
time.sleep(3)
for anchor in anchors:
    temp = anchor.get_attribute("href")
    print(temp)
    anchor.click()
    time.sleep(2)
time.sleep(5)
driver.quit()