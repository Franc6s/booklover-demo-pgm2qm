import pandas as pd

class BookLover:
    def __init__(self,name,email,fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})

    def add_book(self,book_name,rating):
        try: 
            rating >=1 and rating <=5
        except:
            print("ratings cannot be below 1 and above 5")

        if book_name in self.book_list:
            print(f"{book_name} already exists.")
        else :
            new_book = pd.DataFrame({'book_name':[book_name],'book_rating':[rating]})
            self.book_list = pd.concat([self.book_list,new_book], ignore_index=True)
            self.num_books +=1
            print(f"{book_name} was successfully added")
    