from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#Imports para evitar fechamento imediato do Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Códigos para evitar crash do Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

navigator = webdriver.Chrome(options=chrome_options)

navigator.get("https://google.com")
navigator.find_element("xpath", '//*[@id="APjFqb"]').send_keys('Huawei Wikipédia')
navigator.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()