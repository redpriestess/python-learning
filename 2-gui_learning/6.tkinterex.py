'''
Tkinter Programming Problem: Library Book Rental System

You are asked to build a small desktop application for a community library using Tkinter.

Scenario:
The library keeps books in different categories. Each book has:

* title
* author
* category
* number of available copies

Users can:

1. View all available books
2. Borrow a book
3. Return a book
4. See how many books they have borrowed

Requirements:

1. Data Structure

* Store all books in a dictionary.

* The key should be the book title.

* The value should be another dictionary containing:

  * author
  * category
  * available_copies

* Maintain a list to store the titles borrowed by the current user.

2. GUI Requirements
   Create a Tkinter window with:

* An Entry widget where the user types a book title.
* Buttons:

  * View Books
  * Borrow Book
  * Return Book
  * My Borrowed Books
* A Text widget or Listbox to display results.

3. Functional Requirements

A. View Books

* Use a for loop to go through the dictionary.
* Display each book with title, author, category, and available copies.
* If no books are available, show a message using an if condition.

B. Borrow Book

* When the user enters a title and clicks Borrow:

  * Use an if condition to check if the title exists in the dictionary.
  * If it exists, check if available_copies > 0.
  * If yes:

    * Decrease available_copies by 1.
    * Add the book title to the borrowed books list.
  * If no copies are available, show a message.
  * If the book does not exist, show a message.

C. Return Book

* Use a while loop to search through the borrowed books list to see if the user has borrowed that book.
* If found:

  * Remove one occurrence from the list.
  * Increase available_copies in the dictionary.
* If not found, show a message.

D. My Borrowed Books

* Use a dictionary to count how many times each title appears in the borrowed books list.
* Display the count of each borrowed book using a for loop.
* If the list is empty, show a message.

4. Function Design

* Write separate functions for:

  * view_books()
  * borrow_book()
  * return_book()
  * show_borrowed_books()
* Connect each function to its corresponding button.

5. Additional Rule

* The program should keep running until the user closes the window.
* All logic must be implemented using:

  * if conditions
  * lists
  * dictionaries
  * for loops
  * at least one while loop
  * user defined functions
'''


# books= {
#     "Harry Potter":{
#         "author":"JK rowling",
#         "category":"Non fiction",
#         "copies":3},
    
#     "Aryan":{
#         "author":"Rishka",
#         "category":"life",
#         "copies":4},
    
#     "Life of Pi":{
#         "author":"druvosky",
#         "category":"fantasy",
#         "copies":3}

# }

# borrowed_books = []
# def viewing():
#     data=""
#     for title,info in books.items():
#         data+=(f"{title}:{info["author"]}:{info["category"]}: {info["copies"]}\n")
#         label_viewbooks.config(text=data)
# def borrowing():
#     title=entry_borrowbooks.get()
#     if title in books:
#         if books[title]["copies"]>0:
#             books[title]["copies"]-=1
#             borrowed_books.append(title)
#             label_viewborrows.configure(text=f"Borrowed={borrowed_books}") 
#         else:
#             label_viewborrows.configure(text=f"no borrowed books")

    
# def returning():
#     book_name=label_returnbooks.get()
#     if book_name in borrowed_books:
#         borrowed_books.remove(book_name)
#         actuallabel_returnbooks.configure(text=f"You are returning {book_name}")
#     if book_name in books:
#         books[book_name]["copies"]+=1
#         actuallabel_returnbooks.configure(text=f"You are returning {book_name}")
#     else:
#         actuallabel_returnbooks.configure(text=f"book not found")

# def view_borrowed():

#     if not borrowed_books:
#         label_viewborrows.config(text="No books borrowed")
#         return
#     counts = {}
#     for book in borrowed_books:
#         if book in counts:
#             counts[book] += 1
#         else:
#             counts[book] = 1
#     text = ""
#     for title, number in counts.items():
#         text += f"{title} : {number}\n"

#     label_viewborrows.config(text=text)
   





# import tkinter as tk

# window=tk.Tk()
# window.title("Library book rental system") 
# window.geometry("1000x600")

# form_label=tk.Label(window,text="library book rental system",font=("Aptos",15))
# form_label.pack()

# button_viewbooks=tk.Button(window,text="view books",font=("Aptos",10), command=viewing)
# button_viewbooks.pack(anchor="w",padx=10,pady=10)

# label_viewbooks=tk.Label(window,text="",font=("Aptos",10))
# label_viewbooks.pack(anchor="w",padx=10,pady=10)

# button_borrowbooks=tk.Button(window,text="borrow books",font=("Aptos",10),command=borrowing)
# button_borrowbooks.pack(anchor="w",padx=10,pady=10)

# entry_borrowbooks=tk.Entry(window,text="",font=("Aptos",10))
# entry_borrowbooks.pack(anchor="w",padx=10,pady=10,fill="x")

# button_addbooks=tk.Button(window,text="Add books",font=("Aptos",10))
# button_addbooks.pack(anchor="w",padx=10,pady=10)

# entry_addbooks=tk.Entry(window,text="",font=("Aptos",10))
# entry_addbooks.pack(anchor="w",padx=10,pady=10,fill="x")

# button_returnbooks=tk.Button(window,text="return books",font=("Aptos",10),command=returning)
# button_returnbooks.pack(anchor="w",padx=10,pady=10)

# label_returnbooks=tk.Entry(window,text="",font=("Aptos",10))
# label_returnbooks.pack(anchor="w",padx=10,pady=10,fill="x")

# actuallabel_returnbooks=tk.Label(window,text="",font=("Aptos",10))
# actuallabel_returnbooks.pack(anchor="w",padx=10,pady=10)

# button_viewborrows=tk.Button(window,text="borrowed books",font=("Aptos",10))
# button_viewborrows.pack(anchor="w",padx=10,pady=10)

# label_viewborrows=tk.Label(window,text="",font=("Aptos",10))
# label_viewborrows.pack(anchor="w",padx=10,pady=10)
# window.mainloop()



'''as a table'''


books= {
    "Harry Potter":{
        "author":"JK rowling",
        "category":"Non fiction",
        "copies":3},
    
    "Aryan":{
        "author":"Rishka",
        "category":"life",
        "copies":4},
    
    "Life of Pi":{
        "author":"druvosky",
        "category":"fantasy",
        "copies":3}

}

borrowed_books = []
def viewing():
    data=""
    for title,info in books.items():
        data+=(f"{title}:{info["author"]}:{info["category"]}: {info["copies"]}\n")
        label_viewbooks.config(text=data)
def borrowing():
    title=entry_borrowbooks.get()
    if title in books:
        if books[title]["copies"]>0:
            books[title]["copies"]-=1
            borrowed_books.append(title)
            label_viewborrows.configure(text=f"Borrowed={borrowed_books}") 
        else:
            label_viewborrows.configure(text=f"no borrowed books")

    
def returning():
    book_name=label_returnbooks.get()
    if book_name in borrowed_books:
        borrowed_books.remove(book_name)
        actuallabel_returnbooks.configure(text=f"You are returning {book_name}")
    if book_name in books:
        books[book_name]["copies"]+=1
        actuallabel_returnbooks.configure(text=f"You are returning {book_name}")
    else:
        actuallabel_returnbooks.configure(text=f"book not found")

def view_borrowed():

    if not borrowed_books:
        label_viewborrows.config(text="No books borrowed")
        return
    counts = {}
    for book in borrowed_books:
        if book in counts:
            counts[book] += 1
        else:
            counts[book] = 1
    text = ""
    for title, number in counts.items():
        text += f"{title} : {number}\n"

    label_viewborrows.config(text=text)
   





import tkinter as tk
from tkinter import ttk 

window=tk.Tk()
window.title("Library book rental system") 
window.geometry("1000x600")

form_label=tk.Label(window,text="library book rental system",font=("Aptos",15))
form_label.pack()

button_viewbooks=tk.Button(window,text="view books",font=("Aptos",10), command=viewing)
button_viewbooks.pack(anchor="w",padx=10,pady=10)

table=ttk.Treeview(window,columns=("col1","col2","col3","col4"),show="headings")
table.heading("col1",text="Book title")
table.heading("col2",text="Author")
table.heading("col3",text="Number of Copies")
table.pack()

button_borrowbooks=tk.Button(window,text="borrow books",font=("Aptos",10),command=borrowing)
button_borrowbooks.pack(anchor="w",padx=10,pady=10)

entry_borrowbooks=tk.Entry(window,text="",font=("Aptos",10))
entry_borrowbooks.pack(anchor="w",padx=10,pady=10,fill="x")

button_addbooks=tk.Button(window,text="Add books",font=("Aptos",10))
button_addbooks.pack(anchor="w",padx=10,pady=10)

entry_addbooks=tk.Entry(window,text="",font=("Aptos",10))
entry_addbooks.pack(anchor="w",padx=10,pady=10,fill="x")

button_returnbooks=tk.Button(window,text="return books",font=("Aptos",10),command=returning)
button_returnbooks.pack(anchor="w",padx=10,pady=10)

label_returnbooks=tk.Entry(window,text="",font=("Aptos",10))
label_returnbooks.pack(anchor="w",padx=10,pady=10,fill="x")

actuallabel_returnbooks=tk.Label(window,text="",font=("Aptos",10))
actuallabel_returnbooks.pack(anchor="w",padx=10,pady=10)

button_viewborrows=tk.Button(window,text="borrowed books",font=("Aptos",10))
button_viewborrows.pack(anchor="w",padx=10,pady=10)

label_viewborrows=tk.Label(window,text="",font=("Aptos",10))
label_viewborrows.pack(anchor="w",padx=10,pady=10)
window.mainloop()

