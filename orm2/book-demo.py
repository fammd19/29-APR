from author import Author
from book import Book

# Author.create_table()
# Book.create_table()

# Author.create("Fi")
# Author.create("Mack")
# Author.create("Mary")

# Book.create("Fi book", "Fiction", 1)
# Book.create("Fi book 2", "Fiction", 1)
# Book.create("Mack's mad maths", "Non-fiction", 2)
# Book.create("Mary had a little lamb", "Adventure", 3)

# for author in Author.get_all():
#     print(author.name)

# for book in Book.get_all():
#     print(f"{book.title} by {book.author_name()}")

# books = Book.find_by_author("Fi")

# for book in books:
#     print(f"{book.title} by {book.author_name()}")

new_author = Author.create("J.K.")
new_author.add_book("HP", "Fiction")
new_author.add_book("HP 2", "Fiction")