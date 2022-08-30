from turtle import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from models import Review
# from app import sentiment_scores
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    overallRating = ''
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        overallRating = 'Positive'
    elif sentiment_dict['compound'] <= - 0.05 :
        overallRating = "Negative"
    else :
        overallRating = "Neutral"
    return {'overallSentiment':sentiment_dict,'overallRating':overallRating}
    
# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# options.add_argument('--headless')




def getReviews(url):
    

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    all_comment = driver.find_element(By.CLASS_NAME,'product-rating-overview__filters')
    all_div_comment =all_comment.find_elements(By.TAG_NAME,'div')
   
    num_pages = 0
    try:
        num_pages = round(int(all_div_comment[6].text.split('(')[1].split(')')[0])/6)
    except:
        num_pages = 50
    current_page_num = 1
    reviews = []
    while True:
        if num_pages==current_page_num:
            driver.close()
            return reviews

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
            review = Review(name=name,rating=stars,title='',comment=comment,region='',date=rating_time,sentiment=sentiment_scores(comment))
            reviews.append(review)
        # trigger next page
        next_btn = driver.find_element(By.CLASS_NAME,"shopee-icon-button--right ")
        next_btn.click()
        time.sleep(0.05)
        current_page_num+=1
    

# sampleurl = 'https://shopee.ph/2022-Best-selling-Korean-ladies-white-shoes-i.174274877.7867509069?sp_atk=a3166c4c-9041-418d-bbe5-6c43a41749c9&xptdk=a3166c4c-9041-418d-bbe5-6c43a41749c9s'
# print(getReviews(sampleurl))