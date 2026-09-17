import sqlite3
from datetime import datetime

#The name of the database file to be used
finance = "finances.db"


#Actually creating the database/table if it doesn't exist yet. Setup function basically.
def make_database():
    connection = sqlite3.connect(finance)
    cursor = connection.cursor()

    # Creating a table with the columns/rows of id, category, amount, and description. The id is set to auto increment.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS finances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            specifics TEXT,
            amount REAL,
            description TEXT
        )
    """)
    connection.commit()
    connection.close()

#Using cursor here to like grab the databse if that makes sense
def make_finances(category, specifics, amount, description):
    connection = sqlite3.connect(finance)
    cursor = connection.cursor()

    #? can be used to place values in the database. I figured out that SQL Injection is a thing, so ? are good.
    cursor.execute("""
        INSERT INTO finances (category, specifics, amount, description) 
        VALUES (?, ?, ?, ?)
    """, (category, specifics, amount, description))
    
    connection.commit()
    connection.close()




#DISPLAY aspects here. So, with this, the database will actually show on the terminal properly 
def show_all_finances():
    connection = sqlite3.connect(finance)
    cursor = connection.cursor()

    #All the rows/columns are being selected with the * and being displayed
    cursor.execute("SELECT * FROM finances")
    all_rows = cursor.fetchall()

    #Using a for loop to go through each row to print out the contents. 
    #0 is id, 1 is category, 2 is specifics, 3 is amount, 4 is description
    print("\n--- ALL FINANCES ---")
    for row in all_rows:
        print(f"ID: {row[0]} | Category: {row[1]} | Specifics: {row[2]} | Amount: ${row[3]} | Info: {row[4]}")
    print("--------------------\n")
    connection.close()


"""
This makes sure everything runs properly. The if statement is there to ensure that the program runs if
the file is executed directly. 

As of September 17th, I just added an input system to allow users to determine what they want to see
"""
if __name__ == "__main__":
    make_database()

    while True:
        print("Welcome to the Finance Journal!")
        print("1. Add a new finance entry")
        print("2. Show all finance entries")
        print("3. Exit")

        choice = input("Please select an option (1, 2, or 3): ")

        if choice == "1":
            category = input("Enter the category: ")
            specifics = input("Enter the specifics: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter a description: ")
            make_finances(category, specifics, amount, description)
        elif choice == "2":
            show_all_finances()
        elif choice == "3":
            print("Exiting the Finance Journal. Goodbye and Thanks!")
            break
        else:
            print("Invalid. Enter again.")

    
    make_finances("Food", "College Lunch", 10.50, "Lunch at campus cafe")
    make_finances("Clothes", "New Shoes", 90.00, "Updated shoes")
    make_finances("Entertainment", "Blockbuster Movie", 13.00, "Movie night")


show_all_finances()