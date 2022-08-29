from turtle import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# options.add_argument('--headless')
driver = webdriver.Chrome()
driver.get("https://shopee.ph/New-Rubber-Shoes-Breathable-Sneakers-Korean-Shoes-For-Women-i.218082310.15738934670?sp_atk=52048e25-8a60-423d-86fd-f885737fcb73&xptdk=52048e25-8a60-423d-86fd-f885737fcb73")
time.sleep(5)
all_comment = driver.find_element(By.CLASS_NAME,'product-rating-overview__filters')
all_div_comment =all_comment.find_elements(By.TAG_NAME,'div')
num_pages = round(int(all_div_comment[6].text.split('(')[1].split(')')[0])/6)

current_page_num = 1
while True:
    if num_pages==current_page_num:
        break

    elems = driver.find_elements(By.CLASS_NAME,'shopee-product-rating__main')
    # go through all the comments
    for x in elems:
        comment = ''
        try:
            comment = x.find_element(By.CLASS_NAME,'_280jKz').text
        except:
            break

        name = x.find_element(By.CLASS_NAME,'shopee-product-rating__author-name').text
        star_container = x.find_element(By.CLASS_NAME,'shopee-product-rating__rating')
        stars = len(star_container.find_elements(By.TAG_NAME,'svg'))
        rating_time = x.find_element(By.CLASS_NAME,'shopee-product-rating__time').text.split('|')[0]
        variation = x.find_element(By.CLASS_NAME,'shopee-product-rating__time').text.split('|')[1]

        print("name: "+name)
        print("--------------")
        print(comment)
        print("-----------------------------------------------------")
    # trigger next page
    next_btn = driver.find_element(By.CLASS_NAME,"shopee-icon-button--right ")
    next_btn.click()
    # time.sleep(0.3)
    current_page_num+=1
driver.close()
