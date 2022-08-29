from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.lazada.com.ph/products/bighi-laundry-beads-detergent-strong-stain-removal-long-lasting-scent-laundry-detergent-gel-long-fragrance-3in1-liquid-high-concentration-laundry-fragrance-beads-50pcs-i2979197945-s14584953753.html?spm=a2o4l.home.flashSale.3.239e359dfWDO4q&search=1&mp=1&c=fs&clickTrackInfo=rs%3A0.6047999858856201%3Bfs_item_discount_price%3A131.00%3Bitem_id%3A2979197945%3Bmt%3Ahot%3Bfs_utdid%3A-1%3Bfs_item_sold_cnt%3A190%3Babid%3A287818%3Bfs_item_price%3A290.00%3Bpvid%3Ad84e8e19-ddb5-4a57-82ce-4fea1e8d68ed%3Bfs_min_price_l30d%3A0%3Bdata_type%3Aflashsale%3Bfs_pvid%3Ad84e8e19-ddb5-4a57-82ce-4fea1e8d68ed%3Btime%3A1661446547%3Bfs_biz_type%3Afs%3Bscm%3A1007.17760.287818.%3Bchannel_id%3A0000%3Bfs_item_discount%3A55%25%3Bcampaign_id%3A186665&scm=1007.17760.287818.0")

elems = driver.find_elements(By.CLASS_NAME, "mod-reviews")
for el in elems:
    print('-------------------------')
    print(el.get_attribute('innerHTML'))
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)


