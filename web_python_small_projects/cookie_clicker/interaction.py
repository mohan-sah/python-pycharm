from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , value=True)

driver =  webdriver.Chrome(options=chrome_options)

driver.get(url=URL)

article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a").text
print(article_count)




driver.quit()

