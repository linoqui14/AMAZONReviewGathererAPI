
import requests
import json
from review_model import Review
from endecrypt import Deepy



#AMAZON URL
sample_url = 'https://www.amazon.com/Roku-Express-Streaming-Wireless-Controls/product-reviews/B0916TKFF2/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
#convert to ascii
ascii_url = Deepy.asciisize(sample_url)



r = requests.get('http://127.0.0.1:5000/'+ascii_url)#append it to url request

json_objects = json.loads(r.content)#get the content of request
reviews = []#empty list
for x in json_objects:#alterate all json object from json_objects
    review = Review.to_Object(json_objects[x])#create a review_model object from that json using to_Object
    reviews.append(review)#append it to the list

for review in reviews:#alterate all reviews
    #so list of reviews man imu nakuha
    #every review is an individual review sa user
    #ato siya ge butang sa list
    #then you can just say
    print(review.name)#for example
    print(review.title)#for example
    print('-------------------------------')




