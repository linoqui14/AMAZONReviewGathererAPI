
import requests
import json
from review_model import Review
from endecrypt import Deepy


 # sample url https://www.amazon.com/Robux-Roblox-Online-Game-Code/product-reviews/B07RZ74VLR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews
sampleurl = 'https://www.amazon.com/Xbox-Wireless-Controller-Pulse-Red-Windows-Devices/dp/B0859XT328/ref=pd_rhf_d_cr_s_pd_crcd_sccl_1_5/138-6449856-6123309?pd_rd_w=FzIna&content-id=amzn1.sym.cee83ff1-8fc1-4533-a3f5-bf3d998f4558&pf_rd_p=cee83ff1-8fc1-4533-a3f5-bf3d998f4558&pf_rd_r=KN035TNTA8WE0GEGT514&pd_rd_wg=Anm5q&pd_rd_r=670f533c-46d1-4e81-a7c3-6acc5bf40ba3&pd_rd_i=B0859XT328&psc=1'
# sampleReviewURLList = sampleurl.split('/')
# sampleReviewURL = sampleReviewURLList[0]+"//"+sampleReviewURLList[2]+'/'+sampleReviewURLList[3]+'/'+'product-reviews'+'/'+sampleReviewURLList[5]+'/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
# print(sampleReviewURL)



#AMAZON URL
# sample_url = 'https://www.amazon.com/Roku-Express-Streaming-Wireless-Controls/product-reviews/B0916TKFF2/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

# #convert to ascii
ascii_url = Deepy.asciisize(sampleurl)


print(ascii_url)
# r = requests.get('https://argatherer.herokuapp.com/'+ascii_url)#append it to url request

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




