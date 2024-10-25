import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="blahblahblah",
)

mycursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
mycursor.close()
mydb.close()
