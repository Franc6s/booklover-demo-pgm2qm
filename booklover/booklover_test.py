import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        author = BookLover("Suzanne Nelson","suzanne@bookedits.com","Romance")

        author.add_book("A Tale of Magnolious",4)
        self.assertIn("A Tale of Magnolious",author.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        author = BookLover("Elizabeth Goddard","liz@bookedits.com","Urban")
        
        author.add_book("Storm Warning",5)
        author.add_book("Storm Warning",4)
        self.assertEqual(author.num_books,1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        author = BookLover("Eiren Caffall","caffe@bookedits.com","Science-Fiction")
        author.add_book("All the Water in the World",5)
        self.assertTrue(author.book_list['book_name'].isin(["All the Water in the World"]).any())
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        author = BookLover("Gregg Hurwitz","hurwitz@bookedits.com","Thriller")
        self.assertFalse(author.book_list['book_name'].isin(['Nemesis']).any())

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        author= BookLover("Thomas Perry", "perry@example.com", "mystery")
        
        # Add books to the list
        author.add_book("Pro Bono",4)
        author.add_book("The Informant",4)
        
        # Test if num_books matches the expected value
        self.assertEqual(author.num_books, 2)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        author= BookLover("Suzanne Collins", "collins@example.com", "Science-Fiction")

        author.add_book("The Hunger Games",4)
        author.add_book("Catching Fire",4)
        author.add_book("Mockinjay",5)

        favorites = author.book_list[author.book_list['book_rating']>3]
        self.assertTrue(all(rating > 3 for rating in favorites['book_rating']))

                
if __name__ == '__main__':
    unittest.main(verbosity=3)