class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contract in Contract.all: 
            if contract.author == self:
                total += contract.royalties
        return total


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]



class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if type(author) is Author:
            self.author = author
        else:
            raise TypeError("Not an author")

        if type(book) is Book:
            self.book = book
        else:
            raise TypeError("Not a book")
    
        if type(date) is str:
            self.date = date
        else:
            raise TypeError("Not a string")
        
        if type(royalties) is int or type(royalties) is float:
            self.royalties = royalties
        else: 
            raise TypeError("Not a number")
        
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

