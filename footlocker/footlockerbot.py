from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()

browser.get("https://footlocker.com")
assert 'Sneakers - Athletic Shoes | Foot Locker' in browser.title
