
import requests
import json
from review_model import Review
from endecrypt import Deepy


 # sample url https://www.amazon.com/Robux-Roblox-Online-Game-Code/product-reviews/B07RZ74VLR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews
sampleurl = 'https://www.amazon.com/Controller-Vertical-Charging-Accessories-Rechargeable/product-reviews/B08VMV5Q3Z/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
# sampleReviewURLList = sampleurl.split('/')
# sampleReviewURL = sampleReviewURLList[0]+"//"+sampleReviewURLList[2]+'/'+sampleReviewURLList[3]+'/'+'product-reviews'+'/'+sampleReviewURLList[5]+'/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
# print(sampleReviewURL)



#AMAZON URL
# sample_url = 'https://www.amazon.com/Roku-Express-Streaming-Wireless-Controls/product-reviews/B0916TKFF2/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

# #convert to ascii
ascii_url = Deepy.asciisize(sampleurl)
r = requests.get('http://127.0.0.1:5000/'+ascii_url)#append it to url request
print(r.content)
# json_objects = json.loads(r.content)#get the content of request
# reviews = []#empty list
# for x in json_objects:#alterate all json object from json_objects
#     review = Review.to_Object(json_objects[x])#create a review_model object from that json using to_Object
#     reviews.append(review)#append it to the list

# for review in reviews:#alterate all reviews
#     #so list of reviews man imu nakuha
#     #every review is an individual review sa user
#     #ato siya ge butang sa list
#     #then you can just say
#     print(review.name)#for example
#     print(review.title)#for example
#     print('-------------------------------')




