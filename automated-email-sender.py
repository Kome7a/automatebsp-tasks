#! python3
# automated-email-sender.py - Sends an email through cmd as follows - a-e-s.py [email to receiver] [message]

import sys
from selenium import webdriver

my_email = ""
my_pass = ""
browser = webdriver.Firefox()
browser.get("https://abv.bg")
browser.set_page_load_timeout(20)
browser.implicitly_wait(20)
# Remove cookies

gdpr_frame_id = "abv-GDPR-frame"

frame = browser.find_element_by_id(gdpr_frame_id)
browser.execute_script("arguments[0].remove()", frame)

browser.find_element_by_id("username").send_keys(my_email)
browser.find_element_by_id("password").send_keys(my_pass)
browser.find_element_by_id("loginBut").click()
browser.find_element_by_class_name("abv-button").click()
browser.find_element_by_class_name("clientField").click()

browser.find_element_by_xpath("""/html/body/div[1]/div/div[4]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]
/table/tbody/tr[2]/td[2]/div/input").send_keys(sys.argv[1]""")

mess = browser.find_element_by_class_name("gwt-RichTextArea").click()

browser.find_element_by_xpath("""/html/body/div[1]/div/div[4]/div/div[4]/div
/div[4]/div/div[2]/div/div[2]/div/iframe""").send_keys(sys.argv[2])

browser.find_element_by_class_name("abv-button").click()
browser.find_element_by_xpath("""/html/body/div[7]/div/table/tbody/tr[2]/td[2]/div
/table/tbody/tr[2]/td/div/div[1]""").click()
