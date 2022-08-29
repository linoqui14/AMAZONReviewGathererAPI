import json
from flask import Flask
import requests
from bs4 import BeautifulSoup
from models import Review
import wordninja as wninja
from endecrypt import asciisize,deasciisize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)

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


# ‘/’ URL is bound with hello_world() function.

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text
def html_code(url):
  
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    
    # display html code
    return (soup)

def cus_data(soup):
    cus_list = []
    for item in soup.find_all("div", attrs={'data-hook','review'}):
        
        data_arr = item.get_text().split('\n')
        rating = data_arr[0][-18:]
        rating_double = rating.split(' ')[0]
        if len(data_arr[0]) == 0:
            continue      
        name = data_arr[0].split(rating)[0]
        title = data_arr[1]
        test1 = data_arr[2].replace("Reviewed in the ", "").replace("Reviewed in ", "").replace("on", "")
        test2 = test1.split(" ")
        test2 = list(filter(None, test2))
        test3 = []
        test = 0
        i = 0
        monthscanner = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        # loop purpose not finished
        while(i != len(monthscanner)):
            try:
                test = test2.index(monthscanner[i])
            except:
                pass #idk wadufook
            test3.append(test2[test])
            i = i + 1
        region = ''
        #check if region is correctly split
        if len(data_arr[2].split(' on')[0].split('Reviewed in the '))==1:
            region = data_arr[2].split(' on')[0].split('Reviewed in ')[1]
            if region == '':
                region = data_arr[2].split(' on')[0].split('Reviewed in ')[0]
        else:
            region = data_arr[2].split(' on')[0].split('Reviewed in the ')[1]
        #getting date and remove undesired words
        date = wninja.split(data_arr[2].split('on ')[1])[0:3]
        comment = data_arr[3]
        num_found_helpful = data_arr[5].split(' ')[0]
        if num_found_helpful=='':
            num_found_helpful = 0
        review = Review(name,rating_double,title,comment,region,date,num_found_helpful,sentiment_scores(comment))
        cus_list.append(review)
    return cus_list
@app.route('/')
def test():
    return 'Test'

@app.route('/<url>',methods=['GET'])

def getReviewData(
    url = ''
):
    
    url =  deasciisize(url)
    if 'https://shopee.ph/' in url:
        print(url)
        soup = html_code(url)
        review = soup.find_all("div",attrs={"class": "product-rating-overview"})
        print(soup)
        # cus_res = cus_data(soup)

        return {
            'site':'shoppe'
        }
    urlsplit = url.split('/')
    if urlsplit[3] == 'dp':
        return {
            'error':'please go to review page of this product then use that link'
        }
    else:    
        url = urlsplit[0]+"//"+urlsplit[2]+'/'+urlsplit[3]+'/'+'product-reviews'+'/'+urlsplit[5]+'/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    if url == '':
        return ''
    page = 1
    url.replace('pageNumber=1','')
    url = url+'&reviewerType=avp_only_reviews&pageNumber='

    reviews = []
    while True:
            url = url+str(page)
            soup = html_code(url)
            cus_res = cus_data(soup)
            page+=1
            if cus_res == 'n/a':
                continue
            if len(cus_res) == 0:
                break
            for review in cus_res:
                # print(review.sentiment)
                reviews.append(review)
     

     
    to_json_array = {}
    for i,review in enumerate(reviews):
        to_json_array[i] = review.jasonnize()
       
    return json.dumps(to_json_array)
    # return json.dumps(to_json_array)

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()