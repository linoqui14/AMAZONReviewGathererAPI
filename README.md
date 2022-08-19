# AMAZON ReviewGatherer API
This API will get all the Verified Purchase reviews
Please install following dependencies

# How to use
1. Run the server by running app.py
2. On you code, the amazon url must be converted using asciisize(url) function from endecrypt.py 

    ```python
    amazon_url = asciisize('https://www.amazon.com/Controller-Vertical-Charging-Accessories-Rechargeable/product-reviews/B08VMV5Q3Z/ref=cm_cr_dp_d_show_all_btm?      ie=UTF8&reviewerType=all_reviews')
    ```
3. Use request to get the result from the server
    ```python
    r = requests.get('http://127.0.0.1:5000/'+amazon_url)
    ```
4. Make it into a json object using json.loads
    ```python
    json_objects = json.loads(r.content)#get the content of request
    ```
5. Recommended that you must put all the object in a list for easy use
   ```python
   reviews = []#for review model
   ```
6. Loop all the json object and convert it into a Review object using Review.to_object function from Review model class
    ```python
    for x in json_objects:#alterate all json object from json_objects
       review = Review.to_Object(json_objects[x])#create a review_model object from that json using to_Object
       reviews.append(review)#append it to the list
    ```
 # Full example code
```python
import requests
import json
from review_model import Review
from endecrypt import Deepy



sampleurl = 'https://www.amazon.com/Controller-Vertical-Charging-Accessories-Rechargeable/product-reviews/B08VMV5Q3Z/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

# #convert to ascii
ascii_url = Deepy.asciisize(sampleurl)
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




```
# You can use this api instead of running it locally 
## API URL - please dont abuse it 😊

(https://argatherer.herokuapp.com/)




