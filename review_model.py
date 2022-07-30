




class Review:
    def __init__(self,name,rating,title,comment,region,date,num_found_helpful = 0) -> None:
        self.name = name
        self.rating = rating
        self.title = title
        self.comment = comment
        self.region = region
        self.date = date
        self.num_found_helpful = num_found_helpful
    
    def jasonnize(self):
        return {
            'name':self.name,
            'rating':self.rating,
            'title':self.title,
            'comment':self.comment,
            'region':self.region,
            'date':self.date,
            'num_found_helpful':self.num_found_helpful,
        }

    def to_Object(object):
        return Review(
            name = object['name'],
            rating = object['rating'],
            title = object['title'],
            comment = object['comment'],
            region = object['region'],
            date = object['date'],
            num_found_helpful = object['num_found_helpful'],
        )
        
    