
import requests
import json
from review_model import Review
from endecrypt import Deepy


 # sample url https://www.amazon.com/Robux-Roblox-Online-Game-Code/product-reviews/B07RZ74VLR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews
sampleurl = 'https://www.amazon.com/dp/B08VMV5Q3Z/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B08VMV5Q3Z&pd_rd_w=IbNBW&content-id=amzn1.sym.3be1c5b9-5b41-4830-a902-fa8556c19eb5&pf_rd_p=3be1c5b9-5b41-4830-a902-fa8556c19eb5&pf_rd_r=YF0W1WSWFKNEADFP8VK8&pd_rd_wg=ic0kd&pd_rd_r=30e597ff-46b2-4469-915a-3b966bb8bb96&s=videogames&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNzZEM0NRRUpVN09RJmVuY3J5cHRlZElkPUEwOTg3NzMxQlhHTEZVNEdEVktOJmVuY3J5cHRlZEFkSWQ9QTA3ODg3MTEyVkMzQ05RT09LODZGJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
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




