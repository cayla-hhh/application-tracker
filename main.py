import sqlite3

conn = sqlite3.connect('job_tracker.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        User_ID INTEGER PRIMARY KEY,
        Username TEXT,
        Email TEXT UNIQUE,
        Password_Hash TEXT           
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Applications (
        App_ID INTEGER PRIMARY KEY,
        User_ID INTEGER,
        Job_Title TEXT,
        Company TEXT,
        Deadline TEXT,
        Status Text,
        FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
    )            
''')
conn.commit()

cursor.execute('''
    INSERT OR IGNORE INTO Users (Username, Email, Password_Hash)
    VALUES ('text_user', 'test@email.com', 'pass123')
''')
conn.commit()

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
print(users)

