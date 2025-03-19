import mysql.connector

# Connect to MySQL
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ncc1701@"  # ✅ Removed extra comma
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database (Fixed hyphen issue)
cursorObject.execute("CREATE DATABASE CRM_Proj")

# Close the cursor and connection
cursorObject.close()
dataBase.close()

print("Database 'CRM_Proj' created successfully.")
