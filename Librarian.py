bookList = []

for i in range(5):
    book = input("Enter book: ")
    bookList = bookList + [book]

bookList.sort()

print bookList