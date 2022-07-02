

class Review:
    def __init__(self,name,rating,title,style,comment,region,date,num_found_helpful = 0) -> None:
        self.name = name
        self.rating = rating
        self.title = title
        self.style = style
        self.comment = comment
        self.region = region
        self.date = date
        self.num_found_helpful = num_found_helpful
        self.title = title
        pass
    