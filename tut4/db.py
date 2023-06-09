import pymysql

conn = pymysql.connect(
    host= 'sql8.freesqldatabase.com',
    database= 'sql8624116',
    user= 'sql8624116',
    password= 'MDdE6Yt9PL',
    charset='utf8mb4',
    cursorclass= pymysql.cursors.DictCursor
)

cursor = conn.cursor()
sql_query = """CREATE TABLE books(
    id integer PRIMARY KEY AUTO_INCREMENT,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
    )"""
cursor.execute(sql_query)
conn.close()
