import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#to keep it from closing
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', value=True)


driver = webdriver.Chrome(options=chrome_option)
# driver.get("https://www.amazon.in/AGARO-Imperial-Functions-Adjustable-Stainless/dp/B09XHX3191/ref=dp_prsubs_sccl_2/261-4700197-3858964?pd_rd_w=Yoa1V&content-id=amzn1.sym.d9c1aa74-df3a-4de8-8459-f574cbbceb60&pf_rd_p=d9c1aa74-df3a-4de8-8459-f574cbbceb60&pf_rd_r=TX1R1HZPFPJQ2Y92KFEN&pd_rd_wg=1kOmy&pd_rd_r=db3d1709-2f9e-4338-a9bd-ef0914b837ba&pd_rd_i=B09XHX3191&psc=1")
driver.get("https://www.python.org/")

# price_find = driver.find_element(by=By.CLASS_NAME, value="a-price-whole").text
# print(price_find)

# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# image_url = driver.find_element(by=By.ID, value="landingImage")
# print(image_url.get_attribute('src'))

# product_url = driver.find_element(by=By.CSS_SELECTOR, value=".a-row a")
# print(product_url.get_attribute("href"))

# submit_url = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_url.get_attribute("href"))

# creating a list of event dict
upcoming_event = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
dates = upcoming_event.find_elements(by=By.CSS_SELECTOR, value="ul li time")
names = upcoming_event.find_elements(by=By.CSS_SELECTOR, value="ul li a")
our_list = {}
#4. Using Dictionary Comprehension:
# our_list = {i: {"date": date.text,"name": name.text} for i,(date,name) in enumerate(zip(dates,names))}

#5. Using dict() with a List of Tuples:
# our_list  = dict((i,stamp) for i,(date,name) in enumerate(zip(dates,names)) for stamp in [{"date": date.text,"name":name.text }])


for (i,date,name) in zip(range(len(dates)),dates,names):
    stamp = {}
    stamp["date"] =  date.text
    stamp["name"] = name.text
    print(stamp)

    #Direct Assignment:
    # our_list[i]= stamp

    #2. Using the update() Method:
    # our_list.update({i:stamp})

    #3. Using setdefault():
    our_list.setdefault(i,stamp)

    #6. Using a Loop with dict():
    our_list = dict(our_list,**{f"{i}": stamp})

print(our_list)


time.sleep(1)
# driver.close() #close tab
driver.quit() #close browser


