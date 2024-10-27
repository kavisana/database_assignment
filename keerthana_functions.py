#modify this module to include the function definitions
#Developed by :   Keerthana Avisana
import sqlite3
import os
def create_database_file(file_name):
    try:
        conn = sqlite3.connect(file_name)
    except sqlite3.Error as e:
        print(e)
    else:
        print('Created the database file.')
        return conn
    
def create_rep_table(database_connection):
    #use the connection object to create the database table
    #Create a function that will create the rep table and add data to it. 
    #Use the data in sql_commands.txt to help you with it.
    try:
        cursor = database_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS rep (
                          rep_num CHAR(2) PRIMARY KEY,
                          last_name CHAR(15),
                          first_name CHAR(15),
                          street CHAR(15),
                          city CHAR(15),
                          state CHAR(2),
                          zip CHAR(5),
                          commission DECIMAL(7,2),
                          rate DECIMAL(3,2)
                          )''')
        print("Rep table created.")
        cursor.execute("INSERT INTO rep VALUES ('20', 'Avisana', 'Keerthana', '624 Randall', 'Grove', 'FL', '33321', 20542.50, 0.05)")
        database_connection.commit()
        print("Data inserted into rep table.")
    except sqlite3.Error as e:
        print("Error creating or inserting data in rep table:", e)
    pass
def create_customer_table(database_connection):
    #use the connection object to create the database table
    #Create a function that will create the customer table and add the data to it.
    # Use the data in sql_commands.txt to help you with it.
    try:
        cursor = database_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS customer (
                          customer_num CHAR(3) PRIMARY KEY,
                          customer_name CHAR(35) NOT NULL,
                          street CHAR(15),
                          city CHAR(15),
                          state CHAR(2),
                          zip CHAR(5),
                          balance DECIMAL(8,2),
                          credit_limit DECIMAL(8,2),
                          rep_num CHAR(2)
                          )''')
        print("Customer table created.")
        
        # Insert sample data
        cursor.execute("INSERT INTO customer VALUES ('148', 'Al''s Appliance and Sport', '2837 Greenway', 'Fillmore', 'FL', '33336', 6550.00, 7500.00, '20')")
        database_connection.commit()
        print("Data inserted into customer table.")
    except sqlite3.Error as e:
        print("Error creating or inserting data in customer table:", e)
    pass
def insert_a_customer_record(database_connection):
    #Create a function that prompts the user for a rep number. 
    # If the result is not empty, display the first record.
    try:
        customer_num = input("Enter customer number: ")
        customer_name = input("Enter customer name: ")
        street = input("Enter street address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter ZIP code: ")
        balance = float(input("Enter balance: "))
        credit_limit = float(input("Enter credit limit: "))
        rep_num = input("Enter rep number associated with the customer: ")
        
        cursor = database_connection.cursor()
        cursor.execute("INSERT INTO customer (customer_num, customer_name, street, city, state, zip, balance, credit_limit, rep_num) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (customer_num, customer_name, street, city, state, zip_code, balance, credit_limit, rep_num))
        database_connection.commit()
        print("Customer record inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting customer record:", e)
    pass
def query_rep_table(database_connection):
    #Create a function that prompts the user for a rep number. 
    # If the result is not empty, display the first record.
    try:
        rep_num = input("Enter rep number to search: ")
        cursor = database_connection.cursor()
        cursor.execute("SELECT * FROM rep WHERE rep_num = ?", (rep_num,))
        record = cursor.fetchone()
        if record:
            print("Record found:", record)
        else:
            print("No record found.")
    except sqlite3.Error as e:
        print("Error fetching rep record:", e)
    pass
def update_rep_table(database_connection):
    #Create a function that prompts the user for a rep number.  
    # Then use the rep number to update the rep commission if it is in the [0.0 to 0.20]  range
    try:
        rep_num = input("Enter rep number to update commission: ")
        new_commission = float(input("Enter new commission rate (between 0.0 and 0.20): "))
        if 0.0 <= new_commission <= 0.20:
            cursor = database_connection.cursor()
            cursor.execute("UPDATE rep SET commission = ? WHERE rep_num = ?", (new_commission, rep_num))
            database_connection.commit()
            print("Commission updated successfully.")
        else:
            print("Commission rate is out of range.")
    except sqlite3.Error as e:
        print("Error updating commission:", e)
    pass
def delete_customer_record(database_connection):
    # Create a function that prompts the user for a customer number.  
    # if the customer number exists, confirm for deletion and 
    # then and delete then delete that customer 
    try:
        customer_num = input("Enter customer number to delete: ")
        confirm = input(f"Are you sure you want to delete customer {customer_num}? (y/n): ")
        if confirm.lower() == 'y':
            cursor = database_connection.cursor()
            cursor.execute("DELETE FROM customer WHERE customer_num = ?", (customer_num,))
            database_connection.commit()
            print("Customer record deleted successfully.")
        else:
            print("Deletion canceled.")
    except sqlite3.Error as e:
        print("Error deleting customer record:", e)
    pass
def delete_database(file_name, database_connection):
    # Create a function that deletes the database.  Verify that the file exists. 
    # Close the connection.  Then confirm the user really wants to delete the file,  Then delete the file.
    if os.path.exists(file_name):
        confirm = input("Are you sure you want to delete the database? (y/n): ")
        if confirm.lower() == 'y':
            database_connection.close()
            os.remove(file_name)
            print("Database deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Database file does not exist.")
    pass
