# class Notansunzon:
#     def displayinfo(self):
#         print('Welcome to Notansunzone')
        
# demoobject= Notansunzon()

# demoobject.displayinfo()


class Book:
    def summary(self, title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

        print(self.title, self.author, self.pages)
        

mybook = Book()
mybook.summary('Harry Potter', 'Paresh', 100)