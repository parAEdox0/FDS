# Write a Python program for department library which has N books, write
# functions for following:
# a) Delete the duplicate entries
# b) Display books in ascending order based on cost of books
# c) Count number of books with cost more than 500.
# d)Copy books in a new list which has cost less than 500.

book_list = []
price_list = []
unique_books = []
unique_price = []

# print("Enter book details (format: <book_name> <cost>). Press Enter with an empty line to finish input.")
# while True:
#     data = input("Enter book details: ")
#     if data == "":
#         break
#     else:
#         data = data.split(" ")
#         book_list.append(data[0])
#         price_list.append(int(data[1]))

number_of_books = int(input("Enter Number of Entries you want to make : "))
for i in range(0, number_of_books):
    entry = input(f"Enter book {i+1} details : ")
    split = entry.split(" ")
    book_list.append(split[0])
    price_list.append(split[1])

print()
print("Entered book names:", book_list)
print("Entered costs:", price_list)
print()

def duplicate():

    for i in range (0, len(book_list)):
        if book_list[i] not in unique_books:
            unique_books.append(book_list[i])
            unique_price.append(price_list[i])
    print("************* after deleting duplicate entries ***************")
    print()
    for i in range(0, len(unique_books)):
        print(f"{unique_books[i]} = {unique_price[i]}")
    print()

def sorting():
    for i in range(0, len(unique_price)):
        for j in range(i + 1, len(unique_price)):
            if unique_price[i] > unique_price[j]:
                temp_price = unique_price[i]
                unique_price[i] = unique_price[j]
                unique_price[j] = temp_price
                temp_book = unique_books[i]
                unique_books[i] = unique_books[j]
                unique_books[j] = temp_book
    print("************* after sorting according to cost ***************")
    print()
    for i in range(0, len(unique_books)):
        print(f"{unique_books[i]} = {unique_price[i]}")
    print()

def above_fivehundred():
    above_books = []
    above_price = []
    for i in range(0, len(unique_price)):
        if int(unique_price[i]) > 500:
            above_books.append(unique_books[i])
            above_price.append(unique_price[i])
    print("************* list of books having cost more than 500 *****************")
    print()
    for i in range(0, len(above_books)):
        print(f"{above_books[i]} = {above_price[i]}")
    print(f"Total = {len(above_books)}")
    print()

def below_fivehundred():
    below_books = []
    below_price = []
    for i in range(0, len(unique_price)):
        if int(unique_price[i]) < 500:
            below_books.append(unique_books[i])
            below_price.append(unique_price[i])
    print("************* list of books having cost less than 500 *****************")
    print()
    for i in range(0, len(below_books)):
        print(f"{below_books[i]} = {below_price[i]}")
    print(f"Total = {len(below_books)}")
    print()

duplicate()
sorting()
above_fivehundred()
below_fivehundred()
