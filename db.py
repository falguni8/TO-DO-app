import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('todo.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Execute a query to fetch all data from the task table
cursor.execute("SELECT * FROM todo")

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Print out each row
for row in rows:
    print(row)

# Close the connection
connection.close()