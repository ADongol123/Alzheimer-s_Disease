import mysql.connector

# Database connection setup
db_config = {
    'host': 'localhost',  # Change if not running locally
    'user': 'root',       # Your MySQL username
    'password': 'ASD@1234dsa',  # Your MySQL password
    'database': 'test_db',   # Your database name
}

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create a table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS posts (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    body TEXT
);
"""
cursor.execute(create_table_query)

# Insert data into the table
insert_query = "INSERT INTO posts (id, title, body) VALUES (%s, %s, %s)"
for item in json_data:
    cursor.execute(insert_query, (item['id'], item['title'], item['body']))

# Commit the changes and close the connection
conn.commit()
print("Data inserted into MySQL successfully!")
cursor.close()
conn.close()
