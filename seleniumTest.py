from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()

browser.get("https://shop-usa.palaceskateboards.com/")
#assert 'Google' in browser.title

elem = browser.find_element_by_class_name('product-link')  # Find the search box
elem.click()

buy = browser.find_element_by_name('button')
buy.click()
#elem.send_keys('baik19@vt.edu')

#search = 