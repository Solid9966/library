class BookNotFound(Exception):
    # case : required book is not exist
    pass
class BookHasNoBorrowHistory(Exception):
    # case : there is not history of book loan
    pass