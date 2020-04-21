from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get("https://play2048.co/")
element = browser.find_element_by_tag_name("html")
while True:
    element.send_keys(Keys.ARROW_RIGHT)
    element.send_keys(Keys.ARROW_DOWN)
    element.send_keys(Keys.ARROW_UP)
    element.send_keys(Keys.ARROW_LEFT)
