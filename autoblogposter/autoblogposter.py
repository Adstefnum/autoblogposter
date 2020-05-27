from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#getting input
blog_url = input("Enter the link to your wordpress blog:")
usernameKey = input("Enter your username:")
passwordKey = input("Enter your password:")

#getting the name of post and post info
path_to_post_file = r'C:\Users\USER\Documents\PYTHON PROJECTS\autoblogposter\post/'
file = os.listdir(path_to_post_file)
title_int = file[0].split(".")
title = title_int[0]

details = open(path_to_post_file+file[0],'r')
post = details.read()

#finding the appropriate buttons and places and perfroming needed action
browser = webdriver.Chrome()
browser.get(blog_url)

username = browser.find_element_by_id('user_login')
username.send_keys(usernameKey)

password = browser.find_element_by_id('user_pass')
password.send_keys(passwordKey)

loginBtn = browser.find_element_by_id('wp-submit')
loginBtn.click()

newPostBtn = browser.find_element_by_link_text('New')
newPostBtn.click()

titleArea = browser.find_element_by_id('post-title-0')
titleArea.send_keys(title)
titleArea.send_keys(Keys.ENTER)
titleArea.send_keys(Keys.TAB)
titleArea.send_keys(post)

pubBtn = browser.find_element_by_css_selector("#editor > div > div > div.components-navigate-regions > div > div.block-editor-editor-skeleton__header > div > div.edit-post-header__settings > button.components-button.editor-post-publish-panel__toggle.editor-post-publish-button__button.is-primary")
pubBtn.click()

finalBtn = browser.find_element_by_css_selector("#editor > div > div > div.components-navigate-regions > div > div.block-editor-editor-skeleton__body > div.block-editor-editor-skeleton__publish > div > div > div > div.editor-post-publish-panel__header > div > button")
finalBtn.click()

