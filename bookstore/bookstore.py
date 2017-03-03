class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.library = []
        
    def get_books(self):
        return self.library
        
    def add_book(self, book):
        self.library.append(book)
        
    def search_books(self, title = None, author = None):
        search_return = []
        for item in self.library:
            if author is not None:
                if author.name in item.author.name:
                    search_return.append(item)
            elif title is not None:
                if title.lower() in item.title.lower():
                    search_return.append(item)
        return search_return


class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.library = []
        
    def get_books(self):
        return self.library


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.library.append(self)
