# import sqlite functions for the program
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

# Create the "book" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        qty INT
    )
''')

# Insert sample data into the "book" table
cursor.executemany('''
    INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)
''', [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
])

# menu loop so that user can see the menu again once a action is performed
while True:
    print('''
    Please select an option below to perform an action on the database:
    1 - Add a book to the database
    2 - Update a book's information in the database
    3 - Delete a book from the database
    4 - Search for a book in the database
    5 - Exit program
    ''')

# variable to store users input 
    User_Choice = input("Please enter your choice: ")

# logic to see what the user selected

# if user entered option 1 the program will ask the user 
# for book details then will add the book they made into the database
    if User_Choice == "1":
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        qty = int(input("Enter the quantity: "))
        cursor.execute("INSERT INTO book (title, author, qty) VALUES (?, ?, ?)", (title, author, qty))
        conn.commit()
        print("Book added to the database.")

# if the user entered option 2 the program will
# ask the user for the id of the book they want to update then 
# the program will ask the user to add the new details if the book exists
    elif User_Choice == "2":
        book_id = int(input("Enter the ID of the book you want to update: "))
        new_title = input("Enter the new title: ")
        new_author = input("Enter the new author: ")
        new_qty = int(input("Enter the new quantity: "))
        cursor.execute("UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?", (new_title, new_author, new_qty, book_id))
        conn.commit()
        print("Book information updated.")

# if the user enters option 3 the program will as the user what id of the book they want to delete is 
# this will nly work if the book exists if not the program will print a appropriate message
    elif User_Choice == "3":
        book_id = int(input("Enter the ID of the book you want to delete: "))
        cursor.execute("SELECT id FROM book WHERE id = ?", (book_id,))
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
            conn.commit()
            print("Book deleted successfully.")
        else:
            print("Book not found.")

# if the user  enters option 4 the program will ask the user for the id of the book they wan to see
# then if the book is there the program will display it
    elif User_Choice == "4":
        search_title = input("Enter the title of the book you want to find: ")
        cursor.execute("SELECT * FROM book WHERE title = ?", (search_title,))
        book = cursor.fetchone()
        if book:
            print("Book found:")
            print("ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Quantity:", book[3])
        else:
            print("Book not found.")

# if the user enters option 5 the program will say bye and exit
    elif User_Choice == "5":
        print("Bye!!")
        break

# if the user enters a invalid option the program will print this
    else:
        print("Invalid input, please try again!")

# saves and closes the database
conn.close()