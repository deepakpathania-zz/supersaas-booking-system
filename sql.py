import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect('sample.db') as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""DROP TABLE posts""")
    c.execute('CREATE TABLE posts(title TEXT, details TEXT)')

    # insert dummy data into the table
    c.execute('INSERT INTO posts VALUES("Coference room 1", "259969")')
    c.execute('INSERT INTO posts VALUES("Conference Room 2", "259970")')
    c.execute('INSERT INTO posts VALUES("Conference Room 3", "259971")')
    c.execute('INSERT INTO posts VALUES("Conference Room 4", "259972")')
    c.execute('INSERT INTO posts VALUES("Conference Room 5", "259973")')