# import module
import requests
from bs4 import BeautifulSoup
from review_model import Review
import argparse

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
        region = ''
        if len(data_arr[2].split(' on')[0].split('Reviewed in the '))==1:
            region = data_arr[2].split(' on')[0].split('Reviewed in the ')[0]
        else:
             region = data_arr[2].split(' on')[0].split('Reviewed in the ')[1]
        date = data_arr[2].split('on ')[1].split('Style')[0]
        style =  data_arr[2].split('on ')[1].split('Style')[1].split(': ')[1].split('Verified Purchase')[0]
        comment = data_arr[3]
        num_found_helpful = data_arr[5].split(' ')[0]
        if num_found_helpful=='':
            num_found_helpful = 0
        review = Review(name,rating_double,title,style,comment,region,date,num_found_helpful)
        cus_list.append(review)
    return cus_list

def getReviewData(
    url = ''
):
    if url == '':
        return
    page = 1
    url.replace('pageNumber=1','')
    url = url+'&reviewerType=avp_only_reviews&pageNumber='
    while True:
        url = url+str(page)
        
        
        soup = html_code(url)
        cus_res = cus_data(soup)
        
    
        page+=1
        if cus_res == 'n/a':
            print("Ah shit")
            continue
        if len(cus_res) == 0:
            break
        for reviews in cus_res:
            print(reviews.name)
            rating = float(reviews.rating)
            rating_str = ""
            for x in range(0,int(rating)):
                rating_str+="*"
            print(rating_str)
            print(reviews.comment)
            print("-------------")
        print("-------------------------- Page: "+str(page-1))
    
def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, default='', help='File from')
    opt = parser.parse_args()
    return opt   

def main(opt):
    getReviewData(**vars(opt))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)