from turtle import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.lazada.com.ph/products/199-mens-fashion-casual-waterproof-bag-usb-outdoor-backpack-schoolbag-laptop-super-affordable-random-backpacks-swipe-photos-for-the-random-items-to-be-received-strictly-no-choosing-sulit-lahat-ng-makukuha-dahil-maganda-ang-quality-para-sa-pres-i3157984808-s15713530890.html?spm=a2o4l.home.flashSale.4.5041359dDsmLOa&search=1&mp=1&c=fs&clickTrackInfo=rs%3A0.14130571484565735%3Bfs_item_discount_price%3A165.00%3Bitem_id%3A3157984808%3Bmt%3Ahot%3Bfs_utdid%3A-1%3Bfs_item_sold_cnt%3A50%3Babid%3A287818%3Bfs_item_price%3A89000.00%3Bpvid%3Addedbd7c-4c37-4d25-99d9-ae75381915b8%3Bfs_min_price_l30d%3A0%3Bdata_type%3Aflashsale%3Bfs_pvid%3Addedbd7c-4c37-4d25-99d9-ae75381915b8%3Btime%3A1661760817%3Bfs_biz_type%3Afs%3Bscm%3A1007.17760.287818.%3Bchannel_id%3A0000%3Bfs_item_discount%3A99%25%3Bcampaign_id%3A186839&scm=1007.17760.287818.0")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
time.sleep(1)
contents = driver.find_elements(By.CLASS_NAME,'item-content')
current_page_num = 1
while True:
    next_btn = driver.find_element(By.CLASS_NAME,'next-pagination-pages')
    btn = next_btn.find_elements(By.TAG_NAME,'button')
    num_pages = int(next_btn.text.split('...')[1])
    if num_pages+1==current_page_num:
        break
    # print(next_btn.text)
    for content in contents:
        print(content.text)
    print("-----------Page:"+str(current_page_num)+"----------------")
    time.sleep(0.3)
    btn[len(btn)-1].click()
    current_page_num+=1

driver.close()
