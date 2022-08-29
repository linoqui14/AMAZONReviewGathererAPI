
import requests
import json
from review_model import Review
from endecrypt import asciisize,deasciisize



sampleurl = 'https://shopee.ph/2022-Best-selling-Korean-ladies-white-shoes-i.174274877.7867509069?sp_atk=a3166c4c-9041-418d-bbe5-6c43a41749c9&xptdk=a3166c4c-9041-418d-bbe5-6c43a41749c9s'

# #convert to ascii
ascii_url = asciisize(sampleurl)
r = requests.get('http://127.0.0.1:5000/'+ascii_url)#append it to url request

json_objects = json.loads(r.content)#get the content of request
reviews = []#empty list
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
#     print(review.comment)
#     print(review.sentiment)
#     print('-------------------------------')







